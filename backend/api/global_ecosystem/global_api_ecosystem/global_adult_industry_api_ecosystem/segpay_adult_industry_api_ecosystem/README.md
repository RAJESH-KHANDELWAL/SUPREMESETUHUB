# SEGPAY SPECIALIST PAYMENT ECOSYSTEM — ADULT_INDUSTRY API Ecosystem

- Provider ID: `segpay`
- Category: `ADULT_INDUSTRY`
- Provider-owned catalog: `backend/api/global_ecosystem/global_api_ecosystem/global_ai_api_ecosystem/segpay_adult_industry_ecosystem`
- Shared category catalog: `backend/api/global_ecosystem/global_api_ecosystem/global_adult_industry_api_ecosystem`
- Status: `CATALOG_ONLY`
- Official API documentation verified: `False`
- Live connection verified: `False`

## Purpose

This folder indexes the provider under the shared ADULT_INDUSTRY category so the ecosystem can follow a consistent provider/category layout. The mapping comes from the central provider catalog; it does **not** prove that the provider offers a public API or that an adapter is implemented.

## Integration gate

1. Verify the provider's official product and API documentation and current terms.
2. Confirm the API actually supports this category and the required account/region access.
3. Implement a provider-specific adapter only for supported operations.
4. Keep credentials in environment variables or a managed secret store; never commit secrets.
5. Add mocked unit tests and authenticated integration tests before marking any connection live.

Do not infer capabilities, create fake endpoints, or mark this folder live-connected based on catalog presence alone.
