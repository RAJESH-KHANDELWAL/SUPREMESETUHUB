# Education, Learning & Training API Ecosystem

Independent domain package. Existing catalog and routes remain the maintained implementation; this structure separates service domains and access tiers.

## Separate directories
- categories/: one file per education category
- jobs/: education-sector roles and hiring taxonomy
- business/: institutions, providers and education businesses
- india/: Bharat-specific education systems and references
- global/: international education systems and references
- coaches/, consultants/, advisors/: distinct professional service directories
- relationships/: age-appropriate relationship and family learning
- access_tiers/normal/, supreme/, adult_18_plus/: separate access tiers

## Adult 18+ boundary
Adult-only material must be lawful, consensual, age-gated, privacy-protective and jurisdiction-reviewed. This tier is limited to lawful adult education/wellness and non-graphic compliance metadata. Exclude minors, exploitation, coercion, non-consensual material and sexual content involving family members or relatives. Family content belongs only in non-sexual education and support.

## Existing API
- GET /industries/education-learning-training/status
- GET /industries/education-learning-training/categories
- GET /industries/education-learning-training/categories?q=university
- GET /industries/education-learning-training/categories/{category_id}

## Limitations
These folders are taxonomy scaffolding, not verified listings, live vacancies, accredited courses, provider integrations or functioning access-control enforcement. Verify credentials, licenses, safeguarding, privacy and applicable laws before publication.
