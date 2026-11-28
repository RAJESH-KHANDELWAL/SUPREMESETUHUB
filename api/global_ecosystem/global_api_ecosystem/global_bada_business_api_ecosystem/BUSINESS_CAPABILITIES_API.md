# Bada Business API Capability Contracts

All routes below are mounted under `/api/v1/global-ecosystem/business`.

## Connected module inventory
- `GET /capabilities/architecture/modules` — enumerates the routes actually registered in this Bada Business router and records the ownership boundaries for Company/Companies, Platforms and Organizations.
- `GET /governance/approved-requirements` — returns only explicitly confirmed user decisions.
- `GET /governance/scope-constraints` — exposes the folder ownership and implementation constraints.

## Business lifecycle
- `GET /capabilities/lifecycle` — ordered lifecycle taxonomy from Idea through Closure.

## Trust and safety
- `GET /capabilities/trust-safety` — identity, registration/licence, employer/job, product/service, fraud/scam and misinformation control definitions.
- These are framework definitions, not operational identity verification, fraud detection or moderation.

## Jurisdictional compliance
- `GET /capabilities/compliance/framework` — required legal-obligation record fields and validation rules.
- No country dataset is claimed as ingested or verified. Each legal record must cite an official authority, jurisdiction, business activity, effective dates and last verification evidence. Local legal review remains necessary where rules are ambiguous.

## Business Intelligence and API analytics
- `GET /capabilities/business-intelligence` — event contract, analytics capability inventory and privacy controls.
- This does not claim a live analytics database or live metrics. Analytics ownership for other ecosystems remains in their respective folders.

## Capability integrity
- `GET /capabilities/integrity` — validates the static capability contracts.

## Scope boundaries
- This implementation is Bada Business API only; no separate platform is created here.
- AI and automation implementation is excluded from this folder.
- Education and learning APIs remain in Bada Business.
- Banking and payment APIs remain in their separately owned API folders and may be connected only through authorised APIs.
- Company/Companies, Platforms and Organizations remain separate ecosystems; this change does not modify their folders.
- External provider catalogue entries are not live connections. A connection is live only after official API access, credentials, terms, environment configuration and integration tests are verified.
