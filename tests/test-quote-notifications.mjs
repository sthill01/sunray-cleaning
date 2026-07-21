import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";

const root = new URL("../", import.meta.url);
const defaultRecipients = [
  "quotes@sunray-cleaning.com",
  "cyntya@sunray-cleaning.com",
  "cyntyahill@gmail.com",
  "sunrayservices17@gmail.com",
  "sthill01@gmail.com",
];

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
  test(`${handler.name} sends legitimate leads to email, Pushover, SMS, and Sheets`, async () => {
    const module = await importSource(handler.source);
    const calls = installFetchRecorder();
    const env = {
      RESEND_API_KEY: "resend-test-key",
      BREVO_API_KEY: "brevo-api-key",
      BREVO_SMS_SENDER: "SunRay",
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
      utm_source: "google",
      notes: "Please call after 3 PM.",
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
        "https://api.brevo.com/v3/transactionalSMS/send",
        "https://api.brevo.com/v3/transactionalSMS/send",
        "https://sheets.example/leads",
      ],
    );

    const resendBody = JSON.parse(calls[0].init.body);
    assert.deepEqual(resendBody.to, defaultRecipients);
    assert.equal(resendBody.reply_to, "lead@example.com");

    const sheetBody = JSON.parse(calls[4].init.body);
    const expectedMountainTime = new Intl.DateTimeFormat("en-US", {
      timeZone: "America/Denver",
      year: "numeric",
      month: "short",
      day: "numeric",
      hour: "numeric",
      minute: "2-digit",
      second: "2-digit",
      timeZoneName: "short",
    }).format(new Date(sheetBody.submittedAt));
    assert.match(
      resendBody.text,
      new RegExp(`Submitted at \\(Mountain Time\\): ${expectedMountainTime.replace(/[.*+?^${}()|[\\]\\\\]/g, "\\$&")}`),
    );

    const pushBody = new URLSearchParams(String(calls[1].init.body));
    assert.equal(pushBody.get("token"), "pushover-app-token");
    assert.equal(pushBody.get("user"), "pushover-group-key");
    assert.equal(pushBody.get("priority"), "1");
    assert.equal(pushBody.get("sound"), "cashregister");
    const expectedAlert = [
      "New website lead",
      "Name: Test Lead",
      "Phone: +1 435-555-0100",
      "Email: lead@example.com",
      "Service: Deep clean",
      "UTM source: google",
      "Location: Heber City",
      "Notes: Please call after 3 PM.",
    ].join("\n");
    assert.equal(pushBody.get("message"), expectedAlert);

    const smsBodies = calls.slice(2, 4).map((call) => JSON.parse(call.init.body));
    assert.equal(calls[2].init.headers["api-key"], "brevo-api-key");
    assert.deepEqual(smsBodies, [
      {
        sender: "SunRay",
        recipient: "18016042189",
        content: expectedAlert,
        type: "transactional",
        tag: "website-lead",
      },
      {
        sender: "SunRay",
        recipient: "18018501253",
        content: expectedAlert,
        type: "transactional",
        tag: "website-lead",
      },
    ]);
  });

  test(`${handler.name} keeps filtered spam out of email, Pushover, and SMS`, async () => {
    const module = await importSource(handler.source);
    const calls = installFetchRecorder();
    const env = {
      RESEND_API_KEY: "resend-test-key",
      BREVO_API_KEY: "brevo-api-key",
      BREVO_SMS_SENDER: "SunRay",
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

  test(`${handler.name} filters balance-link spam placed in the name field`, async () => {
    const module = await importSource(handler.source);
    const calls = installFetchRecorder();
    const env = {
      RESEND_API_KEY: "resend-test-key",
      BREVO_API_KEY: "brevo-api-key",
      BREVO_SMS_SENDER: "SunRay",
      SUNRAY_PUSHOVER_APP_TOKEN: "pushover-app-token",
      SUNRAY_PUSHOVER_GROUP_KEY: "pushover-group-key",
      SUNRAY_QUOTE_SHEETS_WEBHOOK_URL: "https://sheets.example/leads",
      SUNRAY_QUOTE_SPAM_WEBHOOK_URL: "https://sheets.example/spam",
    };
    const payload = {
      "first-name": "Transfer 236,538 $. GET -> graph.org/BALANCE-3682444-USD-04-21-2?hs=207a475660afe0aaa051de1c75113820",
      phone: "605466216884",
      email: "way197vrvvidx6@web-library.net",
      location: "05cglw",
      notes: "uk4zk9",
    };

    const response = await handler.run(module, makeRequest(payload), env);
    const result = await response.json();

    assert.equal(response.status, 200);
    assert.equal(result.ok, true);
    assert.equal(result.trackConversion, false);
    assert.deepEqual(calls.map((call) => call.url), ["https://sheets.example/spam"]);

    const spamAudit = JSON.parse(calls[0].init.body);
    assert.equal(spamAudit.filteredAsSpam, true);
    assert.equal(spamAudit.spamScore, 4);
    assert.match(spamAudit.spamReasons, /url_in_quote/);
  });
}
