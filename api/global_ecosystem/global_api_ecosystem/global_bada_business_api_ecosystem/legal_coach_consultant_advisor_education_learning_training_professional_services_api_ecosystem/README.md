# Professional Coaching, Consulting, Advisory, Education, Learning & Training Services API Ecosystem

A unified India + Global discovery and documentation layer for professional coaches, consultants, advisors, educators, trainers, learning providers, institutions and other professional service providers.

- Geographic scope: Bharat (India) and international markets
- Delivery channels: online, offline and hybrid
- Audience: individuals, students, families, professionals, founders, MSMEs, enterprises, institutions, public bodies and nonprofit organisations
- Status: taxonomy and discovery documentation; provider verification and production integrations are separate work

## Unified professional domains

### 1. Coaching services
- Business, entrepreneurship, startup and MSME coaching
- Executive, leadership, management and team coaching
- Career, employability, interview and workplace coaching
- Sales, marketing, customer experience and negotiation coaching
- Productivity, performance, communication and public-speaking coaching
- Personal development, goal-setting and life-skills coaching
- Financial-literacy and money-management education (not regulated investment advice)
- Digital skills, technology adoption and digital-business coaching
- Fitness, sports, nutrition and wellbeing coaching, subject to relevant professional scope
- Relationship, parenting and family-skills education within lawful and appropriate boundaries

### 2. Consulting services
- Business strategy, growth, operations and management consulting
- Startup, entrepreneurship, franchise and MSME consulting
- Process improvement, quality, productivity and organisational development
- Human resources, talent, learning and workforce consulting
- Technology, software, AI, data, cybersecurity and digital-transformation consulting
- Marketing, branding, communications and customer research consulting
- Finance operations, accounting systems and business planning support
- Architecture, engineering, project and sustainability consulting
- Education, institutional development and training-programme consulting
- Research, analytics, market intelligence and documentation consulting

### 3. Advisory services
- Business, corporate, strategic and management advisory
- Startup, fundraising-readiness and business-model advisory (no guarantee of funding)
- Career, education-pathway and professional-development advisory
- HR, leadership, governance and organisational advisory
- Digital transformation, technology and innovation advisory
- Operations, supply-chain and project advisory
- Financial education and general financial-planning information; regulated advice only through appropriately authorised professionals
- Sector-specific technical and institutional advisory

### 4. Education, learning and training
- Early childhood, school and higher education
- Competitive and entrance examination preparation
- Coaching, tuition, tutoring and academic support
- Online learning, EdTech and digital course platforms
- Professional, corporate and leadership training
- Vocational, trade, technical and skill development
- IT, software, AI, data, cloud and cybersecurity education
- Language, communication and soft-skills learning
- Study-abroad and admissions guidance
- Certifications, assessment and examination services
- Special, inclusive and lifelong learning
- Education infrastructure, research and academic support

### 5. Wider professional services
- Accounting, bookkeeping, taxation support and audit/assurance
- Human resources, recruitment and talent services
- Architecture, interior design and engineering consultancy
- Translation, interpretation and localisation
- Business process outsourcing and virtual administration
- Professional writing, editing and documentation
- Research, business analytics and reporting

## Canonical implementation ownership

This folder is the unified discovery/documentation home. It must not create duplicate provider records, category registries, Python services or API routes.

- **Professional Services:** canonical non-legal professional-services implementation is maintained in `industry_api_ecosystems/professional_legal_business_services`.
- **Education, Learning & Training:** canonical education implementation is maintained in `industry_api_ecosystems/education_learning_training`.
- Coaching, consulting and advisory directories in this folder classify professional specialisations and discovery dimensions. Where a service belongs to a canonical industry package, that package owns its category data and API operations.

Existing canonical endpoints remain:
- `GET /industries/professional-legal-business-services/status`
- `GET /industries/professional-legal-business-services/categories`
- `GET /industries/professional-legal-business-services/categories?q=...`
- `GET /industries/professional-legal-business-services/categories/{category_id}`
- `GET /industries/education-learning-training/status`
- `GET /industries/education-learning-training/categories`
- `GET /industries/education-learning-training/categories?q=...`
- `GET /industries/education-learning-training/categories/{category_id}`

## Geographic and delivery dimensions

Use `india/` for India-specific professional contexts, qualifications, institutional structures and jurisdictional references. Use `global/` for country- and region-specific contexts. Do not assume that an Indian qualification, licence, accreditation or professional title is automatically recognised in another jurisdiction.

Each provider or service record should be classified by:
- Country, state/province, city and service area
- Online, offline or hybrid delivery
- Professional domain and specialisation
- Intended audience and service language
- Qualifications, registrations and licences where applicable
- Experience and evidence-backed credentials
- Service format, availability and published pricing where verified
- Accessibility, privacy, safeguarding and complaints process

## Legal and regulated-service boundary

Legal services, lawyers, litigation, legal opinions, legal documentation and legal representation are excluded from this professional coaching/consulting/education taxonomy. Their category documentation is consolidated under `../global_legal_services_api_ecosystem/`. The Legal Services runtime API is not claimed to be implemented by this documentation move; implementation and registration must be handled separately.

Regulated accounting, audit, tax, financial, healthcare, engineering, architecture and other licensed work must be clearly distinguished from general coaching or informational services and delivered only by professionals authorised for the relevant jurisdiction. Coaching must not be presented as therapy, medical care, legal advice or regulated financial advice unless the provider is appropriately qualified and authorised.

## Verification and implementation limits

This taxonomy does not prove that a provider exists, is active, qualified, licensed, accredited, insured or endorsed. It does not represent live listings, verified vacancies, course accreditation, payments, bookings or production integrations. Verify identity, credentials, professional registrations, institutional recognition, safeguarding, privacy, consumer protections and local law before publishing provider claims or enabling transactions.

The legacy directory name is retained for path compatibility; the ecosystem's current display name and scope are defined by this README.
