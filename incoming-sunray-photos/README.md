# Incoming Sun Ray Photos

Place only customer-approved job photos in this folder. Every photo batch must include a `photo-intake.json` copied from `photo-intake.example.json`.

The importer no longer assigns a city, service, consent status, or approval status from a filename. Those facts must be verified in the manifest before a photo can enter the public gallery.

## Required workflow

1. Copy approved images into this folder or a batch subfolder.
2. Copy `photo-intake.example.json` to `photo-intake.json`.
3. Add one manifest record for every image.
4. Confirm customer consent, the broad city/county, service type, and privacy review.
5. Run `npm run photos:validate`.
6. Review the generated records with `npm run photos:dry-run`.
7. Run `npm run import:local-gallery` only after validation passes.

## Privacy rules

Do not upload family photos, client names, exact addresses, mail, documents, keys, door or access codes, license plates, security panels, or identifiable exterior views. The public record stores only city-or-county-level location information.

The importer converts approved images to optimized JPEG files and strips source EXIF metadata during conversion. Imported social copy remains in `draft` status until it is posted manually.
