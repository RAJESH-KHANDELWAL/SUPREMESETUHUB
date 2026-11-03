# Jobs, Careers & Employment Industry Adapter

Stable industry identifier: `jobs_careers_employment`.

## Purpose
This package is the industry-facing discovery and API adapter for employment-related businesses and services. It is not a second work/job taxonomy and does not own job-category definitions.

## Canonical ownership
- **Work and employment context** (Government Jobs, Private Sector Jobs, Corporate Jobs, Public Sector Jobs, Local Jobs, Remote Jobs, Full-Time, Contract, etc.) is owned only by `work_careers_employment_business_api_ecosystem/categories.py`.
- **Freelance, gig and independent-service skills** are owned only by `freelance_gig_independent_work_business_api_ecosystem`.
- **Cross-industry A–Z sectors and work-model facets** are owned only by `universal_work_business_taxonomy_api_ecosystem`.
- **Employment-industry service/provider classification** is distinct: recruitment agencies, staffing services, career guidance providers, placement services, HR/payroll vendors, and job-platform operators. This adapter must not copy existing Work & Careers category definitions.

## Current safe scope
The industry adapter exposes the existing Work & Careers category catalogue by stable ID and identifies the owning domain. No separate duplicate catalogue is maintained here. Industry-provider service categories are not expanded until their non-overlapping definitions and owner are established.

## Endpoints
- `GET /industries/jobs-careers-employment/status`
- `GET /industries/jobs-careers-employment/categories`
- `GET /industries/jobs-careers-employment/categories?q=...`
- `GET /industries/jobs-careers-employment/categories/{category_id}`
- `GET /industries/jobs-careers-employment/employment-categories`
- `GET /industries/jobs-careers-employment/employment-categories?q=...`
- `GET /industries/jobs-careers-employment/employment-categories/{category_id}`

The last three endpoints are compatibility aliases into the canonical Work & Careers catalogue. They must not create another copy of its source records.

## Status
Taxonomy and adapter only. This package does not supply live vacancies, verified employers, recruiter authorizations, or legal eligibility decisions.
