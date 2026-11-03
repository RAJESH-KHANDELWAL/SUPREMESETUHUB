# Legal, Coaching, Consulting, Advisory, Education, Learning, Training & Professional Services API Ecosystem

Unified discovery and documentation home for legal services, coaches, consultants, advisors, education, learning, training and wider professional services.

## Core areas

- `categories/` — 12 legal and professional-services categories, each with category scope and API ecosystem documentation.
- `coaches/` — coaching professionals and services.
- `consultants/` — consulting professionals and services.
- `advisors/` — advisory professionals and services.
- `education_learning_training/` — cross-domain link to the canonical Education, Learning & Training industry.
- `jobs/` — employment and role discovery.
- `business/` — business and professional-service discovery.
- `india/` and `global/` — geographic discovery dimensions.
- `access_tiers/normal/` and `access_tiers/supreme/` — access-tier documentation.

## Canonical implementation ownership

The legal and professional-services taxonomy and Python API implementation remain in:
`industry_api_ecosystems/professional_legal_business_services`.

Its existing catalog, routes, schemas, service and tests are the canonical implementation for the 12 categories:
legal services; accounting and taxation; business consulting; company secretarial and compliance; human resources; marketing and advertising agencies; design and architecture; engineering consultancy; IT professional services; translation and localization; procurement and sourcing; testing and certification.

The education, learning and training implementation remains separately maintained in:
`industry_api_ecosystems/education_learning_training`.
It owns its 15-category catalog, routes, schemas, service and tests. Education-specific coaching, tutoring, professional/corporate training, vocational skills, certifications and lifelong learning belong to that canonical package.

## API endpoints

Legal and professional services:
- `GET /industries/professional-legal-business-services/status`
- `GET /industries/professional-legal-business-services/categories`
- `GET /industries/professional-legal-business-services/categories?q=...`
- `GET /industries/professional-legal-business-services/categories/{category_id}`

Education and training:
- `GET /industries/education-learning-training/status`
- `GET /industries/education-learning-training/categories`
- `GET /industries/education-learning-training/categories?q=...`
- `GET /industries/education-learning-training/categories/{category_id}`

## Data and professional safeguards

This is a taxonomy and discovery documentation ecosystem. It does not itself provide legal representation, legal advice, accredited education, verified provider listings, live vacancies, credential checks, professional licensing verification, government filing, payment processing, appointment booking or external integrations. Verify professional credentials, institutional recognition, course accreditation, safeguarding, privacy, jurisdiction and current law through appropriate official sources before relying on or publishing provider claims.

No duplicate Python catalogs, provider records or API routes are created in this documentation folder.
