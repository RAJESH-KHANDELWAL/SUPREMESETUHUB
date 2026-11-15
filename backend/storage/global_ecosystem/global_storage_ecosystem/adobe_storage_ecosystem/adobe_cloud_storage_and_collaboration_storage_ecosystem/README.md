# Adobe Cloud Storage and Collaboration

Catalog Adobe cloud projects, folders, files, cloud documents, Creative Cloud Libraries and brands where the subscribed product exposes them. Preserve provider-native IDs, ownership, permissions, version references and lifecycle metadata. The Adobe Cloud Drive desktop mount/sync client is an access surface, not a separate storage backend. Do not assume a universal Adobe Drive API.

## Integration boundary

This folder owns storage-side catalog and lifecycle metadata only. Adobe API clients, OAuth, scopes, endpoints and API operations are owned by `backend/api/global_ecosystem/global_api_ecosystem/adobe_api_ecosystem/`. This ecosystem remains `NOT_CONFIGURED` until product entitlement, authorization, live health checks and required operations are verified.
