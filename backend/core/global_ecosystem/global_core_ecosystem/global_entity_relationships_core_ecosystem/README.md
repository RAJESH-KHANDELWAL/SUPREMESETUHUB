# GLOBAL ENTITY RELATIONSHIPS CORE ECOSYSTEM

A read-only CORE control plane for entity identity references, relationship taxonomy, evidence provenance, verification-state metadata, and relationship-policy validation.

## Architecture

- `catalog.py`: canonical root, 36 category taxonomy and relationship-type metadata.
- `registry.py`: deterministic in-memory category registry and lookup.
- `models.py`: typed relationship metadata contract.
- `policy.py`: required fields, relationship type, status, self-edge and evidence URL validation.
- `manager.py`: stable public entry point, health/status, category inventory, tree, dependency map, policy validation and 2468 master-catalog reference.
- `service.py`: application-facing read-only facade.
- `orchestrator.py`: catalog discovery and health coordination.
- `tests/` and `test_global_entity_relationships_core.py`: contract and behavior coverage.

## Master catalog alignment

The backend master catalog reference is `backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json` (`GLOBAL_TO_SUPREME_MASTER_ECOSYSTEM`), with the documented target of 2,468 unique entries. Its current count and remaining count are exposed as reference metadata only. This CORE does not copy, fabricate, or mutate the master catalog.

## Scope and boundary

CORE manages metadata taxonomy and validation only. It does not store relationship records, call provider APIs, authenticate, perform background jobs, or confirm real-world ownership, affiliation, consent, licensing, employment, or relationship claims. Evidence URLs and a `VERIFIED` state are input metadata; validation is not independent verification.

## Sensitive relationship domains

Sensitive categories require data minimization, lawful purpose, access control, consent where applicable, age-appropriate safeguards, and safety review. No private or sensitive relationship claim should be inferred from catalog membership.

## Service tiers

Normal, Standard, Advanced, Enterprise and Supreme are classification/governance labels only. They do not imply deployed integrations, access entitlement, verification, or service guarantees.
