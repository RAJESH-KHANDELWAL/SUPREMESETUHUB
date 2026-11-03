# KAMASUTRA | INTIMACY | RELATIONSHIP | SEX | CHUDAI | PORN | ADULT | HEALTH | WELLNESS | COACH | CONSULTANT | ADVISOR | PROFESSIONAL SERVICES | WORK & BUSINESS API ECOSYSTEM

**Canonical package:** `kamasutra_intimacy_relationship_sex_chudai_porn_adult_health_wellness_coach_consultant_advisor_professional_services_work_business_api_ecosystem`  
**Scope:** Bharat + Global World; adult-only (18+), consent-first, privacy-preserving taxonomy and business/work API scaffold.

This package separates education, clinical healthcare, relationships, lawful adult media, products, careers, coaching, consulting, professional services, technology, trade, research and compliance. It is a taxonomy scaffold, not a verified provider directory, medical advice, legal advice, or proof of live integrations.

## Safety and scope
- Adult-only contexts; no minors, exploitation, trafficking, coercion, or non-consensual intimate content.
- Lawful adult media only, with consent, age assurance, licensing and jurisdiction review.
- Clinical services must be delivered by appropriately licensed professionals; coaches and consultants must not present themselves as clinicians.
- India and international legal requirements must be reviewed separately before launch.

## Package layers
- `subcategories.py`: all domain folder IDs and labels.
- `models.py`: typed taxonomy record.
- `catalog.py`: consolidated taxonomy records.
- `service.py`: search, detail and status operations.
- `schemas.py`: API response schemas.
- `routes.py`: FastAPI router; parent router registration is a separate integration step.
- Each domain has its own folder with `README.md` and `catalog.py`.
