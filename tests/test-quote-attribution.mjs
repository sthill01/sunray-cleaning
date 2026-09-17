import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import vm from "node:vm";

const source = await readFile(new URL("../quote-modal-gpt.js", import.meta.url), "utf8");

function storage(initial = {}) {
  const values = new Map(Object.entries(initial));
  return {
    getItem(key) {
      return values.has(key) ? values.get(key) : null;
    },
    setItem(key, value) {
      values.set(key, String(value));
    },
    removeItem(key) {
      values.delete(key);
    },
  };
}

function runPage({ url, referrer = "", localStorage = storage(), sessionStorage = storage(), forms = [], fetch }) {
  const listeners = {};
  const location = new URL(url);
  const document = {
    referrer,
    body: { classList: { add() {}, remove() {} } },
    activeElement: null,
    addEventListener(name, callback) {
      listeners[name] = callback;
    },
    querySelector() {
      return null;
    },
    querySelectorAll(selector) {
      return selector === ".quote-form" ? forms : [];
    },
    createElement: element,
    createTextNode: (textContent) => ({ textContent }),
  };
  const window = { document, location, localStorage, sessionStorage, dataLayer: [] };
  window.window = window;
  vm.runInNewContext(source, {
    window,
    document,
    URL,
    URLSearchParams,
    fetch,
    FormData: class {
      constructor(form) { this.values = Object.fromEntries([...form.fields].map(([name, field]) => [name, field.value || ""])); }
    },
    Date,
    Math,
    Number,
    JSON,
    Object,
    Array,
    String,
    console,
  });
  listeners.DOMContentLoaded();
  return {
    localStorage,
    sessionStorage,
    attribution: JSON.parse(localStorage.getItem("sunray_attribution_v2")),
    dataLayer: window.dataLayer,
  };
}

function element(tagName) {
  return {
    tagName, attributes: {}, children: [], style: {}, value: "",
    setAttribute(name, value) { this.attributes[name] = value; },
    getAttribute(name) { return this.attributes[name] || null; },
    appendChild(child) { this.children.push(child); },
  };
}

function quoteForm() {
  const fields = new Map();
  const listeners = {};
  const register = (child) => {
    if (child.attributes?.name) fields.set(child.attributes.name, child);
    (child.children || []).forEach(register);
  };
  const grid = { appendChild: register };
  return {
    fields, listeners, className: "quote-form", reset() {},
    getAttribute(name) { return name === "action" ? "/api/quote" : name === "name" ? "quote" : ""; },
    appendChild: register,
    addEventListener(name, callback) { listeners[name] = callback; },
    querySelector(selector) {
      if (selector === ".field-grid") return grid;
      const name = selector.match(/\[name="([^"]+)"\]/)?.[1];
      return fields.get(name) || null;
    },
  };
}

test("first and latest touch capture UTMs, click IDs, and ValueTrack fields", () => {
  const first = runPage({
    url:
      "https://www.sunray-cleaning.com/contact/?gclid=G1&utm_source=google&utm_campaign=summit&campaign_id=123&ad_group_id=456&asset_group_id=789&creative_id=999&match_type=e&network=g&device=m",
    referrer: "https://www.google.com/",
  });
  const attribution = first.attribution;

  assert.equal(attribution.first_touch_gclid, "G1");
  assert.equal(attribution.latest_touch_gclid, "G1");
  assert.equal(attribution.first_touch_utm_campaign, "summit");
  assert.equal(attribution.latest_touch_campaign_id, "123");
  assert.equal(attribution.latest_touch_asset_group_id, "789");
  assert.equal(attribution.latest_touch_device, "m");
  assert.equal(attribution.gclid, "G1");
  assert.ok(Date.parse(attribution.attribution_expires_at) > Date.now());
  assert.match(attribution.attribution_session_id, /^session_/);
});

