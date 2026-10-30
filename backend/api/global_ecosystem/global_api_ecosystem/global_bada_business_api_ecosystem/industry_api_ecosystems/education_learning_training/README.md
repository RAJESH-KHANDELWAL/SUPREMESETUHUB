# Education, Learning & Training API

Domain package within `industry_api_ecosystems`.

## Included taxonomy

The catalog currently defines 15 top-level categories covering school education, higher education, exam preparation, coaching, EdTech, corporate training, vocational skills, IT education, languages, study-abroad services, certification, inclusive education, lifelong learning, education infrastructure, and academic research services.

## Endpoints

Mounted under the Industry API router:
- `GET /industries/education-learning-training/status`
- `GET /industries/education-learning-training/categories`
- `GET /industries/education-learning-training/categories?q=university`
- `GET /industries/education-learning-training/categories/{category_id}`

## Scope and limitations

This is a structured taxonomy, not a verified directory of institutions, courses, accreditations, fees, admissions, jobs, or placements. No third-party integration is claimed. Verify institution recognition and accreditation with the relevant official authority before relying on education claims. Future provider connectors require official documentation, permissions, privacy controls, validation, and tests.
