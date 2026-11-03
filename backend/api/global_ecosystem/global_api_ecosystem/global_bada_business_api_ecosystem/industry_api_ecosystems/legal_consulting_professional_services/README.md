# Legal, Consulting & Professional Services — Compatibility Domain

Stable ID: `legal_consulting_professional_services`  
Status: `taxonomy_scaffold` / compatibility discovery layer.

## Canonical source

The canonical maintained taxonomy and Python API package is `industry_api_ecosystems/professional_legal_business_services`. It already contains 12 top-level categories, catalog, schemas, routes, service and tests. This folder must not create a second category registry or duplicate provider records.

## Purpose

This domain name provides a clearer legal/consulting-oriented discovery entry point. Its categories map to the canonical package:

- `legal_services` — Legal Services
- `accounting_taxation` — Accounting & Taxation
- `business_consulting` — Business Consulting
- `company_secretarial` — Company Secretarial & Compliance
- `human_resources` — Human Resources Services
- `marketing_agencies` — Marketing & Advertising Agencies
- `design_architecture` — Design & Architecture
- `engineering_consultancy` — Engineering Consultancy
- `it_professional_services` — IT Professional Services
- `translation_localization` — Translation & Localization
- `procurement_advisory` — Procurement & Sourcing
- `testing_certification` — Testing & Certification Services

## Scope and limitations

This is a taxonomy/discovery structure, not a legal advice service, law firm, CA/CS practice, regulator, government portal or professional licensing authority. No professional credentials, bar enrolment, certificate of practice, firm registration, accreditation, provider quality, client relationship or statutory eligibility is verified by this scaffold. Applicable jurisdiction and current law must be checked through official sources and qualified professionals. Never present an unverified listing as approved or certified.

## Data ownership

Keep category definitions and API behavior in the canonical `professional_legal_business_services` package. Add a compatibility route or import facade only after explicit integration tests confirm that IDs and schemas remain consistent.
