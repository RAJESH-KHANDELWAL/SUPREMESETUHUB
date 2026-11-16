# Cohere Classify Core Ecosystem

**Provider:** Cohere  
**Layer:** CORE  
**Capability:** `classify`  
**Status:** `interface_only`

## Responsibility
Owns capability identity, typed request contracts, validation, metadata, lifecycle vocabulary, security policy and CORE service interface. Does not own HTTP transport, SDK execution, retries, database/storage persistence or UI.

## Standard product-package layout
`authentication/`, `capabilities/`, `docs/`, `events/`, `lifecycle/`, `models/`, `schemas/`, `security/`, `services/`, `tests/`, plus `contracts.py`, `service.py`, `ecosystem_config.py` and `ecosystem_manifest.json`.

Live Cohere operations remain disabled until approved API/ENGINE adapters, secure credentials, model configuration and integration tests are in place.
