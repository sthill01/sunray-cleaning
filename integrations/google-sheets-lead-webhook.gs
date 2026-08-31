const LEAD_SHEET_NAME = "Leads";
const FILTERED_SPAM_SHEET_NAME = "Filtered Spam";

const LEAD_FIELDS = [
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
  { key: "how-heard", label: "How Did You Hear About Us?" },
];

const SPAM_FIELDS = [
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
  { key: "how-heard", label: "How Did You Hear About Us?" },
];

function doPost(event) {
  try {
    const payload = JSON.parse(event.postData.contents || "{}");
    const isSpam = payload.filteredAsSpam === true || String(payload.filteredAsSpam || "").toLowerCase() === "true";
    const fields = isSpam ? SPAM_FIELDS : LEAD_FIELDS;
    const sheet = getSheet(isSpam ? FILTERED_SPAM_SHEET_NAME : LEAD_SHEET_NAME, fields);
    const row = fields.map((field) => payload[field.key] || "");
    sheet.appendRow(row);

    return jsonResponse({ ok: true });
  } catch (error) {
    return jsonResponse({ ok: false, error: String(error) });
  }
}

function getSheet(sheetName, fields) {
  const spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
  const sheet = spreadsheet.getSheetByName(sheetName) || spreadsheet.insertSheet(sheetName);
  const headers = fields.map((field) => field.label);
  const currentHeaders = sheet.getRange(1, 1, 1, headers.length).getValues()[0];
  const needsHeaders = currentHeaders.join("") === "" || currentHeaders.join("|") !== headers.join("|");

  if (needsHeaders) {
    sheet.getRange(1, 1, 1, headers.length).setValues([headers]);
    sheet.setFrozenRows(1);
    sheet.getRange(1, 1, 1, headers.length).setFontWeight("bold").setBackground("#f1f3f4");
    sheet.autoResizeColumns(1, headers.length);
  }

  return sheet;
}

function jsonResponse(payload) {
  return ContentService.createTextOutput(JSON.stringify(payload))
    .setMimeType(ContentService.MimeType.JSON);
}
