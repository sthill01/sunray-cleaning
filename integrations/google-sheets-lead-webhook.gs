const LEAD_SHEET_NAME = "Lead Ledger";
const FILTERED_SPAM_SHEET_NAME = "Filtered Spam";
const SPREADSHEET_ID = "SET_IN_DEPLOYED_CODE_GS";
const MOUNTAIN_TIME_ZONE = "America/Denver";
const DEDUPE_WINDOW_MS = 10 * 60 * 1000;
const DEDUPE_SCAN_LIMIT = 250;

const LEGACY_LEAD_FIELDS = [
  { key: "submittedAt", label: "Submitted At" },
  { key: "first-name", label: "First Name" },
  { key: "name", label: "Name" },
  { key: "phone", label: "Phone" },
  { key: "email", label: "Email" },
  { key: "service-area", label: "City or Neighborhood" },
  { key: "service-type", label: "Service Type" },
  { key: "home-size", label: "Home Size" },
  { key: "preferred-timing", label: "Preferred Timing" },
  { key: "notes", label: "Notes" },
  { key: "message", label: "Message" },
  { key: "pageUrl", label: "Page URL" },
  { key: "first_landing_page", label: "First Landing Page" },
  { key: "landing_page", label: "Landing Page" },
  { key: "referrer", label: "Referrer" },
  { key: "gclid", label: "GCLID" },
  { key: "gbraid", label: "GBRAID" },
  { key: "wbraid", label: "WBRAID" },
  { key: "msclkid", label: "Microsoft Click ID" },
  { key: "fbclid", label: "Facebook Click ID" },
  { key: "ttclid", label: "TikTok Click ID" },
  { key: "li_fat_id", label: "LinkedIn Click ID" },
  { key: "utm_source", label: "UTM Source" },
  { key: "utm_medium", label: "UTM Medium" },
  { key: "utm_campaign", label: "UTM Campaign" },
  { key: "utm_term", label: "UTM Term" },
  { key: "utm_content", label: "UTM Content" },
  { key: "utm_id", label: "UTM ID" },
  { key: "source", label: "Source" },
  { key: "attribution_updated_at", label: "Attribution Updated At" },
];

const LEGACY_SPAM_FIELDS = [
  { key: "submittedAt", label: "Submitted At" },
  { key: "spamStatus", label: "Spam Status" },
  { key: "spamScore", label: "Spam Score" },
  { key: "spamReasons", label: "Spam Reasons" },
  { key: "spamReviewNote", label: "Review Note" },
  { key: "first-name", label: "First Name" },
  { key: "name", label: "Name" },
  { key: "phone", label: "Phone" },
  { key: "email", label: "Email" },
  { key: "service-area", label: "City or Neighborhood" },
  { key: "service-type", label: "Service Type" },
  { key: "home-size", label: "Home Size" },
  { key: "preferred-timing", label: "Preferred Timing" },
  { key: "notes", label: "Notes" },
  { key: "message", label: "Message" },
  { key: "pageUrl", label: "Page URL" },
  { key: "first_landing_page", label: "First Landing Page" },
  { key: "landing_page", label: "Landing Page" },
  { key: "referrer", label: "Referrer" },
  { key: "gclid", label: "GCLID" },
  { key: "gbraid", label: "GBRAID" },
  { key: "wbraid", label: "WBRAID" },
  { key: "msclkid", label: "Microsoft Click ID" },
  { key: "fbclid", label: "Facebook Click ID" },
  { key: "ttclid", label: "TikTok Click ID" },
  { key: "li_fat_id", label: "LinkedIn Click ID" },
  { key: "utm_source", label: "UTM Source" },
  { key: "utm_medium", label: "UTM Medium" },
  { key: "utm_campaign", label: "UTM Campaign" },
  { key: "utm_term", label: "UTM Term" },
  { key: "utm_content", label: "UTM Content" },
  { key: "utm_id", label: "UTM ID" },
  { key: "source", label: "Source" },
  { key: "attribution_updated_at", label: "Attribution Updated At" },
  { key: "filteredAsSpam", label: "Filtered As Spam" },
];

