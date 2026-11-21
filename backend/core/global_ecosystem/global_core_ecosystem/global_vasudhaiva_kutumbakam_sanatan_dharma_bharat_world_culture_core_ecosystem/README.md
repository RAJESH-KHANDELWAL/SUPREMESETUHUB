# GLOBAL VASUDHAIVA KUTUMBAKAM | SANATAN DHARMA | BHARAT SANSKRITI | WORLD CULTURE CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Root:** `backend/core/global_ecosystem/global_core_ecosystem/global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_core_ecosystem/`

## Mission and ownership

This Core layer is the read-only control plane for cultural domain identity, discovery, knowledge-resource metadata, evidence assessment, provenance, consent and publication-readiness boundaries. It preserves four distinct pillars: Vasudhaiva Kutumbakam, Sanatan Dharma, Bharat Sanskriti and World Culture.

The authoritative cultural knowledge source remains `backend/global_ecosystem/global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_ecosystem/`. The API domain remains under `backend/api/global_ecosystem/global_api_ecosystem/global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_api_ecosystem/`. The related business expression remains separate in the Bada Business ecosystem. Core references these layers and does not duplicate their implementations.

## Architecture

- `catalog.py`: ecosystem identity, pillars, domain registrations and layer references.
- `domain_catalog.py`: 13 canonical cultural Core domains.
- `domain_runtime.py`: shared read-only runtime reused by every domain package.
- `resource_catalog.py` and `resource_ecosystem_index.json`: source-backed knowledge discovery and domain-family metadata. No unverified resource count is invented.
- `contracts.py`: tenant and result contracts.
- `governance.py` and `policy.py`: record validation, evidence, consent, rights and access safeguards.
- `module_service.py`: reusable domain facade.
- `orchestrator.py`: discovery, health and dependency metadata.
- `service.py`: public service preserving the original `GlobalCulturalCore` interface.
- `manager.py`: canonical Python entry point; `manager.php`: PHP result facade.
- `test_cultural_core_domains.py`: structural and behavior tests.
- Each domain package contains only `__init__.py` and `manager.py`; shared logic is not copied into each package.

## Domain coverage

Sanatan Dharma; Bharat Sanskriti; Bharat Civilization; World Cultures; World Civilizations; Languages and Literature; Heritage and Archives; Festivals and Living Traditions; Arts and Traditions; Knowledge and Education; Oral History; Cultural Timeline; Evidence and Verification.

## Evidence and community safeguards

Distinguish primary texts, documented history, oral testimony, traditional accounts, scholarly interpretation and contemporary application. Preserve source edition, provenance, uncertainty and conflicting accounts. Never approve a record without source references. Community, sacred, private and restricted knowledge requires the relevant custodian's informed permission. Online availability is not a license to reuse. Record consent, attribution, rights and takedown/correction status. Do not imply endorsement by a government, religious institution, community or academic body without documented authorization.

## Layer boundaries

Core does not implement API transport, authentication, storage, database, search indexing, AI, payments, commercial services or publication delivery. Those remain in their respective layers. Cultural Core discovery is not a grant of access, publication permission, copyright license or commercial right. Business use must be reviewed independently in the business ecosystem.

## Status

This is a structured Core baseline over the 13 existing source domains, not an exhaustive catalogue of every world culture, community, tradition, language, text, artefact or historical source. No live external connections are verified by this package.
