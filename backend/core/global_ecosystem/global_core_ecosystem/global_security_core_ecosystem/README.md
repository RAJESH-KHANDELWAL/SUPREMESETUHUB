# GLOBAL SECURITY CORE ECOSYSTEM

A provider-neutral, read-only CORE control plane for security-domain taxonomy, provider capability metadata, jurisdictional governance boundaries and readiness discovery.

## Canonical architecture

- `ecosystem_manifest.json`: canonical identity, counts, boundaries, jurisdictional coverage and declared support areas
- `catalog.json` + `domain_catalog.py`: 33 non-exhaustive security-domain records, each mapped to a direct-child CORE ecosystem package
- `<domain>_core_ecosystem/`: each domain is a direct child of this ecosystem root, with `__init__.py`, `domain_manifest.json` and a domain-specific README; there is no intermediate `domains/` folder
- `provider_catalog.json` + `provider_catalog.py`: 6 non-exhaustive provider metadata records
- `catalog.py`: canonical ecosystem registry and compatibility facade
- `jurisdiction_catalog.py`: validated India and cross-border jurisdiction profile registry
- `contracts.py`: tenant-context, external secret-reference and result contracts
- `policy.py`: metadata redaction and capability classification; not an authorization engine
- `content_safety_policy.py`: protective adult-platform, age-assurance, consent and prohibited-content metadata guardrails only
- `domain_catalog.py`: validates every registered domain package and its manifest at catalog load
- `module_service.py`: provider-neutral, policy-aware metadata service
- `orchestrator.py`: provider/domain discovery, health and dependency summaries
- `service.py`: read-only public control-plane facade
- `jurisdictions/india/` and `jurisdictions/global/`: jurisdictional control mappings and profiles; legal registers require authoritative, dated source review
- `shared_support/`: the 11 declared shared-support areas
- `integrations/`, `services/`, `tools/`: separately owned capability namespaces
- `<provider>_security_core_ecosystem/`: provider-specific manifests and metadata-only packages

## Domain coverage

The 33 domain records cover identity, zero trust, endpoints, networks, cloud, applications, data privacy, cryptography, threat intelligence, incident response, vulnerabilities, GRC, resilience, supply chain, collaboration, awareness, fraud, physical/IoT/OT, age assurance, child safety, lawful adult-platform safeguards, consent and intimate-image protection, exploitation and trafficking prevention, sensitive intimate-data privacy, sexual-health information integrity, content moderation, synthetic-media abuse, jurisdictional compliance, digital wellbeing, identity impersonation, payment security, platform trust and safety, and research/evidence assurance.

Coverage is intentionally non-exhaustive. New domains must receive a unique ID, a direct-child folder ending in `_core_ecosystem`, a manifest and a documented owner before registration.

## Adult, sexual-content and Kamasutra-related boundary

This is a **security and protection ecosystem**, not an adult-content library. It covers age assurance, lawful age-restricted access, consent, privacy, exploitation prevention, non-consensual intimate-image reporting/takedown, child safety and platform trust. Kamasutra or sexual-health educational material may be governed by a separate lawful education/knowledge ecosystem; this CORE only defines protective controls around access, privacy and safety. It does not store, generate or distribute pornography or explicit sexual media. Child sexual-abuse material and non-consensual intimate imagery are prohibited and must never be stored or reproduced.

## Jurisdictional coverage

- India profile: map applicable Indian laws, regulators, reporting channels and data-protection obligations with source, effective date and review status.
- Global profile: map international standards and country/region-specific requirements without assuming one law applies worldwide.
- Country coverage is non-exhaustive. Legal mappings require qualified review and dated authoritative sources; this catalog is not legal advice.

## Provider inventory

Apple, AWS, Cloudflare, Google, IBM and Microsoft are represented as metadata-only provider packages. Registration does not imply an account, subscription, credential, API entitlement or live connection.

## Security boundaries

CORE metadata checks do not authenticate a person, prove authorization, enforce network controls, scan a workload, detect an incident or certify compliance. Tenant-context validation checks required fields only. Production authentication and authorization belong in independently tested identity/API layers; enforcement belongs in independently tested runtime and infrastructure layers. Store secret values only in an external secret manager; CORE must contain references at most, never secret values.

## Technology boundaries

This CORE package is Python-based. PHP belongs in separately deployed PHP application/API or WordPress integration packages when required; do not add PHP files to this Python metadata layer merely for symmetry. API, storage, database, runtime and application implementations must remain separately owned and tested.

## Coverage and service tiers

Normal → Basic → Standard → Premium → Professional → Enterprise → Supreme describes governance/service tiers, not guaranteed protection or provider features.

## Validation

Run the focused integrity and contract suite from the repository root:

```bash
PYTHONPATH=. python -m pytest -q backend/core/global_ecosystem/global_core_ecosystem/global_security_core_ecosystem/tests
```

Passing these tests validates repository metadata contracts only; it does not certify live security controls or legal compliance.
