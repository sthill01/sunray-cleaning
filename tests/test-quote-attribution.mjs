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

function runPage({ url, referrer = "", localStorage = storage(), sessionStorage = storage() }) {
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
    querySelectorAll() {
      return [];
    },
  };
  const window = { document, location, localStorage, sessionStorage, dataLayer: [] };
  window.window = window;
  vm.runInNewContext(source, {
    window,
    document,
    URLSearchParams,
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
