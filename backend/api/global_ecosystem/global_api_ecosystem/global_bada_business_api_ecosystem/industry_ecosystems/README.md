# Industry Ecosystems API

A read-only API over the curated India + Global industry taxonomy in `registry.py`.

## Mounted endpoints

- `GET /api/v1/global-ecosystem/business/industries/status`
- `GET /api/v1/global-ecosystem/business/industries`
- `GET /api/v1/global-ecosystem/business/industries/{industry_id}`

## Query parameters

- `channel`: `online`, `offline`, or `hybrid`
- `coverage`: `india` or `global`
- `q`: case-insensitive search over industry ID and name
- `include_adult`: opt-in visibility for the separately classified 18+ taxonomy. This is not age verification or authorization to access an adult service.

## Example

```http
GET /api/v1/global-ecosystem/business/industries?coverage=india&channel=online
```

## Scope and limitations

This API serves taxonomy metadata only. It does not claim that every business/provider is listed, nor does it connect to Google, Microsoft, AWS, Meta, OpenAI or other third-party systems. Those require separately documented provider adapters, credentials, permission checks, rate-limit handling and contract tests. Never store secrets in source control.

Adult-sector records require applicable-law review, age assurance, consent, privacy and safety controls before any provider integration or transaction flow is enabled.
