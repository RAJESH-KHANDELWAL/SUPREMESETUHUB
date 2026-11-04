# Education, Learning & Training API Ecosystem

Canonical industry ID: `education_learning_training`  
Coverage target: India + Global  
Current top-level categories: 19  
Status: `taxonomy_scaffold`

This is the maintained education industry package. Upgrade it in place; do not create another industry package for education, student learning or skills.

## Category coverage

The 19 categories cover:
- Early childhood, school and higher education
- Competitive examinations, coaching and tutoring
- Online learning, EdTech and virtual classrooms
- Professional, corporate and vocational training
- Technical, IT, computer, AI, Generative AI and data-literacy education
- Language learning, communication and study-abroad admissions
- Certification, assessment and inclusive education
- Career learning, lifelong learning, research and academic services
- Digital skills, freelancing and remote-work training
- Entrepreneurship, MSME and business education
- Digital marketing and creator-economy training

## Dedicated API

- `GET /industries/education-learning-training/status`
- `GET /industries/education-learning-training/categories`
- `GET /industries/education-learning-training/categories?q=university`
- `GET /industries/education-learning-training/categories/{category_id}`
- `GET /industries/education-learning-training/cross-ecosystem-links`

The existing route contract and stable category IDs are retained. Search covers category IDs, names and subcategory IDs. Existing category IDs and response contracts are retained. Existing AI/data literacy, freelancing/remote-work, MSME/business education and digital-marketing tracks are extended with credential, portfolio, AI-evaluation and learning-interoperability subtopics.

## Cross-ecosystem links

The cross-ecosystem endpoint points to the canonical student/skills, jobs/employment, science/research, technology and classification-standard domains. It does not copy their records. Any occupation or qualification mapping must cite the source standard, version and reviewed crosswalk.

## India and Global coverage

Keep India-specific and country-specific/global education records separately identified. Future records should carry country/jurisdiction, source, source version, last-verified timestamp, recognition/accreditation status, delivery mode, language, age/grade applicability and verification state. Do not infer recognition or accreditation from a provider's own claims.

## Learning and credential safeguards

- Course completion is not automatically a regulated qualification, licence or accredited credential.
- Accreditation, examination authority, professional recognition and certificate issuer must be independently evidenced.
- Protect learner records, minors' data, assessment results and accessibility needs; collect only necessary data.
- Provide age-appropriate safeguarding and moderation for learner-to-learner and learner-to-instructor interactions.
- AI education should teach limitations, privacy, intellectual-property awareness, bias, human review and responsible use.
- Freelancing and remote-work education is training only; it does not represent a job vacancy, guaranteed client, guaranteed income or payment service.
- Business education is learning content, not legal, tax, investment or regulated financial advice.

## Adjacent ecosystem boundaries

- The `students_education_skills_business_api_ecosystem` remains a separate core student/skills taxonomy layer. Cross-reference stable IDs where appropriate; do not copy its records into this industry catalog.
- AI research, model development and scientific R&D remain in Science, Research, Innovation & Technology. This package covers teaching and learning about AI.
- Technology/software industry catalogs describe products and services; this package describes education and training about them.
- Jobs and vacancies remain in Jobs, Careers & Employment. Training records must not be represented as employment listings.
- Business consulting and professional services remain in their owning ecosystems. This package covers structured education and training only.

## Existing directory structure

- `categories/`: category-specific documentation
- `jobs/`: education-sector role taxonomy and hiring concepts
- `business/`: institutions and education-provider business concepts
- `india/` and `global/`: jurisdiction-specific reference boundaries
- `coaches/`, `consultants/`, `advisors/`: distinct professional directories
- `access_tiers/`: normal, supreme and adult-only taxonomy boundaries

These folders are scaffolding, not verified listings, live vacancies, accredited courses, provider integrations or functioning access-control enforcement. Verify sources, credentials, safeguarding, privacy and applicable law before publishing live records.
