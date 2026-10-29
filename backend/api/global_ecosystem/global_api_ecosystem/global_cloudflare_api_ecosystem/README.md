# GLOBAL CLOUDFLARE API ECOSYSTEM

Cloudflare product/service-specific folders are maintained under this directory. Each product folder contains a README and a Python catalog module. The catalog is based on Cloudflare's official [product catalog](https://www.cloudflare.com/products/) and [developer documentation directory](https://developers.cloudflare.com/directory/).

## Structure

- `cloudflare_api_ecosystem.py` — main index
- `catalog_cloudflare_api_ecosystem/` — centralized product/service catalog
- Product folders — one nested folder per product/service area

Shared AI, APP, CLOUD, DOMAIN, SECURITY, SERVER, WEB and VPS category mappings stay in their respective GLOBAL API ECOSYSTEM folders and are not duplicated here.

**Important:** these files are catalog scaffolding, not live integrations. Product availability, public API coverage and account/plan eligibility vary. Live connections must be implemented and tested separately.


## Adult Industry category mapping

The Adult Industry mapping is intentionally maintained in the shared category directory, rather than as a duplicate provider-owned product folder here:

- [Cloudflare Adult Industry mapping](../global_adult_industry_api_ecosystem/cloudflare_adult_industry_api_ecosystem/README.md)
- Shared category: `global_adult_industry_api_ecosystem/cloudflare_adult_industry_api_ecosystem/`

This is a catalog-only cross-reference to general Cloudflare products that may be relevant (DNS/zones, security/WAF/API Shield, SSL/TLS, R2, Stream/Images, Workers/Pages, Analytics/Logpush). It does not indicate a dedicated Cloudflare adult-industry API or a live connection.
