# GLOBAL COMPANY / COMPANIES API ECOSYSTEM

A source-aware directory for company records, with separate compatibility surfaces for operating businesses and independent professionals.

## Main components
- Shared, source-aware profile registry and search service.
- Separate record-class packages for legal companies, operating businesses and independent professionals.
- Company-specific module index for the existing company packages under `global_companies_ecosystem/`.
- Industry, country and provider registries, with explicit readiness boundaries.
- Company world-map metadata, data-source directory, integrations, services, tools and tests.

## Company module directory
The `company_modules_api_ecosystem/` package indexes the company-specific code modules already present in this repository. It exposes list, search, detail and status endpoints. This index is deliberately separate from company profile records: package presence does not mean verified profile data exists or that the module is connected to the shared JSON registry.

## Data and integration status
The local `data/company_registry.json` profile registry is currently empty. Country/provider metadata is not a live government or provider connection. No worldwide completeness, company verification, or live external data feed is implied.

See [GLOBAL_COVERAGE_AND_CLASSIFICATION.md](GLOBAL_COVERAGE_AND_CLASSIFICATION.md) and [company_modules_api_ecosystem/README.md](company_modules_api_ecosystem/README.md).
