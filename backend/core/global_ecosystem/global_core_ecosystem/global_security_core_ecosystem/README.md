# GLOBAL SECURITY CORE ECOSYSTEM

A provider-neutral, read-only CORE control plane for security-domain taxonomy, provider capability metadata, governance boundaries and readiness discovery.

## Canonical architecture

- `ecosystem_manifest.json`: canonical identity, counts, boundaries and declared support areas
- `catalog.json` + `domain_catalog.py`: 18 non-exhaustive security-domain records
- `provider_catalog.json` + `provider_catalog.py`: 6 non-exhaustive provider metadata records
- `catalog.py`: canonical ecosystem registry and compatibility facade
- `contracts.py`: tenant-context, external secret-reference and result contracts
- `policy.py`: metadata redaction and capability classification; not an authorization engine
- `module_service.py`: provider-neutral, policy-aware metadata service
- `orchestrator.py`: provider/domain discovery, health and dependency summaries
- `service.py`: read-only public control-plane facade
- `shared_support/`: the 11 declared shared-support areas
- `integrations/`, `services/`, `tools/`: reserved, separately owned capability namespaces
- `<provider>_security_core_ecosystem/`: provider-specific manifests and metadata-only packages

## Provider inventory

Apple, AWS, Cloudflare, Google, IBM and Microsoft are represented as metadata-only provider packages. Registration does not imply an account, subscription, credential, API entitlement or live connection. Provider manifests must remain consistent with `provider_catalog.json`.

## Security boundaries

CORE metadata checks do not authenticate a person, prove authorization, enforce network controls, scan a workload, detect an incident or certify compliance. Tenant-context validation checks required fields only. Production authentication and authorization belong in independently tested identity/API layers; enforcement belongs in independently tested runtime and infrastructure layers. Store secret values only in an external secret manager; CORE must contain references at most, never secret values.

## Coverage and service tiers

The domain and provider taxonomies are intentionally non-exhaustive. Normal → Basic → Standard → Premium → Professional → Enterprise → Supreme describes governance/service tiers, not guaranteed protection or provider features.

## Validation

Run the focused integrity and contract suite from the repository root:

```bash
PYTHONPATH=. python -m pytest -q backend/core/global_ecosystem/global_core_ecosystem/global_security_core_ecosystem/tests
```

The suite checks manifest/catalog consistency, provider package manifests, canonical paths, shared-support directories, and declared security boundaries. Passing these tests validates repository metadata contracts only; it does not certify live security controls.
