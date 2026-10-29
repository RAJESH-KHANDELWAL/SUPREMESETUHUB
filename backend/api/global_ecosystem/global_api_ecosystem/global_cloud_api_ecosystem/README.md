# GLOBAL CLOUD API ECOSYSTEM

This family lists providers whose cloud infrastructure/API capability is documented or is a recognized public cloud platform. A catalog entry is not proof of a live connection; every integration remains catalog-only until official API documentation, credentials, permissions and tests are verified.

## Cloud infrastructure and API providers

The central registry at `backend/api/global_api_ecosystem_catalog.py` is the source of truth for provider-to-family membership. Providers include major global cloud platforms and API-backed infrastructure providers such as AWS, Google Cloud, Microsoft Azure, Oracle Cloud, Alibaba Cloud, Tencent Cloud, Huawei Cloud, Baidu AI Cloud, JD Cloud, Kingsoft Cloud, China Telecom Cloud, IBM Cloud, DigitalOcean, Rackspace, Scaleway, OVHcloud, Hetzner Cloud and Vultr. Object-storage providers such as Backblaze and Wasabi are included only as API-backed cloud/storage services, not as general-purpose compute clouds.

## Not automatically a CLOUD API provider

Adult-friendly hosting vendors and general web-hosting companies must not be listed in this family merely because they sell hosting, VPS or server products. The following entries had no official API documentation verified in this catalog and have therefore been removed from the central `CLOUD` family membership: AbeloHost, ViceTemple, FlokiNET, Shinjiru, HostSailor, BlueAngelHost, AlexHost and HOSTKEY. Their provider discovery records belong under the relevant ADULT_INDUSTRY/HOSTING/SERVER families unless and until an official cloud API is verified.

## Scope boundary

- Cloud APIs mean documented programmatic interfaces for cloud account, compute, networking, infrastructure, resource lifecycle or cloud operations.
- VPS provisioning and lifecycle APIs belong in GLOBAL VPS API ECOSYSTEM; general hosting control panels belong in GLOBAL HOSTING API ECOSYSTEM unless an official cloud API is established.
- Catalog membership is not proof that a public API exists, that an account is eligible, or that authentication works.
- Do not mark any provider live until official API documentation, required scopes/permissions, secure credentials, adapter behavior and tests have been verified.
- Never commit credentials or secrets.
