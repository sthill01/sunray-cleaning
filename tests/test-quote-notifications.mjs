import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";

const root = new URL("../", import.meta.url);
const defaultRecipients = ["cyntyahill@gmail.com", "sunrayservices17@gmail.com", "sthill01@gmail.com"];

async function importSource(relativePath) {
  const source = await readFile(new URL(relativePath, root), "utf8");
  const encoded = Buffer.from(source).toString("base64");
  return import(`data:text/javascript;base64,${encoded}#${Date.now()}-${Math.random()}`);
}

function makeRequest(payload) {
  return new Request("https://www.sunray-cleaning.com/api/quote", {
    method: "POST",
    headers: {
      accept: "application/json",
      "content-type": "application/json",
      referer: "https://www.sunray-cleaning.com/contact/",
    },
    body: JSON.stringify(payload),
  });
}

function installFetchRecorder() {
  const calls = [];
  globalThis.fetch = async (input, init = {}) => {
    calls.push({ url: typeof input === "string" ? input : input.url, init });
    return Response.json({ status: 1 });
  };
  return calls;
}

const handlers = [
  {
    name: "Pages Function",
    source: "functions/api/quote.js",
    run: (module, request, env) => module.onRequestPost({ request, env }),
  },
  {
    name: "Worker",
    source: "worker.js",
    run: (module, request, env) => module.default.fetch(request, env),
  },
];

for (const handler of handlers) {
  test(`${handler.name} sends legitimate leads to three emails, Pushover, and Sheets`, async () => {
    const module = await importSource(handler.source);
    const calls = installFetchRecorder();
    const env = {
      RESEND_API_KEY: "resend-test-key",
      SUNRAY_PUSHOVER_APP_TOKEN: "pushover-app-token",
      SUNRAY_PUSHOVER_GROUP_KEY: "pushover-group-key",
      SUNRAY_QUOTE_SHEETS_WEBHOOK_URL: "https://sheets.example/leads",
      SUNRAY_QUOTE_SPAM_WEBHOOK_URL: "https://sheets.example/spam",
    };
    const payload = {
      "first-name": "Test Lead",
      phone: "+1 435-555-0100",
      email: "lead@example.com",
      "service-area": "Heber City",
      "service-type": "Deep clean",
      "preferred-timing": "Next week",
    };

    const response = await handler.run(module, makeRequest(payload), env);
    const result = await response.json();

    assert.equal(response.status, 200);
    assert.equal(result.ok, true);
    assert.equal(result.trackConversion, true);
    assert.deepEqual(
      calls.map((call) => call.url),
      [
        "https://api.resend.com/emails",
        "https://api.pushover.net/1/messages.json",
        "https://sheets.example/leads",
      ],
    );

    const resendBody = JSON.parse(calls[0].init.body);
    assert.deepEqual(resendBody.to, defaultRecipients);
    assert.equal(resendBody.reply_to, "lead@example.com");

    const pushBody = new URLSearchParams(String(calls[1].init.body));
    assert.equal(pushBody.get("token"), "pushover-app-token");
    assert.equal(pushBody.get("user"), "pushover-group-key");
    assert.equal(pushBody.get("priority"), "1");
    assert.equal(pushBody.get("sound"), "cashregister");
    assert.match(pushBody.get("message"), /Name: Test Lead/);
    assert.match(pushBody.get("message"), /Phone: \+1 435-555-0100/);
    assert.match(pushBody.get("message"), /City: Heber City/);
  });

  test(`${handler.name} keeps filtered spam out of email and Pushover`, async () => {
    const module = await importSource(handler.source);
    const calls = installFetchRecorder();
    const env = {
      RESEND_API_KEY: "resend-test-key",
      SUNRAY_PUSHOVER_APP_TOKEN: "pushover-app-token",
      SUNRAY_PUSHOVER_GROUP_KEY: "pushover-group-key",
      SUNRAY_QUOTE_SHEETS_WEBHOOK_URL: "https://sheets.example/leads",
      SUNRAY_QUOTE_SPAM_WEBHOOK_URL: "https://sheets.example/spam",
    };
    const payload = {
      "first-name": "Spam Test",
      phone: "+1 435-555-0101",
      "service-area": "Park City",
      website: "https://spam.example",
    };

    const response = await handler.run(module, makeRequest(payload), env);
    const result = await response.json();

    assert.equal(response.status, 200);
    assert.equal(result.ok, true);
    assert.equal(result.trackConversion, false);
    assert.deepEqual(calls.map((call) => call.url), ["https://sheets.example/spam"]);

    const spamAudit = JSON.parse(calls[0].init.body);
    assert.equal(spamAudit.filteredAsSpam, true);
    assert.equal(spamAudit.spamStatus, "Filtered before email or conversion tracking");
  });
}