test("a new click clears absent latest-touch fields without erasing first touch", () => {
  const first = runPage({
    url: "https://www.sunray-cleaning.com/?gclid=G1&utm_source=google&utm_campaign=original&campaign_id=111&device=m",
  });
  const second = runPage({
    url: "https://www.sunray-cleaning.com/services/?gclid=G2&utm_source=google&campaign_id=222&network=x",
    referrer: "https://www.google.com/",
    localStorage: first.localStorage,
    sessionStorage: storage(),
  }).attribution;

  assert.equal(second.first_touch_gclid, "G1");
  assert.equal(second.first_touch_utm_campaign, "original");
  assert.equal(second.latest_touch_gclid, "G2");
  assert.equal(second.latest_touch_campaign_id, "222");
  assert.equal(second.latest_touch_utm_campaign, "");
  assert.equal(second.latest_touch_device, "");
  assert.equal(second.utm_campaign, "");
  assert.equal(second.device, "");
});

test("expired attribution starts a new clean session", () => {
  const localStorage = storage({
    sunray_attribution_v2: JSON.stringify({
      gclid: "EXPIRED",
      first_touch_gclid: "EXPIRED",
      attribution_expires_at: "2020-01-01T00:00:00.000Z",
    }),
  });
  const attribution = runPage({ url: "https://www.sunray-cleaning.com/contact/", localStorage }).attribution;

  assert.equal(attribution.gclid, undefined);
  assert.equal(attribution.first_touch_gclid, "");
  assert.match(attribution.first_touch_landing_page, /\/contact\/$/);
});

test("the successful form response supplies the immutable Lead ID to GTM", () => {
  assert.match(source, /sendLeadConversionEvent\(form, payload\.leadId\)/);
  assert.match(source, /pushTrackingEvent\("sunray_lead_form_submit", payload, leadId\)/);
  assert.match(source, /event_id: sanitizeAttributionValue\(eventId, 200\)/);
});

test("an untagged ChatGPT referral replaces an older Google click without erasing first touch", () => {
  const google = runPage({ url: "https://www.sunray-cleaning.com/?gclid=G1&utm_source=google&utm_campaign=older" });
  const ai = runPage({
    url: "https://www.sunray-cleaning.com/services/recurring-cleaning/",
    referrer: "https://chatgpt.com/c/private-conversation?q=private-details",
    localStorage: google.localStorage,
  }).attribution;
  assert.equal(ai.first_touch_acquisition_channel, "paid_google");
  assert.equal(ai.first_touch_gclid, "G1");
  assert.equal(ai.latest_touch_acquisition_channel, "ai_referral");
  assert.equal(ai.acquisition_source, "chatgpt");
  assert.equal(ai.acquisition_evidence, "referrer");
  assert.equal(ai.latest_touch_referrer, "https://chatgpt.com/");
  assert.equal(ai.gclid, "");
  assert.equal(ai.utm_campaign, "");
  assert.ok(!JSON.stringify(ai).includes("private-"));
});

test("paid OpenAI tags override a referring AI site and source-only ChatGPT tags stay referrals", () => {
  const paid = runPage({
    url: "https://www.sunray-cleaning.com/?utm_source=openai&utm_medium=cpc&utm_campaign=park_city",
    referrer: "https://chatgpt.com/",
  }).attribution;
  assert.equal(paid.acquisition_channel, "paid_openai");
  assert.equal(paid.acquisition_evidence, "paid_utm");
  const referral = runPage({ url: "https://www.sunray-cleaning.com/?utm_source=chatgpt.com" }).attribution;
  assert.equal(referral.acquisition_channel, "ai_referral");
  assert.equal(referral.acquisition_evidence, "utm_source");
});

test("Google paid clicks replace AI latest touch and keep AI discovery evidence", () => {
  const ai = runPage({ url: "https://www.sunray-cleaning.com/", referrer: "https://perplexity.ai/search/private" });
  const google = runPage({
    url: "https://www.sunray-cleaning.com/?gclid=G2&utm_source=google&utm_medium=cpc",
    referrer: "https://chatgpt.com/",
    localStorage: ai.localStorage,
  }).attribution;
  assert.equal(google.first_touch_acquisition_channel, "ai_referral");
  assert.equal(google.first_touch_acquisition_source, "perplexity");
  assert.equal(google.acquisition_channel, "paid_google");
  assert.equal(google.acquisition_evidence, "google_click_id");
});