const VALUE_TRACK_FIELDS = [
  { key: "campaign_id", label: "Campaign ID" },
  { key: "ad_group_id", label: "Ad Group ID" },
  { key: "asset_group_id", label: "Asset Group ID" },
  { key: "creative_id", label: "Creative ID" },
  { key: "match_type", label: "Match Type" },
  { key: "network", label: "Network" },
  { key: "device", label: "Device" },
];

const TOUCH_MARKETING_FIELDS = [
  { key: "gclid", label: "GCLID" },
  { key: "gbraid", label: "GBRAID" },
  { key: "wbraid", label: "WBRAID" },
  { key: "msclkid", label: "Microsoft Click ID" },
  { key: "fbclid", label: "Facebook Click ID" },
  { key: "ttclid", label: "TikTok Click ID" },
  { key: "li_fat_id", label: "LinkedIn Click ID" },
  { key: "utm_source", label: "UTM Source" },
  { key: "utm_medium", label: "UTM Medium" },
  { key: "utm_campaign", label: "UTM Campaign" },
  { key: "utm_term", label: "UTM Term" },
  { key: "utm_content", label: "UTM Content" },
  { key: "utm_id", label: "UTM ID" },
].concat(VALUE_TRACK_FIELDS);

const PHASE_ONE_FIELDS = [
  { key: "leadId", label: "Lead ID" },
  { key: "submittedAtUtcIso", label: "Submitted At UTC ISO" },
  { key: "leadTimestampMt", label: "Lead Timestamp (MT)" },
  { key: "leadDateMt", label: "Lead Date (MT)" },
  { key: "leadTimeMt", label: "Lead Time (MT)" },
  { key: "attribution_session_id", label: "Attribution Session ID" },
  { key: "attribution_expires_at", label: "Attribution Expires At" },
  { key: "first_touch_at", label: "First Touch At" },
  { key: "first_touch_landing_page", label: "First Touch Landing Page" },
  { key: "first_touch_referrer", label: "First Touch Referrer" },
  { key: "latest_touch_at", label: "Latest Touch At" },
  { key: "latest_touch_landing_page", label: "Latest Touch Landing Page" },
  { key: "latest_touch_referrer", label: "Latest Touch Referrer" },
  { key: "dedupeFingerprint", label: "Dedupe Fingerprint" },
].concat(
  VALUE_TRACK_FIELDS,
  TOUCH_MARKETING_FIELDS.map((field) => ({ key: `first_touch_${field.key}`, label: `First Touch ${field.label}` })),
  TOUCH_MARKETING_FIELDS.map((field) => ({ key: `latest_touch_${field.key}`, label: `Latest Touch ${field.label}` })),
);

const LEAD_FIELDS = LEGACY_LEAD_FIELDS.concat(PHASE_ONE_FIELDS);
const SPAM_FIELDS = LEGACY_SPAM_FIELDS.concat(PHASE_ONE_FIELDS);

function doPost(event) {
  const lock = LockService.getScriptLock();

  try {
    const payload = JSON.parse((event && event.postData && event.postData.contents) || "{}");
    const isSpam = payload.filteredAsSpam === true || String(payload.filteredAsSpam || "").toLowerCase() === "true";
    const fields = isSpam ? SPAM_FIELDS : LEAD_FIELDS;
    const submittedDate = parseSubmittedDate(payload.submittedAt);
    const fingerprint = createLeadFingerprint(payload);

    lock.waitLock(10000);
    const sheetState = getSheetState(isSpam ? FILTERED_SPAM_SHEET_NAME : LEAD_SHEET_NAME, fields);
    const duplicate = findDuplicate(sheetState.sheet, sheetState.headers, payload.leadId, fingerprint, submittedDate);
    if (duplicate) {
      return jsonResponse({
        ok: true,
        duplicate: true,
        duplicateBy: duplicate.duplicateBy,
        leadId: duplicate.leadId || payload.leadId || "",
      });
    }

    const row = buildRow(sheetState.headers, fields, payload, submittedDate, fingerprint);
    sheetState.sheet.appendRow(row);
    applyDateFormats(sheetState.sheet, sheetState.headers, sheetState.sheet.getLastRow());

    return jsonResponse({ ok: true, duplicate: false, leadId: payload.leadId || "" });
  } catch (error) {
    return jsonResponse({ ok: false, error: String(error) });
  } finally {
    if (lock.hasLock()) lock.releaseLock();
  }
}

