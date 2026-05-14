# Google Tag Manager Conversion Tracking

Sun Ray production tracking is managed through Google Tag Manager on the Cloudflare Pages build. The site code should only push `dataLayer` events; GA4, Google Ads conversions, conversion linker, remarketing, and reporting tags should be managed in GTM.

## Current Site Install

- Cloudflare Pages source repo: `C:\Users\sthil\Documents\GitHub\sunray-cleaning`
- Build command: `npm run build:production`
- Build output: `cloudflare-preview`
- GTM container: `GTM-W78H8S3C`
- GTM injection point: `tools/build-cloudflare-preview.py`
- Runtime script source: `quote-modal-gpt.js`
- Built runtime script: `cloudflare-preview/quote-modal.js`

The build script injects GTM into every generated page, so do not paste separate per-page Google Ads or GA4 snippets into the HTML source.

## Data Layer Events

`quote-modal-gpt.js` pushes these events into `window.dataLayer`:

| Data layer event | When it fires | GTM use |
| --- | --- | --- |
| `sunray_lead_form_submit` | Quote form API submission succeeds | Primary lead conversion |
| `sunray_call_cta_click` | Visitor clicks a `tel:` call link | Call-click conversion or key event |
| `sunray_text_cta_click` | Visitor clicks an `sms:` text link | Text-click conversion or key event |
| `sunray_quote_cta_click` | Visitor clicks a Get a quote / quote-form CTA | Soft intent event |
| `sunray_quote_submit_click` | Visitor clicks the quote submit button before validation/API success | Diagnostic event only |

Each event can include these parameters:

| Parameter | Meaning |
| --- | --- |
| `event_id` | Unique event ID for dedupe/debugging |
| `cta_type` | `quote`, `call`, `text`, or `submit` |
| `cta_text` | Button/link text or aria label |
| `cta_url` | Link href, such as `tel:+18016042189` |
| `cta_section` | Nearby header/section/footer/form label |
| `form_name` | Quote form name on successful submit |
| `lead_type` | `quote_form` on successful submit |
| `page_location` | Full page URL |
| `page_title` | Browser page title |
| `conversion_value` | `1` by default |
| `currency` | `USD` |

## Recommended GTM Variables

Create these Data Layer Variables:

| GTM variable | Data layer variable name |
| --- | --- |
| `DLV - event_id` | `event_id` |
| `DLV - cta_type` | `cta_type` |
| `DLV - cta_text` | `cta_text` |
| `DLV - cta_url` | `cta_url` |
| `DLV - cta_section` | `cta_section` |
| `DLV - form_name` | `form_name` |
| `DLV - lead_type` | `lead_type` |
| `DLV - conversion_value` | `conversion_value` |
| `DLV - currency` | `currency` |

## Recommended GTM Triggers

Create exact-match Custom Event triggers:

| Trigger name | Event name |
| --- | --- |
| `CE - Sun Ray Lead Form Submit` | `sunray_lead_form_submit` |
| `CE - Sun Ray Call CTA Click` | `sunray_call_cta_click` |
| `CE - Sun Ray Text CTA Click` | `sunray_text_cta_click` |
| `CE - Sun Ray Quote CTA Click` | `sunray_quote_cta_click` |
| `CE - Sun Ray Quote Submit Click` | `sunray_quote_submit_click` |

Optional combined trigger with regex enabled:

```text
^sunray_(lead_form_submit|call_cta_click|text_cta_click|quote_cta_click|quote_submit_click)$
```

## Recommended GA4 Tags

Create a GA4 event tag for each reporting event:

| GTM trigger | GA4 event name | Priority |
| --- | --- | --- |
| `CE - Sun Ray Lead Form Submit` | `generate_lead` | Mark as GA4 key event |
| `CE - Sun Ray Call CTA Click` | `phone_call_click` | Mark as key event if calls are lead starts |
| `CE - Sun Ray Text CTA Click` | `text_message_click` | Mark as key event if texts are lead starts |
| `CE - Sun Ray Quote CTA Click` | `quote_cta_click` | Reporting only / optional key event |
| `CE - Sun Ray Quote Submit Click` | `quote_submit_click` | Reporting/debug only |

Add the same event parameters to each GA4 event tag when available:

- `event_id`
- `cta_type`
- `cta_text`
- `cta_url`
- `cta_section`
- `form_name`
- `lead_type`
- `value`
- `currency`

Use `{{DLV - conversion_value}}` for `value` and `{{DLV - currency}}` for `currency`.

## Recommended Google Ads Tags

Install one Conversion Linker tag in GTM and fire it on all pages.

Create Google Ads website conversion actions in Google Ads, then use **Tag setup > Use Google Tag Manager** to copy the Conversion ID and Conversion Label into GTM.

| Google Ads conversion action | GTM trigger | Optimization recommendation |
| --- | --- | --- |
| Quote form lead | `CE - Sun Ray Lead Form Submit` | Primary |
| Phone CTA click | `CE - Sun Ray Call CTA Click` | Primary if calls are real leads; otherwise Secondary |
| Text CTA click | `CE - Sun Ray Text CTA Click` | Primary if texts are real leads; otherwise Secondary |
| Quote CTA click | `CE - Sun Ray Quote CTA Click` | Secondary |

Use these Google Ads tag fields:

- Conversion ID: from Google Ads
- Conversion Label: from Google Ads
- Conversion Value: `{{DLV - conversion_value}}`
- Currency Code: `{{DLV - currency}}`
- Transaction ID: `{{DLV - event_id}}`

For lead conversions, set counting to **One** in Google Ads.

## GTM Preview QA

1. Run `npm run build:production`.
2. Serve `cloudflare-preview` locally or deploy a Cloudflare Pages preview.
3. Open GTM Preview and connect to the preview URL.
4. Test these actions:
   - Click Get a quote.
   - Click Call.
   - Click Text.
   - Submit a valid quote form and confirm the success state.
5. Confirm each event appears in the GTM event stream.
6. Confirm the intended GA4 and Google Ads tags fire once.
7. Confirm `sunray_quote_submit_click` fires on submit-button click, but `sunray_lead_form_submit` fires only after successful form API response.

## Account-Side Notes

Use GTM as the operational source of truth. GA4 can still mark `generate_lead`, `phone_call_click`, and `text_message_click` as key events for reporting, but Google Ads conversion firing should happen from GTM if the goal is one central tag-management surface.
