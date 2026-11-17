# GLOBAL SECURITY CORE ECOSYSTEM

A provider-neutral, read-only CORE control plane for security-domain taxonomy, provider capability metadata, governance boundaries and readiness discovery.

## Architecture
- `catalog.py`: canonical ecosystem registry and compatibility facade
- `catalog.json` + `domain_catalog.py`: security-domain taxonomy
- `provider_catalog.json` + `provider_catalog.py`: provider inventory and capability metadata
- `contracts.py`: typed tenant, secret-reference, result and readiness contracts
- `policy.py`: least-privilege, tenant-context, sensitive-metadata and capability guardrails
- `module_service.py`: provider-neutral, policy-aware metadata service
- `orchestrator.py`: provider/domain discovery, health and dependency summaries
- `service.py`: read-only public control-plane facade
- `integrations/`, `services/`, `tools/`: reserved, separately owned capability namespaces

## Providers
Apple, AWS, Cloudflare, Google, IBM and Microsoft are represented as metadata-only provider packages. Registration does not imply an account, subscription, credential, API entitlement or live connection.

## Security boundaries
CORE metadata checks do not authenticate a person, prove authorization, enforce network controls, scan a workload, detect an incident or certify compliance. Production enforcement belongs in independently tested API, identity, runtime, infrastructure and application layers. Store secrets only in an external secret manager; this catalog must never contain secret values.

## Coverage and tiers
The taxonomy is intentionally non-exhaustive. Normal → Basic → Standard → Premium → Professional → Enterprise → Supreme describes governance/service tiers, not guaranteed protection or provider features.
