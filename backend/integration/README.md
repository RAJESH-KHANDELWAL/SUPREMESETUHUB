# Bada Business integration

SUPREMESETUHUB currently provides a **catalog-only Bada Business integration**. It is a real, locally executable integration of the repository's canonical Bada Business resource data; it is not a live connection to a Bada Business account or an undocumented provider API.

## Canonical data ownership

- Ecosystem package: `backend/global_ecosystem/global_bada_business_ecosystem/`
- Canonical destination links: `backend/global_ecosystem/global_bada_business_ecosystem/links/platform_links.py`
- Program snapshots: `backend/global_ecosystem/global_bada_business_ecosystem/platform_resources/programs/`
- Canonical catalog: `backend/global_ecosystem/global_bada_business_ecosystem/platform_resources/catalog.py`

The catalog currently exposes 9 destination links and 3 program records. These counts describe repository data, not current provider availability or purchasable offers.

## Integration architecture

- Provider adapter: `backend/integration/provider/bada_business.py`
- Connector adapter: `backend/integration/connector/bada_business.py`
- Connector registry: `backend/integration/connector/registry.py`
- Provider registry: `backend/integration/registry.py`
- FastAPI routes: `backend/api/bada_business_integration.py`
- Tests: `backend/tests/test_bada_business_integration.py`

## API routes

All routes are mounted in the FastAPI application and follow the application's owner-authentication policy:

| Method | Route | Purpose |
|---|---|---|
| GET | `/api/v1/bada-business-integration/status` | Catalog readiness and connection boundary |
| GET | `/api/v1/bada-business-integration/catalog` | Full canonical catalog |
| GET | `/api/v1/bada-business-integration/links` | List links; optional `?q=` text search |
| GET | `/api/v1/bada-business-integration/links/{link_id}` | Link lookup |
| GET | `/api/v1/bada-business-integration/programs` | List programs; optional `?q=` search |
| GET | `/api/v1/bada-business-integration/programs/{program_id}` | Program lookup |

## Capability boundary

- Catalog reads, link lookup, program lookup, and local search: implemented.
- Provider authentication: not configured.
- Official public developer API: not verified.
- Live provider connection: not connected.
- Purchase, enrollment, payment, lead submission, and provider account actions: not implemented.

Do not interpret `CATALOG_ONLY` as `CONNECTED`. No undocumented endpoints or provider credentials are used.
