# GLOBAL KAMASUTRA, RELATIONSHIP, INTIMACY, SEXUAL HEALTH AND ADULT WELLNESS CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Root:** `backend/core/global_ecosystem/global_core_ecosystem/global_kamasutra_relationship_intimacy_sex_chudai_porn_adult_health_wellness_core_ecosystem/`

## Mission
Canonical Core control plane for relationship and intimacy education, adult sexual wellness, reproductive-health domains, Kamasutra/traditional knowledge, lawful adult-media industry metadata, and related professional, technology and commerce ecosystems.

## Architecture
- `manager.py`: canonical entry point for status, inventory, product and domain discovery.
- `catalog.py`: one source of truth for all 62 existing product/package registrations.
- `domain_catalog.py`: 12 domain definitions and complete one-to-one package classification.
- `domain_runtime.py`: shared read-only implementation for the 12 domain managers.
- `orchestrator.py`: inventory, health, product lookup and dependency metadata.
- `service.py`: public ecosystem status.
- `contracts.py`: tenant, readiness and normalized result contracts.
- `policy.py`: age assurance, consent, rights, privacy and professional-boundary rules.
- `test_core_domains.py`: coverage, import, classification and safety tests.
- `PRODUCT_ECOSYSTEM_STANDARD.md`: ownership and package rules.
- `IMPLEMENTATION_STATUS.md`: implementation and verification status.

## Responsibility domains
1. **RELATIONSHIPS AND COMPATIBILITY** — `global_relationships_compatibility_core_ecosystem/`.
2. **SEXUAL EDUCATION AND TRADITIONAL KNOWLEDGE** — `global_sexual_education_traditional_knowledge_core_ecosystem/`.
3. **HEALTHCARE AND RESEARCH** — `global_sexual_reproductive_healthcare_research_core_ecosystem/`.
4. **COACHING AND COUNSELLING** — `global_relationship_intimacy_coaching_counselling_core_ecosystem/`.
5. **ADULT MEDIA AND CREATOR ECONOMY** — `global_adult_media_creator_economy_core_ecosystem/`.
6. **BUSINESS WORK AND TRAINING** — `global_adult_business_work_training_core_ecosystem/`.
7. **COMMERCE AND MARKETPLACES** — `global_adult_wellness_commerce_marketplace_core_ecosystem/`.
8. **TECHNOLOGY AND INFRASTRUCTURE** — `global_adult_technology_infrastructure_core_ecosystem/`.
9. **LAW SAFETY AND COMPLIANCE** — `global_adult_law_safety_compliance_core_ecosystem/`.
10. **PAYMENTS AND BILLING** — `global_adult_payments_billing_core_ecosystem/`.
11. **ADVERTISING AND DISTRIBUTION** — `global_adult_advertising_distribution_core_ecosystem/`.
12. **GLOBAL AND REGIONAL GOVERNANCE** — `global_adult_wellness_governance_partnerships_core_ecosystem/`.

## Package completeness rule
All 62 existing product folders are retained and registered exactly once. The 12 domain folders are classification/discovery facades over those product folders; they do not duplicate product implementations. Product folders receive additional files only when a real product-specific Core responsibility exists. No fixed empty subfolder template is generated.

## Layer ownership
Core owns identity, taxonomy, capability metadata, policy, lifecycle and readiness. API owns provider transport and integrations. Storage/Database own persistence. Engine owns jobs and execution. Frontend owns consent UX and user workflows. CRM/Business owns customer and commercial operations.

## Safety and scope
Only lawful adult contexts involving consenting adults are in scope. Minors, exploitation, trafficking, coercion, non-consensual intimate imagery and child sexual abuse material are prohibited. Applicable services require age assurance, informed consent, rights verification, privacy, reporting and moderation controls. Clinical diagnosis or treatment must be performed only by appropriately licensed professionals.

Catalog registration is not proof of legal eligibility, provider approval, API availability, user authorization, payment readiness or live connectivity. No PHP facade is included because no PHP consumer or cross-language contract is currently defined; Python is the canonical Core implementation.
