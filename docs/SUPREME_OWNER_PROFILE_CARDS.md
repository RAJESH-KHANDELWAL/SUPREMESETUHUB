# SUPREME Owner Profile Cards

The private SUPREME / SUPREME ECOSYSTEM owner dashboard renders the four registered identities through:

- `GET /api/v1/supreme-ecosystem/owner-admin/profiles` (owner authentication required)
- `frontend/supreme/supreme-ecosystem/index.html`
- `frontend/supreme/supreme-ecosystem/index.js`
- `frontend/supreme/supreme-ecosystem/index.css`

## Four profiles

1. `RAJESHKHANDELWAL` — `rajeshkhandelwal.com`
2. `RAJESHKHANDELWALOFFICIAL` — `rajeshkhandelwalofficial.com`
3. `DRRAJESHKHANDELWALIBC` — `drrajeshkhandelwalibc.com`
4. `DRRAJESHKHANDELWALIBCOFFICIAL` — `drrajeshkhandelwalibcofficial.com`

IDs labelled USER / BUSINESS / COMPANY / PROFILE / PAGE / CHANNEL / COMMUNITY / GROUP are SUPREME internal registry IDs, not verified external social-platform IDs.

## Actual profile and cover pictures

No actual profile or cover image files were present in the checked-in profile registry when these cards were added. The dashboard therefore uses styled placeholders and does not invent or scrape personal photos.

Set these optional environment variables on the backend deployment to show the real public HTTPS image URLs:

- `SUPREME_PROFILE_RAJESH_KHANDELWAL_AVATAR_URL`
- `SUPREME_PROFILE_RAJESH_KHANDELWAL_COVER_URL`
- `SUPREME_PROFILE_RAJESH_KHANDELWAL_OFFICIAL_AVATAR_URL`
- `SUPREME_PROFILE_RAJESH_KHANDELWAL_OFFICIAL_COVER_URL`
- `SUPREME_PROFILE_DR_RAJESH_KHANDELWAL_IBC_AVATAR_URL`
- `SUPREME_PROFILE_DR_RAJESH_KHANDELWAL_IBC_COVER_URL`
- `SUPREME_PROFILE_DR_RAJESH_KHANDELWAL_IBC_OFFICIAL_AVATAR_URL`
- `SUPREME_PROFILE_DR_RAJESH_KHANDELWAL_IBC_OFFICIAL_COVER_URL`

Use only images the owner is authorised to use. Keep these image URLs public-read if they need to render in the browser; do not place credentials or signed secrets in URLs. After changing environment variables, restart/redeploy the backend and refresh the owner dashboard.

The route is part of the existing private SUPREME ECOSYSTEM router and inherits its owner-authentication dependency. Do not expose it as a public profile listing endpoint.
