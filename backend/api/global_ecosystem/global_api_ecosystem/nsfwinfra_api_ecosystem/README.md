# NSFWINFRA API ECOSYSTEM

Canonical provider-owned API ecosystem for NSFWInfra in SUPREMESETUHUB.

NSFWInfra describes itself as adult AI infrastructure for developers. Its API provides image and video generation/editing capabilities through asynchronous jobs. This ecosystem is explicitly classified as **adult-content infrastructure** and must remain behind age, jurisdiction, consent, and safety controls.

## Provider details

- Provider ID: `nsfwinfra`
- API base URL: `https://api.nsfwinfra.com`
- API version: `v1`
- Authentication: `Authorization: Bearer <API_KEY>`
- Server-side secret: `NSFWINFRA_API_KEY`
- Current project runtime adapter: `backend/engine/ai/manager.py`
- Infrastructure client: `backend/infrastructure/nsfwinfra.py`
- Live customer connection: **not verified**

## Documented service families

| Family | API route / area | Current project status |
|---|---|---|
| Image generation | `POST /v1/images/generate` | Runtime adapter present; account unverified |
| Image editing | `POST /v1/images/edit` | Documented; adapter not implemented |
| Anime generation | `POST /v1/anime/generate` | Documented; adapter not implemented |
| Text to video | `POST /v1/text-to-video` | Documented; adapter not implemented |
| Image to video | `POST /v1/image-to-video` | Documented; adapter not implemented |
| Image/video effects | `POST /v1/effects/{effect_id}` | Documented; adapter not implemented |
| Async jobs | `GET /v1/jobs/{job_id}` | Required for result polling; not yet integrated end-to-end |
| Webhooks | Dashboard webhook configuration | Signature verification not yet integrated |
| Signed uploads | `POST /v1/uploads` | Documented; adapter not implemented |
| Account and limits | `GET /v1/account`, `GET /v1/models` | Documented; connection verifier not implemented |

All generation endpoints are asynchronous in the provider documentation: create requests return `202 Accepted` with a job ID, then the client polls the job or receives a signed webhook. Do not treat the initial 202 response as a completed image/video result.

## Setup

1. Create an NSFWInfra account and generate a test API key in its dashboard.
2. Add the key to the backend secret manager or deployment environment as `NSFWINFRA_API_KEY`.
3. Never commit the key, place it in frontend JavaScript, or return it in API responses.
4. Use a test key and a small, permitted request before enabling production usage.
5. Configure per-key spending limits and monitor balance and usage.

No API key is included in this repository.

## Adult-content safety requirements

- Restrict access to adults aged 18 or older and verify applicable local-law eligibility.
- Block any sexual content involving minors, age-ambiguous subjects, or youthful depictions.
- Block non-consensual intimate imagery, sexual deepfakes, coercion, and abuse.
- Require the submitter to have lawful rights and consent for every uploaded source image.
- Provide reporting, moderation, audit logging, and account-level suspension controls.
- Do not enable this provider for child-facing products or general users without an explicit adult-only gate.

## Implementation status

The repository currently has an image-generation handler registered in the central AI engine and an async infrastructure helper. The broader service families above are documentation/catalog coverage only. There is no verified live customer credential in this repository, no complete async job lifecycle, no webhook signature verifier, and no production account test recorded.

## Official documentation

- Quickstart: https://nsfwinfra.com/docs
- Authentication: https://nsfwinfra.com/docs/authentication
- API keys and account: https://nsfwinfra.com/docs/api-keys
- Models: https://nsfwinfra.com/docs/models
- Products: https://nsfwinfra.com/products
- Terms: https://nsfwinfra.com/legal/terms

Always re-check the provider's current documentation, account entitlements, pricing, legal terms, and acceptable-use policy before production deployment.