test("internal navigation and a direct return preserve the latest known AI referral", () => {
  const first = runPage({ url: "https://www.sunray-cleaning.com/", referrer: "https://claude.ai/" });
  for (const referrer of ["https://www.sunray-cleaning.com/", "https://sunray-cleaning.com/services/", ""]) {
    const next = runPage({ url: "https://www.sunray-cleaning.com/contact/", referrer, localStorage: first.localStorage }).attribution;
    assert.equal(next.acquisition_channel, "ai_referral");
    assert.equal(next.acquisition_source, "claude");
    assert.equal(next.latest_touch_at, first.attribution.latest_touch_at);
  }
});

test("lookalike hosts are ordinary referrals and missing evidence stays unknown", () => {
  for (const referrer of ["https://chatgpt.com.attacker.example/", "https://notchatgpt.com/", "https://attacker.example/?source=chatgpt.com"]) {
    const attribution = runPage({ url: "https://www.sunray-cleaning.com/", referrer }).attribution;
    assert.equal(attribution.acquisition_channel, "referral");
  }
  for (const referrer of ["", "not a URL", "javascript:alert(1)"]) {
    const attribution = runPage({ url: "https://www.sunray-cleaning.com/", referrer }).attribution;
    assert.equal(attribution.acquisition_channel, "direct_or_unknown");
  }
});

test("older stored referrer paths and queries are removed without changing first-touch marketing", () => {
  const localStorage = storage({ sunray_attribution_v2: JSON.stringify({
    first_touch_at: "2026-09-01T00:00:00.000Z", latest_touch_at: "2026-09-01T00:00:00.000Z",
    first_touch_referrer: "https://chatgpt.com/c/private?email=private@example.com",
    latest_touch_referrer: "https://www.google.com/search?q=private",
    referrer: "https://chatgpt.com/c/private?email=private@example.com",
    latest_touch_gclid: "G1", first_touch_utm_source: "chatgpt.com",
    attribution_expires_at: "2099-01-01T00:00:00.000Z",
  }) });
  const attribution = runPage({ url: "https://www.sunray-cleaning.com/contact/", localStorage }).attribution;
  assert.equal(attribution.first_touch_acquisition_channel, "ai_referral");
  assert.equal(attribution.acquisition_channel, "paid_google");
  assert.equal(attribution.first_touch_referrer, "https://chatgpt.com/");
  assert.ok(!JSON.stringify(attribution).includes("private"));
});

test("optional self-report submits separately from observed attribution and reaches the Lead ID event", async () => {
  const form = quoteForm();
  let submitted;
  const page = runPage({
    url: "https://www.sunray-cleaning.com/?gclid=G1&utm_source=google&utm_medium=cpc",
    forms: [form],
    fetch: async (_url, request) => {
      submitted = request.body.values;
      return { ok: true, json: async () => ({ ok: true, trackConversion: true, leadId: "sr_verified" }) };
    },
  });
  const selfReport = form.fields.get("how-heard");
  assert.equal(selfReport.getAttribute("required"), null);
  assert.ok(selfReport.children.some((option) => option.value === "ChatGPT ad"));
  selfReport.value = "ChatGPT";
  form.listeners.submit({ currentTarget: form, preventDefault() {} });
  await new Promise((resolve) => setImmediate(resolve));
  assert.equal(submitted["how-heard"], "ChatGPT");
  assert.equal(submitted.acquisition_channel, "paid_google");
  assert.equal(submitted.first_touch_acquisition_evidence, "google_click_id");
  const event = page.dataLayer.find((item) => item.event === "sunray_lead_form_submit");
  assert.equal(event.event_id, "sr_verified");
  assert.equal(event.self_reported_source, "ChatGPT");
  assert.equal(event.acquisition_channel, "paid_google");
  assert.equal(event.referrer, undefined);
});
