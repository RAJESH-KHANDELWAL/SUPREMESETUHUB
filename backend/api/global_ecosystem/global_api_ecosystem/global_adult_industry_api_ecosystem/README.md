# GLOBAL ADULT INDUSTRY API ECOSYSTEM

This directory contains catalog metadata for adult-industry service providers. These entries are separate from the shared AI API ecosystem.

Provider folders are catalog/routing records only. They do not prove an official API exists or that authentication, live requests, eligibility, or production integration have been tested. Before implementation, verify official provider documentation, API/partner access, terms, privacy, consent, age-gating, payment compliance, and security requirements.

## Provider categories

- Cloud / infrastructure mapping: Cloudflare (general supported products only; no dedicated adult-industry API implied)
- Hosting: Abelohost, ViceTemple
- Video platforms and studios: Faphouse, Pornhub, XVideos, xHamster, Naughty America, Brazzers, Reality Kings, BangBros, Evil Angel
- Creator platforms: OnlyFans, Fansly, ManyVids, Clips4Sale, LoyalFans
- Payments and payouts: CCBill, Segpay, Verotel, Epoch, Paxum
- Affiliate and advertising: CrakRevenue, TrafficJunky, ExoClick

All provider-specific folders below are metadata scaffolds, not live adapters.


## Provider-to-category mappings

- [Cloudflare Adult Industry mapping](cloudflare_adult_industry_api_ecosystem/README.md) — catalog-only routing to relevant general Cloudflare products, not a dedicated adult-industry API or live integration.


## Cross-category mappings

The Adult Industry category is the canonical classification for the providers listed here. Category-specific views are maintained separately and do not replace this canonical record:

- **AI API:** [GLOBAL AI API ECOSYSTEM](../global_ai_api_ecosystem/README.md) contains catalog-only AI-family routing folders for some adult-industry providers. Their presence does not prove the provider offers an official AI API.
- **APP API:** [GLOBAL APP API ECOSYSTEM](../global_app_api_ecosystem/README.md) contains app/platform views for creator platforms, studios and video services.
- **CLOUD API:** [GLOBAL CLOUD API ECOSYSTEM](../global_cloud_api_ecosystem/README.md) includes only verified cloud-infrastructure API categories. Adult-friendly hosting/VPS vendors remain routed to ADULT INDUSTRY/HOSTING/SERVER unless official cloud APIs are confirmed.
- **Cloudflare:** [Adult Industry mapping](cloudflare_adult_industry_api_ecosystem/README.md) references only relevant general Cloudflare products; it is not a dedicated adult-industry API and is not live-connected.

The central provider registry in backend/api/global_api_ecosystem_catalog.py now routes adult-industry provider catalog paths to this shared category instead of legacy paths under the AI category. Registry family labels describe project routing targets only; all remain CATALOG_ONLY until documentation, credentials, permissions and tests confirm support.
