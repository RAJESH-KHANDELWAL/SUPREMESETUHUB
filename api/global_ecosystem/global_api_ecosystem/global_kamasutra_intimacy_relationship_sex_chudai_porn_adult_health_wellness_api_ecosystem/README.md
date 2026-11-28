# GLOBAL KAMASUTRA | INTIMACY | RELATIONSHIP | SEX | PORN | ADULT HEALTH & WELLNESS API ECOSYSTEM

**Global location:** `backend/api/global_ecosystem/global_api_ecosystem/global_kamasutra_intimacy_relationship_sex_chudai_porn_adult_health_wellness_api_ecosystem/`

**Scope:** Bharat + Global World; adults aged 18+; consent-first, privacy-preserving taxonomy and adult-industry API scaffold.

This is the Global copy of the adult-only ecosystem. A matching copy with the exact same folder name is also maintained under the Bada Business ecosystem; neither location replaces the other. The former `adult_18_plus_lawful_industry_business_api_ecosystem/`, `adult_business_api_ecosystem/` and `adult_sexual_wellness/` folder layers have been removed from the root; their contents are integrated here.

## Coverage

- Kamasutra, adult relationships, couples communication, marriage education and relationship coaching
- Adult family-relationship education, co-parenting communication and qualified counselling referrals (18+ service discovery; safeguarding remains separate)
- Adult intimacy and sexual wellness education
- Adult body confidence, intimacy-related mobility, pelvic-floor wellness education and non-clinical adult fitness/wellbeing coaching (not general gym or medical treatment)
- Clinical sexual-health services (licensed professionals only)
- Relationship counselling and therapy (qualified professionals only)
- Lawful adult media and entertainment, with consent, age assurance and licensing
- Adult wellness products, lawful commerce and professional services
- Coaching, consulting, training, careers and business services
- Adult industry provider catalog references (25 provider folders; catalog-only, not live API connections)
- Research, privacy, safety and jurisdiction-specific compliance
- Restricted 18+ lawful-industry classification taxonomy (default discovery disabled)

## Consolidated modules

- The original Kamasutra taxonomy, routes, schemas, service and 35 domain folders remain at this root.
- Adult 18+ lawful-industry modules are retained as prefixed Python modules to avoid collisions with the original Kamasutra `catalog.py`, `models.py`, `service.py` and `subcategories.py`.
- The 25 adult-industry provider folders are direct children of this ecosystem.
- `adult_sexual_wellness_compat.py` retains a compatibility import to the maintained sexual-wellness taxonomy.

## Cross-ecosystem classification boundary

- Family relationship, couple communication, marriage and adult relationship categories are consolidated here. General parenting, child welfare, elder care, caregiver support and non-sexual community services remain in the Family & Community ecosystem.
- Clinical sexual and reproductive medicine remains in Healthcare, Medical & Life Sciences; this ecosystem may reference those clinical pathways but does not replace licensed care.
- General gyms, sports fitness, nutrition, weight management, yoga, spa and massage remain in the Healthcare, Wellness & Fitness industry ecosystem. Only adult intimacy-related body confidence, mobility and non-clinical wellness education are classified here under the 18+ boundary.
- Adult categories are restricted and must not be exposed through default public discovery. Cross-references must not duplicate provider records.

## Safety and compliance

- Adults 18+ only; no minors, exploitation, trafficking, coercion or non-consensual intimate content.
- Clinical diagnosis and treatment must be provided by appropriately licensed professionals.
- Coaches and consultants must not represent themselves as clinicians.
- Lawful adult media requires documented consent, age assurance, licensing and jurisdiction review.
- India and international requirements must be assessed separately before launch.

## Implementation status

This is a taxonomy/API scaffold, not a verified provider directory, medical or legal advice, or proof of live integrations. Provider modules remain catalog references unless their documentation and live connections are independently verified. The Global API router is mounted under `/api/v1/global-api-ecosystem/adult-wellness`; the Bada Business copy is mounted at `/api/v1/global-ecosystem/business/kamasutra/adult-wellness` and remains available through the Bada Business catalog endpoints. Both locations must pass regression tests and production access-control checks before launch.


## Dual-location architecture

- Global copy: `backend/api/global_ecosystem/global_api_ecosystem/global_kamasutra_intimacy_relationship_sex_chudai_porn_adult_health_wellness_api_ecosystem/`.
- Bada Business copy: `backend/api/global_ecosystem/global_api_ecosystem/global_bada_business_api_ecosystem/global_kamasutra_intimacy_relationship_sex_chudai_porn_adult_health_wellness_api_ecosystem/`.
- Both copies use the exact same folder name and retain their own package files. The Global copy is mounted through the Global API router; the Bada Business registry resolves its local copy.
- This is a non-destructive dual-location arrangement, not a move. Keep both locations in future updates.
