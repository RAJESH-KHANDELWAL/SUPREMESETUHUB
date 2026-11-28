# Global Country-wise Referral Links

Canonical registry for user-supplied iDigitalPreneur referral URLs, organized by package and country.

## Rules
- Preserve complete URLs, including `promocode`, `countryId` and `expires`.
- An exact full-URL repeat is a duplicate and is stored once.
- A different country ID or expiry token is a distinct URL.
- Do not infer country names from country IDs without an authoritative mapping.
- Expiry tokens can expire; registry presence is not proof of current link validity.

## Premium Plus
See [premium_plus_referral_links.json](./premium_plus_referral_links.json).

## Shared Video Presentations
See [shared_video_links.json](./shared_video_links.json). Exact full-URL duplicates are stored once; a matching video ID with a different user ID remains a distinct referral URL. Link availability has not been independently verified.
