# Adobe Storage Ecosystem

Canonical storage subtree under Adobe / What Adobe Provides.

This package organizes Adobe products that may manage, store, deliver or collaborate on digital assets. The presence of a product here does not imply a universal Adobe storage API.

## Product storage packages
- Creative Cloud Assets
- Creative Cloud
- Cloud Storage and Collaboration
- Document Cloud
- Experience Manager Assets
- Express
- Frame.io
- Lightroom
- Workfront

## Implementation rules
1. Confirm an official API exists for the exact product and operation.
2. Confirm the Adobe organization has the required product entitlement, OAuth scopes and permissions.
3. Use the shared Adobe API/integration layer for authentication and HTTP transport.
4. Keep each product adapter isolated and map provider responses to shared storage models.
5. Test metadata listing, object retrieval, upload/download and delete only where the product API documents them.
6. Do not label a provider CONNECTED until a real authenticated operation passes.

Current package status: foundation/catalog scaffold only. The child adapter contracts and metadata registries are not live Adobe connectors. No credentials or live API calls are included.
