# Adobe Lightroom Storage

Catalog Lightroom cloud photo/video assets, albums, metadata and synchronization state. Storage quota, asset access and supported workflows depend on the Lightroom plan and documented product interfaces.

## Integration boundary

This folder owns storage-side catalog and lifecycle metadata only. Adobe API clients, OAuth, scopes, endpoints and API operations are owned by `backend/api/global_ecosystem/global_api_ecosystem/adobe_api_ecosystem/`. This ecosystem remains `NOT_CONFIGURED` until product entitlement, authorization, live health checks and required operations are verified.
