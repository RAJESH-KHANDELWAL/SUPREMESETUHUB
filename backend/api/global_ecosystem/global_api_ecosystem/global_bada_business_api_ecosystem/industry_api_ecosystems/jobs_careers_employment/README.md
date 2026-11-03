# Jobs, Careers & Employment API Ecosystem

Stable domain identifier: `jobs_careers_employment`.

## Scope and separate taxonomies

This package provides a structured India-and-global taxonomy across online, offline and hybrid channels. It is a discovery/API foundation, not a verified directory of providers, a live vacancy feed, a transaction system or a compliance certification.

Two distinct taxonomies are exposed and must remain separate:

1. **Industry/service taxonomy:** 15 top-level business categories covering recruitment portals, freelancing platforms, remote-work services, staffing, HR/payroll, career guidance, internships, executive search, workforce management, resume/interview services, employer branding, employment compliance, outsourcing/BPO, reskilling and professional networking. Each category has four canonical subcategories.
2. **Employment classification taxonomy:** the separate 24-category Work, Jobs & Careers taxonomy, including Government Jobs, Private Sector Jobs, Corporate Jobs, Public Sector Jobs, International Jobs, Local Jobs, Remote Jobs and other employment classifications. Its maintained source remains the Work, Jobs & Careers domain package; this industry API exposes it without duplicating its records.

## Independent package architecture

Every one of the 15 industry categories has its own folder and its own README, `__init__.py`, `categories.py`, `models.py`, `catalog.py`, `schemas.py`, `services.py`, `routes.py`, `validators.py` and `tests/`.

Every one of the 60 industry subcategories has its own nested folder and the same independent file structure. Each leaf resolves its ID from the parent category's canonical `catalog.py`; metadata is not forked into duplicate sources.

The domain-level `catalog.py` remains the source of truth for the 15 industry categories and their 60 subcategory IDs. The separate employment taxonomy remains sourced from the Work, Jobs & Careers domain package.

## API

- `GET /industries/jobs-careers-employment/status`
- `GET /industries/jobs-careers-employment/categories`
- `GET /industries/jobs-careers-employment/categories/{category_id}`
- `GET /industries/jobs-careers-employment/categories/{category_id}/package`
- `GET /industries/jobs-careers-employment/categories/{category_id}/package/subcategories`
- `GET /industries/jobs-careers-employment/categories/{category_id}/package/subcategories/{subcategory_id}`
- `GET /industries/jobs-careers-employment/employment-categories`
- `GET /industries/jobs-careers-employment/employment-categories/{category_id}`

Category and subcategory packages also expose `/status` and `/integrity` endpoints.

## Boundaries and data quality

All category and subcategory packages are taxonomy scaffolds. They do not assert live vacancies, verified employers, genuine clients, provider onboarding, recruitment outcomes, legal eligibility, professional licensing or regulatory approval.

Before ingesting real listings/providers, add source provenance, original URL, jurisdiction, employer/provider identity, publication and expiry timestamps, last-verified timestamp, deduplication, moderation, consent and verification state. Do not infer visa sponsorship, work authorization, statutory compliance or professional credentials from a category label.

## Maintenance

Keep stable IDs lowercase snake_case. Do not duplicate employment-classification records inside the industry/service taxonomy. Cross-domain overlaps (for example, freelance marketplaces and remote jobs) must be connected by explicit crosswalks, not by merging distinct category meanings.
