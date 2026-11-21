# GLOBAL VASUDHAIVA KUTUMBAKAM | SANATAN DHARMA | BHARAT SANSKRITI | WORLD CULTURE CORE ECOSYSTEM

**Parent:** `GLOBAL-CORE-ECOSYSTEM`  
**Root:** `backend/core/global_ecosystem/global_core_ecosystem/global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_core_ecosystem/`  
**Reference architecture:** `google_core_ecosystem/`  
**Master taxonomy reference:** `backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json`

## Mission and ownership

This Core layer is the read-only control plane for cultural domain identity, discovery, knowledge-resource metadata, evidence assessment, provenance, consent and publication-readiness boundaries. It preserves four distinct pillars: Vasudhaiva Kutumbakam, Sanatan Dharma, Bharat Sanskriti and World Culture.

The authoritative cultural knowledge source remains `backend/global_ecosystem/global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_ecosystem/`. The API domain remains under `backend/api/global_ecosystem/global_api_ecosystem/global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_api_ecosystem/`. The related business expression remains separate in the Bada Business ecosystem. Core references these layers and does not duplicate their implementations.

## Architecture and responsibilities

- `catalog.py`: canonical ecosystem identity, pillars, capabilities and child-domain metadata.
- `domain_catalog.py`: the 13 registered domain definitions and their source/API references.
- `domain_runtime.py`: shared read-only runtime reused by registered domain packages.
- `resource_catalog.py` and `resource_ecosystem_index.json`: source-backed knowledge discovery and domain-family metadata; unverified resource totals remain null.
- `contracts.py`: tenant and result contracts.
- `governance.py` and `policy.py`: record validation, evidence, consent, rights and access safeguards.
- `module_service.py`: reusable domain facade.
- `orchestrator.py`: domain discovery, inventory, offering lookup, health and dependency metadata.
- `service.py`: public service, registry status and backward-compatible `get_manager()` factory.
- `manager.py`: canonical Python entry point aligned with Google Core manager conventions.
- `manager.php`: PHP result-normalization facade; Python remains the canonical orchestrator.
- Domain packages reuse the shared runtime; domain-specific business logic is not copied into each package.

## Canonical domain coverage

1. Sanatan Dharma
2. Bharat Sanskriti
3. Bharat Civilization
4. World Cultures
5. World Civilizations
6. Languages and Literature
7. Heritage and Archives
8. Festivals and Living Traditions
9. Arts and Traditions
10. Knowledge and Education
11. Oral History
12. Cultural Timeline
13. Evidence and Verification

These are registered domain families, not a claim that every culture, community, language, tradition, text, artefact or historical source has been exhaustively inventoried. Detailed subtopics belong inside the authoritative domain/API/data layers and should not become empty Core folders.

## Manager interface

The canonical `get_manager()` factory returns `CulturalCoreManager`, which exposes:

- `status()` and `health()`
- `describe()`
- `list_products()` and `get_product()` (domain-package discovery aliases)
- `list_domains()`, `list_domain_inventory()` and `get_domain()`
- `list_offerings()` and `get_offering()`
- `get_domain_manager()`
- `knowledge()`, `search()` and `dependency_map()`

The manager reports metadata and registry state only. It does not claim live provider connections or execute external API calls.

## Evidence and community safeguards

Distinguish primary texts, documented history, oral testimony, traditional accounts, scholarly interpretation and contemporary application. Preserve source edition, provenance, uncertainty and conflicting accounts. Never approve a record without source references. Community, sacred, private and restricted knowledge requires the relevant custodian's informed permission. Online availability is not a license to reuse. Record consent, attribution, rights and takedown/correction status. Do not imply endorsement by a government, religious institution, community or academic body without documented authorization.

## Layer boundaries

Core does not implement API transport, authentication, storage, database, search indexing, AI, payments, commercial services or publication delivery. Those remain in their respective layers. Cultural Core discovery is not a grant of access, publication permission, copyright license or commercial right. Business use must be reviewed independently in the business ecosystem.

## Master catalog policy

The master catalog remains the system-wide source of taxonomy and implementation registration. Its target of 2,468 unique entries is a planning target, not the current implemented count. Do not change counts, fabricate entries, or add duplicate ecosystem records merely to satisfy the target. Register only verified ecosystem identities using the existing registry conventions.

## Verification status

This package currently declares 4 pillars and 13 registered domain families. Resource totals and live external connections are not verified. A production-complete or exhaustive-coverage claim requires repository-wide tests, source inventory validation and runtime verification; catalog registration alone is insufficient.
