# GLOBAL INDIVIDUAL CORE ECOSYSTEM

**Layer:** CORE  
**Parent:** GLOBAL CORE ECOSYSTEM  
**ID:** `GLOBAL-INDIVIDUAL-CORE-ECOSYSTEM`

## Mission
Canonical, provider-neutral control plane for individual-facing capabilities. Owns capability identity, taxonomy, metadata contracts, Core policy classification, discovery and readiness. Does not own end-user sessions, personal records, credentials, provider API transport, payments execution, clinical decisions or content delivery.

## Inventory
29 registered capability packages, each with a dedicated scope document. Registration is metadata only and does not imply an adapter, entitlement, lawful availability or live connection.

## Layer ownership
| Layer | Responsibility |
|---|---|
| Individual Core | Catalog, taxonomy, contracts, policy metadata and orchestration |
| API / Integrations | Provider authentication, consented API access, secrets, transport and normalization |
| Engine | Workflow execution |
| Database | Authorized persistence, schemas and retention |
| Storage | Encrypted files and user-controlled artifacts |
| Application | User-facing consent, access controls and workflows |

## Security
- Tenant and actor identity must originate from authenticated application context.
- Apply data minimization, purpose limitation and retention limits.
- Keep credentials, tokens, government identifiers, medical records and financial account details out of Core metadata.
- Sensitive workflows require explicit authorization, applicable consent, age/jurisdiction checks and audit.
- Age-restricted capabilities must remain unavailable until lawful age assurance and regional eligibility are established.
- Consent must be specific, informed, affirmative, revocable and recorded by the owning application.
- Core policy classification is not a substitute for application authorization or legal compliance.

## Status
`CORE_CATALOG_ONLY`; `api_available: null`; `live_connection_verified: false`; `api_calls_performed: 0`.

## Modules
`catalog.py` registry; `contracts.py` tenant/result contracts; `policy.py` sensitivity and metadata filtering; `service.py` read-only facade; `orchestrator.py` discovery and health; `ecosystem_manifest.json` machine-readable status.

## Child package convention
Each child should grow independently with README, catalog, contracts, policy, service, orchestrator, integrations and tests as warranted. Do not duplicate provider transport or user data in Core.
