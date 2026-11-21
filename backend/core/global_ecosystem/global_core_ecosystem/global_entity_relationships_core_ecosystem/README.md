# GLOBAL ENTITY RELATIONSHIPS CORE ECOSYSTEM

A read-only CORE control plane for entity identity references, relationship taxonomy, evidence provenance, verification-state metadata, and relationship-policy validation.

## Architecture
- `catalog.py`: canonical root, 36 category taxonomy and relationship-type metadata.
- `registry.py`: deterministic in-memory category registry and lookup.
- `models.py`: typed relationship metadata contract.
- `policy.py`: required fields, relationship type, status, self-edge and evidence URL validation.
- `manager.py`: stable public entry point, health/status, category inventory, tree, dependency map, policy validation and master-catalog reference.
- `service.py`: application-facing read-only facade.
- `orchestrator.py`: discovery and health coordination.
- `tests/` and `test_global_entity_relationships_core.py`: contract and behavior coverage.

## Master catalog alignment
Reference: `backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json` (`GLOBAL_TO_SUPREME_MASTER_ECOSYSTEM`), target 2,468 unique entries. The master catalog is referenced only. CORE does not copy, fabricate, or mutate its entries.

## Scope and boundary
CORE manages metadata taxonomy and validation only. It does not store relationship records, call provider APIs, authenticate, perform background jobs, or confirm real-world ownership, affiliation, consent, licensing, employment, or relationship claims. Evidence URLs and a `VERIFIED` state are supplied metadata; validation is not independent verification.

## Sensitive relationship domains
Use data minimization, lawful purpose, access controls, consent where applicable, age-appropriate safeguards, and safety review. Do not infer private or sensitive claims from catalog membership.

## Service tiers
Normal, Standard, Advanced, Enterprise and Supreme are classification/governance labels only; they do not imply integrations, access entitlement, verification, or service guarantees.
