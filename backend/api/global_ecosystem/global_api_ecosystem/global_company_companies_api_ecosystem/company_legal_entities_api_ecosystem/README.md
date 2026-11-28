# Companies Directory

Registered legal entities and formally constituted organizations.

This package follows the modular domain-package pattern used by the Global Bada Business API Ecosystem. It owns category taxonomy, model, service facade and routes while using the parent ecosystem's shared read-only profile registry. Taxonomy membership is not proof of legal registration or verification.

## API
- `GET /api/v1/global-api-ecosystem/global/company-directory/company/catalog`
- `GET /api/v1/global-api-ecosystem/global/company-directory/company/profiles`
- `GET /api/v1/global-api-ecosystem/global/company-directory/company/search?q=...`
- `GET /api/v1/global-api-ecosystem/global/company-directory/company/profiles/{profile_id}`
