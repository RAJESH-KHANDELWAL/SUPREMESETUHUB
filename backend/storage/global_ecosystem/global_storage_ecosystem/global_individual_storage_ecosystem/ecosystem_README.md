# GLOBAL_INDIVIDUAL_STORAGE_ECOSYSTEM — Standard Category Foundation

This package follows the standardized category-foundation structure used by the Google Storage Ecosystem category packages while preserving the provider-neutral individual-storage identity and data boundary. It is not a live personal cloud drive.

## Canonical identity

- Ecosystem ID: `GLOBAL_INDIVIDUAL_STORAGE_ECOSYSTEM`
- Package: `global_individual_storage_ecosystem`
- Provider / owner: `GLOBAL_INDIVIDUAL`
- Category: `INDIVIDUAL`
- Category group: `PERSONAL_AND_INDIVIDUAL_STORAGE`
- Implementation state: `CATEGORY_FOUNDATION_SCAFFOLD`

## Standard modules

Configuration, manifest, metadata models, in-memory registry, validated ecosystem service, category adapter, framework-neutral API handlers, public model export, JSON schemas, taxonomy/index, offline tests and read-only PHP metadata contract are maintained as distinct package modules. The individual record schema remains domain-specific rather than being renamed to a generic provider-category record schema.

## Health and consistency checks

The ecosystem service checks canonical manifest identity and category placement; taxonomy/index identity, equality and counts; duplicate categories; foundation readiness; and the required safe integration flags. Health success means the local foundation contract is internally consistent only. It does not indicate a live external connection.

## Data ownership and security

Identity proofing/authentication, consent decisions, cryptographic keys and external provider operations belong to their respective services. This package stores minimized metadata and opaque references only. It must not store personal file content, credentials, authentication secrets or cryptographic keys.

## Readiness and operational boundary

Runtime enablement defaults to false. Connection remains `NOT_CONFIGURED`, provider product verification remains false and storage operations remain disabled. Authorized integration, live provider health checks and end-to-end tests are mandatory before enabling any external operation.
