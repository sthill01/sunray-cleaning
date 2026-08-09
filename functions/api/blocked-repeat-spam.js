// Confirmed repeat spam identities reported by Sun Ray operations.
// Keep this list narrow to avoid blocking legitimate prospects.
export const BLOCKED_REPEAT_SPAM_EMAILS = new Set([
  "henrydixon487@gmail.com",
]);

export const BLOCKED_REPEAT_SPAM_NAMES = new Set([
  "roberttig",
]);

export const BLOCKED_REPEAT_SPAM_PHONES = new Set([
  "85999923842",
]);

export function isConfirmedRepeatSpam(quote = {}) {
  const email = String(quote.email || "").trim().toLowerCase();
  const name = String(quote["first-name"] || quote.name || "")
    .toLowerCase()
    .replace(/[^a-z0-9]/g, "");
  const phone = String(quote.phone || "").replace(/\D/g, "");

  return (
    BLOCKED_REPEAT_SPAM_EMAILS.has(email) ||
    BLOCKED_REPEAT_SPAM_NAMES.has(name) ||
    BLOCKED_REPEAT_SPAM_PHONES.has(phone)
  );
}
