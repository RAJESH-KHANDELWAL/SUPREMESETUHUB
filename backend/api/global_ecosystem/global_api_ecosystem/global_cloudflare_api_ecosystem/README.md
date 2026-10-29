# GLOBAL CLOUDFLARE API ECOSYSTEM

Cloudflare product/service-specific folders are maintained under this directory. Each product folder contains a README and a Python catalog module. The catalog is based on Cloudflare's official [product catalog](https://www.cloudflare.com/products/) and [developer documentation directory](https://developers.cloudflare.com/directory/).

## Structure

- `cloudflare_api_ecosystem.py` — main index
- `catalog_cloudflare_api_ecosystem/` — centralized product/service catalog
- Product folders — one nested folder per product/service area
- `adult_industry_cloudflare_api_ecosystem/` — mapping of Cloudflare services potentially relevant to adult-industry websites (not a dedicated adult-industry API)

Shared AI, APP, CLOUD, DOMAIN, SECURITY, SERVER, WEB and VPS category mappings stay in their respective GLOBAL API ECOSYSTEM folders and are not duplicated here.

**Important:** these files are catalog scaffolding, not live integrations. Product availability, public API coverage and account/plan eligibility vary. Live connections must be implemented and tested separately.
