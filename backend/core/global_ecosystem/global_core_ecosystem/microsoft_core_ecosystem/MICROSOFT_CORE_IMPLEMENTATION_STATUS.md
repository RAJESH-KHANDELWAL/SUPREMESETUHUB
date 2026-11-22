# Microsoft Core Implementation Status

## Main-branch reconciliation
- The 16 Microsoft product-family directories already exist and are preserved.
- The provider-level Core registry and manager are added at this package root.
- The existing Microsoft API ecosystem remains the transport/adaptor ownership layer.
- No provider-specific database, credentials, OAuth client, API transport, or runtime is created here.

## Registered scope
- 16 existing product families.
- 19 classification domains.
- Canonical Python entry point: `manager.py:get_manager()`.
- PHP facade is metadata interoperability only.

## Operational truth
This package is a metadata/control-plane registry. Product registration does not prove licensing, provisioning, tenant authorization, deployment, API availability, or live connectivity. The implementation reports zero verified live connections and zero API calls. Tests must execute in CI before merge.
