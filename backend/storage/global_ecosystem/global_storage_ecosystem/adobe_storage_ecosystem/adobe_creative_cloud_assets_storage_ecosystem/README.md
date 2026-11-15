# Adobe Creative Cloud Assets Storage

Catalog reusable creative assets and asset references exposed through documented Creative Cloud/Assets capabilities. Keep metadata, ownership, sharing, asset versions and binary-object access separate. API operations and OAuth remain in Adobe API Ecosystem.

## Integration boundary

This folder owns storage-side catalog and lifecycle metadata only. Adobe API clients, OAuth, scopes, endpoints and API operations are owned by `backend/api/global_ecosystem/global_api_ecosystem/adobe_api_ecosystem/`. This ecosystem remains `NOT_CONFIGURED` until product entitlement, authorization, live health checks and required operations are verified.