function doGet() {
  try {
    const spreadsheet = getSpreadsheet();
    const sheet = spreadsheet.getSheetByName(LEAD_SHEET_NAME);
    return jsonResponse({
      ok: true,
      schema: "sunray-lead-ledger-v2",
      sheetName: LEAD_SHEET_NAME,
      sheetReady: Boolean(sheet),
    });
  } catch (error) {
    return jsonResponse({ ok: false, schema: "sunray-lead-ledger-v2", error: String(error) });
  }
}

function setupLeadSheets() {
  const leads = getSheetState(LEAD_SHEET_NAME, LEAD_FIELDS);
  const spam = getSheetState(FILTERED_SPAM_SHEET_NAME, SPAM_FIELDS);
  return {
    ok: true,
    schema: "sunray-lead-ledger-v2",
    sheets: [leads.sheet.getName(), spam.sheet.getName()],
  };
}

function getSpreadsheet() {
  const propertyId = PropertiesService.getScriptProperties().getProperty("SUNRAY_LEAD_SPREADSHEET_ID");
  const configuredId = String(propertyId || SPREADSHEET_ID || "").trim();
  if (configuredId && configuredId !== "SET_IN_DEPLOYED_CODE_GS") {
    return SpreadsheetApp.openById(configuredId);
  }

  const activeSpreadsheet = SpreadsheetApp.getActiveSpreadsheet();
  if (!activeSpreadsheet) {
    throw new Error("Set SPREADSHEET_ID in the deployed Code.gs before publishing the web app.");
  }
  return activeSpreadsheet;
}

function getSheetState(sheetName, fields) {
  const spreadsheet = getSpreadsheet();
  const sheet = spreadsheet.getSheetByName(sheetName) || spreadsheet.insertSheet(sheetName);
  const lastColumn = sheet.getLastColumn();
  let headers = lastColumn > 0 ? sheet.getRange(1, 1, 1, lastColumn).getValues()[0].map(String) : [];
  const existingHeaders = new Set(headers.filter(Boolean));
  const missingHeaders = fields.map((field) => field.label).filter((label) => !existingHeaders.has(label));

  if (missingHeaders.length) {
    const startColumn = headers.length + 1;
    const requiredColumns = headers.length + missingHeaders.length;
    const currentMaxColumns = sheet.getMaxColumns();
    if (requiredColumns > currentMaxColumns) {
      sheet.insertColumnsAfter(currentMaxColumns, requiredColumns - currentMaxColumns);
    }
    sheet.getRange(1, startColumn, 1, missingHeaders.length).setValues([missingHeaders]);
    sheet
      .getRange(1, startColumn, 1, missingHeaders.length)
      .setFontWeight("bold")
      .setBackground("#f1f3f4");
    sheet.autoResizeColumns(startColumn, missingHeaders.length);
    headers = headers.concat(missingHeaders);
  }

  sheet.setFrozenRows(1);
  return { sheet, headers };
}

function buildRow(headers, fields, payload, submittedDate, fingerprint) {
  const fieldsByLabel = new Map(fields.map((field) => [field.label, field]));
  const populatedLabels = new Set();

  return headers.map((header) => {
    const field = fieldsByLabel.get(header);
    if (!field || populatedLabels.has(header)) return "";
    populatedLabels.add(header);
    return getFieldValue(field.key, payload, submittedDate, fingerprint);
  });
}

function getFieldValue(key, payload, submittedDate, fingerprint) {
  if (key === "submittedAt") return submittedDate;
  if (key === "submittedAtUtcIso") return submittedDate.toISOString();
  if (key === "leadTimestampMt") return mountainDateFormula(submittedDate, "timestamp");
  if (key === "leadDateMt") return mountainDateFormula(submittedDate, "date");
  if (key === "leadTimeMt") return mountainDateFormula(submittedDate, "time");
  if (key === "dedupeFingerprint") return fingerprint;
  const value = Object.prototype.hasOwnProperty.call(payload, key) ? payload[key] : "";
  return escapeSheetValue(value);
}

