# GLOBAL INDIVIDUAL CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Canonical root:** `backend/core/global_ecosystem/global_core_ecosystem/global_individual_core_ecosystem/`  
**Master source:** `backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json`

## Mission

A read-only Core control plane for individual identity, access, services, education, skills, work, communication, personal resources, privacy, safety and lawful adult-only service metadata. Its architecture follows the separation used by `google_core_ecosystem/`: catalog, domain taxonomy, contracts, policy, reusable module service, orchestrator, service facade and manager.

## Master-catalog mapping

Reads Section 2, `human_individual_ecosystem`, directly from the canonical 2468-target master catalogue. That section currently defines 20 entries. The full catalogue currently has 246 unique entries, target 2468, remaining 2222. The target is not current coverage; this Core never manufactures entries or edits the master file.

## Architecture

- `catalog.py`: module inventory and lookup.
- `master_catalog.py`: read-only master JSON loader.
- `domain_catalog.py`: source taxonomy mapping and coverage summary.
- `contracts.py`, `models.py`: typed context and metadata contracts.
- `policy.py`: metadata redaction and adult-safety boundaries.
- `module_service.py`: reusable module metadata service.
- `orchestrator.py`: discovery, health and domain mapping.
- `service.py`: public status facade.
- `manager.py`: stable entry point; `registry.py`: unique module lookup.
- `manager.php`: PHP metadata facade; `ecosystem_manifest.json`: machine-readable scope.
- `tests/`: structural, mapping, safety and import tests.

## Layer ownership

CORE owns identity references, taxonomy, capability metadata, policy and readiness only. API owns authentication, consent flows, SDK clients and transport. Storage/Database own durable records, encryption, retention and migrations. Runtime/Engine owns jobs and execution. Application/UI owns user sessions and workflows. Secrets remain in an external secret manager; Core stores no credentials or raw identity documents.

## Safety and privacy

Apply data minimization, purpose limitation, retention limits, access logging and applicable regional law. Adult-only modules cover lawful consenting adults only. Minors, exploitation, trafficking, coercion and non-consensual intimate imagery are prohibited. Age assurance, informed consent, rights verification, moderation, reporting and takedown controls are mandatory.

## Completeness and runtime claims

The 29 modules are an extensible taxonomy, not an exhaustive census of individual services. Registration is not proof of authorization, eligibility, API availability or live connectivity. API calls from Core are zero, persistence is disabled and modules remain `CORE_CATALOG_ONLY` until separately implemented and tested.
