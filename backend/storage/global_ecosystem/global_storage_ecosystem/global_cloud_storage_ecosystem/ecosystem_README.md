# GLOBAL CLOUD STORAGE ECOSYSTEM — FOUNDATION

## Package ownership
Storage owns canonical provider/service identity, metadata schemas, storage taxonomy, lifecycle definitions and health contracts. API/integration modules own external authentication and network operations. The central database owns durable operational persistence.

## Standard provider namespace
Each provider package contains its own manifest, config, metadata models, service contract, API boundary placeholder, model namespace, JSON schema, PHP metadata reader and offline tests. These files do not implement provider SDK calls.

## Safety and readiness
- Default connection state: `NOT_CONFIGURED`.
- External connectivity verification: `false`.
- Storage operations: disabled until a separate authorized integration is implemented and tested.
- Never store secrets or user file contents in this catalog.
- Do not infer availability or supported regions from a namespace existing in this repository.