function escapeSheetValue(value) {
  if (typeof value !== "string") return value;
  return /^[=+\-@]/.test(value.trimStart()) ? `'${value}` : value;
}

function parseSubmittedDate(value) {
  const date = new Date(value || Date.now());
  return Number.isNaN(date.getTime()) ? new Date() : date;
}

function mountainDateFormula(date, kind) {
  const parts = Utilities.formatDate(date, MOUNTAIN_TIME_ZONE, "yyyy,M,d,H,m,s")
    .split(",")
    .map(Number);
  const dateFormula = `DATE(${parts[0]},${parts[1]},${parts[2]})`;
  const timeFormula = `TIME(${parts[3]},${parts[4]},${parts[5]})`;
  if (kind === "date") return `=${dateFormula}`;
  if (kind === "time") return `=${timeFormula}`;
  return `=${dateFormula}+${timeFormula}`;
}

function applyDateFormats(sheet, headers, rowNumber) {
  setFormatByHeader(sheet, headers, rowNumber, "Submitted At", "yyyy-mm-dd hh:mm:ss");
  setFormatByHeader(sheet, headers, rowNumber, "Lead Timestamp (MT)", "yyyy-mm-dd hh:mm:ss");
  setFormatByHeader(sheet, headers, rowNumber, "Lead Date (MT)", "yyyy-mm-dd");
  setFormatByHeader(sheet, headers, rowNumber, "Lead Time (MT)", "h:mm:ss AM/PM");
}

function setFormatByHeader(sheet, headers, rowNumber, header, numberFormat) {
  const column = headers.indexOf(header) + 1;
  if (column > 0) sheet.getRange(rowNumber, column).setNumberFormat(numberFormat);
}

function findDuplicate(sheet, headers, leadId, fingerprint, submittedDate) {
  const lastRow = sheet.getLastRow();
  if (lastRow < 2) return null;
  const startRow = Math.max(2, lastRow - DEDUPE_SCAN_LIMIT + 1);
  const rows = sheet.getRange(startRow, 1, lastRow - startRow + 1, headers.length).getValues();
  const leadIdColumn = headers.indexOf("Lead ID");
  const fingerprintColumn = headers.indexOf("Dedupe Fingerprint");
  const submittedAtColumn = headers.indexOf("Submitted At");

  for (let rowIndex = rows.length - 1; rowIndex >= 0; rowIndex -= 1) {
    const row = rows[rowIndex];
    const existingLeadId = leadIdColumn >= 0 ? String(row[leadIdColumn] || "") : "";
    if (leadId && existingLeadId === String(leadId)) {
      return { duplicateBy: "leadId", leadId: existingLeadId };
    }
    if (!fingerprint || fingerprintColumn < 0 || submittedAtColumn < 0) continue;
    if (String(row[fingerprintColumn] || "") !== fingerprint) continue;
    const existingDate = new Date(row[submittedAtColumn]);
    if (!Number.isNaN(existingDate.getTime()) && Math.abs(submittedDate.getTime() - existingDate.getTime()) <= DEDUPE_WINDOW_MS) {
      return { duplicateBy: "fingerprint", leadId: existingLeadId };
    }
  }

  return null;
}

function createLeadFingerprint(payload) {
  const values = [
    payload["first-name"] || payload.name,
    String(payload.phone || "").replace(/\D/g, ""),
    payload.email,
    payload["service-area"],
    payload["service-type"],
    payload["home-size"],
    payload["preferred-timing"],
    payload.notes || payload.message,
  ].map(normalizeFingerprintValue);
  if (!values.some(Boolean)) return "";
  const bytes = Utilities.computeDigest(Utilities.DigestAlgorithm.SHA_256, values.join("|"), Utilities.Charset.UTF_8);
  return bytes.map((byte) => ((byte + 256) % 256).toString(16).padStart(2, "0")).join("");
}

function normalizeFingerprintValue(value) {
  return String(value || "").toLowerCase().replace(/\s+/g, " ").trim();
}

function jsonResponse(payload) {
  return ContentService.createTextOutput(JSON.stringify(payload))
    .setMimeType(ContentService.MimeType.JSON);
}
