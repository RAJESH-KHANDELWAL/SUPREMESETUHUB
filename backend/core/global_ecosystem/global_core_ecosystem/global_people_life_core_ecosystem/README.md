# GLOBAL PEOPLE LIFE CORE ECOSYSTEM

A dedicated, read-only CORE control plane for global people, family, relationships, work, education, wellbeing, digital public services and lawful adult-only service metadata. It is a direct sibling of the other Global CORE ecosystems under `global_core_ecosystem/`.

## Architecture
- `catalog.py`: canonical ecosystem registry and compatibility facade
- `domain_catalog.py` + `catalog.json`: canonical 28-domain taxonomy
- `contracts.py`: typed tenant, domain, secret-reference and result contracts
- `policy.py`: tenant authorization boundary, sensitive metadata redaction and adult-domain safeguards
- `module_service.py`: reusable policy-aware domain metadata service
- `orchestrator.py`: domain discovery and health summaries
- `service.py`: public read-only control-plane service
- `shared_support/`: cross-cutting support conventions

## Scope and safety
The catalog organizes metadata; it does not provide clinical, legal, financial or crisis-care advice, verify identity or age, establish consent, or prove regulatory compliance. Application workflows must use qualified services and independent lawful controls where required.

Adult-only domains are restricted to lawful consenting verified adults. Application layers must implement reliable age assurance, informed consent, rights/licensing checks, jurisdictional review, privacy protections, moderation and takedown. Prohibited categories include sexual content involving minors, non-consensual intimate imagery, coercion, trafficking and exploitation.

## Service tiers
Normal → Basic → Standard → Premium → Professional → Enterprise → Supreme. Tiers describe service/governance levels, not guaranteed features, entitlements or live integrations.

## Layer boundary
CORE owns taxonomy, metadata, capability policy and readiness. API, storage, database, runtime and application layers own transport, persistence, execution and user workflows. A CORE capability check is not permission to perform a regulated or sensitive operation.
