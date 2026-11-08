# BADA BUSINESS ECOSYSTEM

Canonical product/platform ecosystem root:

backend/bada_business_ecosystem/

## Main package structure

- global_bada_business_ecosystem/ — Bada Business ecosystem domain package
- api_ecosystem/ — stable API ecosystem entry point
- platform/, links/, programs/, courses/, products/, events/, registration/, referrals/ — product-specific modules

## API boundary

The broader API source remains implemented under backend/api/global_ecosystem/global_api_ecosystem/global_bada_business_api_ecosystem/ to preserve existing FastAPI imports and route registrations. The global_bada_business_ecosystem/api_ecosystem module exposes it. This API source tree has not yet been physically relocated.

## Platform resources

The canonical platform links and program snapshots are maintained under global_bada_business_ecosystem/platform_resources/. Old backend/bada_business/... resource paths are compatibility facades only.
