# Businesses Directory

Operating businesses that may or may not be represented as a separately registered legal entity, including sole proprietors, MSMEs, startups and franchises.

This package follows the modular domain-package pattern used by the Global Bada Business API Ecosystem. It owns category taxonomy, model, service facade and routes while using the parent ecosystem's shared read-only profile registry. Taxonomy membership is not proof of legal registration or verification.

## API
- `GET /api/v1/global-api-ecosystem/global/company-directory/business/catalog`
- `GET /api/v1/global-api-ecosystem/global/company-directory/business/profiles`
- `GET /api/v1/global-api-ecosystem/global/company-directory/business/search?q=...`
- `GET /api/v1/global-api-ecosystem/global/company-directory/business/profiles/{profile_id}`
