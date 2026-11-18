# INDIVIDUAL CLOUD STORAGE

**Parent:** GLOBAL INDIVIDUAL CORE ECOSYSTEM  
**Layer:** CORE  
**Domain:** `CLOUD_STORAGE`

## Scope
Cloud-storage provider inventory, capabilities and retention metadata.

## Core responsibilities
- Maintain canonical capability metadata and lifecycle/readiness state.
- Define provider-neutral contracts and policy classifications.
- Expose read-only discovery through the parent Individual Core registry.
- Delegate provider authentication, API transport, persistence and execution to their owning layers.

## Privacy and safety boundaries
- Enforce tenant isolation and least privilege in the application layer.
- Minimize personal data; keep credentials and direct identifiers out of Core metadata.
- Apply explicit consent, age and jurisdiction safeguards wherever legally required.
- Do not claim provider connectivity, compliance or verification without tested evidence.

## Status
`CORE_CATALOG_ONLY`. Parent catalog registration does not mean a dedicated live adapter exists.
