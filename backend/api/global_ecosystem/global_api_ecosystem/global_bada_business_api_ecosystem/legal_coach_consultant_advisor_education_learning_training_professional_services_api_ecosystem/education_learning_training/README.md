# Education, Learning & Training — Linked Domain

This directory connects the Legal, Consulting & Professional Services discovery ecosystem to the existing canonical Education, Learning & Training industry.

## Canonical source — do not duplicate

The maintained education implementation already exists at:
`industry_api_ecosystems/education_learning_training`.

It owns the 15-category catalog, Python service, routes, schemas and tests. Its canonical global API ecosystem entry point is:
`global_education_learning_training_api_ecosystem`.

## Canonical education API

- `GET /industries/education-learning-training/status`
- `GET /industries/education-learning-training/categories`
- `GET /industries/education-learning-training/categories?q=university`
- `GET /industries/education-learning-training/categories/{category_id}`

## Cross-domain scope

Use this link for education providers and services relevant to professional development, including coaching and tutoring, professional and corporate training, vocational and skill development, technical education, language learning, certifications, lifelong learning and education consulting.

The education domain also maintains its own `coaches/`, `consultants/` and `advisors/` directories. Keep education-specific provider and category data in the canonical education domain; keep legal, accounting, compliance and general professional-service taxonomy in `professional_legal_business_services`.

## Boundary

This is a cross-domain navigation document, not a second education catalog or API implementation. Do not copy provider records, category registries, routes or services here. Provider credentials, institutional recognition, course accreditation and professional licences are not verified by this documentation.
