# GLOBAL API ECOSYSTEM

This directory contains the API-family ecosystems under the GLOBAL API ECOSYSTEM parent. Keep each family package separate and use the central provider catalog as the source of truth; do not copy provider implementation code into every family.

## API families
Adult Industry, AI, App, Business, Cloud, Communication, Companies, Database, Developer, Domain, Freelancer, Hosting, Individual, Integrations, Intimacy, Language, Payment, Platforms, Security, Server, Services, Social Media, Software, Storage, System, Tools, Video, Web and Website.

## Provider ecosystems and family placement

The central provider catalog lives in `backend/api/global_api_ecosystem_catalog.py`; FastAPI routes live in `backend/api/global_api_ecosystem_routes.py`. The existing company-specific provider packages for Google, Microsoft, AWS and Apple are the canonical vendor identities. Family folders should contain provider-specific adapters only where the provider offers a relevant, supported API.

| Family | Google | AWS | Microsoft | Apple |
|---|---|---|---|---|
| AI | Gemini / Vertex AI, subject to API access | Amazon Bedrock | Azure AI services | Apple Intelligence / developer APIs where publicly available |
| App | Android and Google Play APIs | App hosting and application services | App platform and identity APIs | App Store Connect and Apple developer APIs |
| Business | Workspace and business APIs | Business/cloud services | Microsoft 365 and Graph | Apple Business Manager APIs where available |
| Cloud | Google Cloud | AWS | Microsoft Azure | Apple cloud APIs only where officially exposed |
| Communication | Gmail and Google Meet APIs | SES and supported messaging integrations | Microsoft Graph, Outlook and Teams APIs | Push notification and communication APIs where available |
| Companies | Google provider identity/package | AWS provider identity/package | Microsoft provider identity/package | Apple provider identity/package |
| Database | Cloud SQL and Firestore | RDS, DynamoDB and supported database APIs | Azure SQL and Cosmos DB | No general-purpose hosted database service assumed |
| Developer | Google developer APIs | AWS SDK and developer APIs | Microsoft developer APIs and SDKs | Apple Developer and App Store Connect APIs |
| Domain / DNS | DNS and domain-related APIs only where currently offered | Route 53 and Route 53 Domains, subject to eligibility | Azure DNS; domain registration may require a separate registrar | No general-purpose registrar assumed |
| Hosting | Cloud Run and supported app-hosting products | EC2, Lightsail and supported hosting services | Azure App Service and supported hosting services | No general-purpose public web-hosting provider assumed |
| Integrations | OAuth, SDK and API connectors | AWS SDK and API connectors | Microsoft Graph, OAuth and SDK connectors | Sign in with Apple and official SDK connectors |
| Payment | Google Pay APIs where supported in the target country/product | Payment integrations only when an actual service/API is available | Payment integrations only when an actual service/API is available | Apple Pay, subject to merchant, region and platform eligibility |
| Platforms | Google Workspace, Google Play and Google Cloud | AWS Console and AWS services | Microsoft 365 and Azure | Apple App Store and Apple developer platforms |
| Security | Google Cloud IAM and security APIs | IAM and AWS security services | Microsoft Entra ID and Defender APIs | Sign in with Apple and officially supported security APIs |
| Server | Compute Engine | EC2 and server-management APIs | Azure Virtual Machines | No general-purpose public server provider assumed |
| Storage | Cloud Storage and Google Drive APIs | S3 and supported storage APIs | Azure Blob Storage and OneDrive/SharePoint APIs | iCloud integration only within Apple's supported APIs and terms |
| Web / Website | Search, Maps, Analytics and supported website APIs | API Gateway and website infrastructure APIs | Microsoft Graph and supported web services | Web-facing Apple developer services where available |
| Software / Tools | Google developer and productivity APIs | AWS tools and SDKs | Microsoft developer/productivity APIs | Apple developer tools and official APIs |

This table is an architecture map, not a statement that every listed product is already wired into this repository. Confirm current product availability, API scope, regional eligibility, billing, and terms before implementing an adapter. Do not represent a product as a domain registrar, generic hosting provider, database provider, or payment processor unless its official product/API actually supports that role.

## Canonical provider package paths

- Google: `backend/integrations/providers/google.py` and `backend/api/global_ecosystem/global_api_ecosystem/global_companies_api_ecosystem/global_companies_ecosystem/google`
- AWS: `backend/integrations/providers/aws.py` and `backend/api/global_ecosystem/global_api_ecosystem/global_companies_api_ecosystem/global_companies_ecosystem/aws`
- Microsoft: `backend/integrations/providers/microsoft.py` and `backend/api/global_ecosystem/global_api_ecosystem/global_companies_api_ecosystem/global_companies_ecosystem/microsoft`
- Apple: `backend/integrations/providers/apple.py` and `backend/api/global_ecosystem/global_api_ecosystem/global_companies_api_ecosystem/global_companies_ecosystem/apple`

Related platform packages are under `global_platforms_api_ecosystem/global_platforms_ecosystem/`. Family-specific provider paths listed in the central catalog are references to code areas; they do not prove that a live connector exists.

## Implementation status rules

- `CATALOG_ONLY`: provider is listed for discovery; no working adapter is implied.
- `CONFIGURATION_READINESS_SCAFFOLD`: configuration/readiness scaffolding exists; credentials and live API operations are not thereby verified.
- A provider may be marked live-connected only after secure credential configuration, successful authenticated API calls, error handling, tests, and operational checks.
- Never commit API keys, OAuth client secrets, access tokens, private keys, or customer credentials. Use environment variables or a managed secret store.
- Do not create fake checkout, domain registration, DNS changes, cloud resources, or payment operations. Production actions require provider-specific adapters, authorization, explicit user confirmation, audit logging, and tested rollback/error paths.


## Provider-owned API ecosystems

Each major provider has its own provider-specific folder at this level. These folders index that provider's own company/platform ecosystem, official products, API families and security/integration boundaries. The shared family folders remain separate and reusable; provider-specific API logic belongs in the corresponding adapter and must not be duplicated across families.

- [Google API Ecosystem](global_google_api_ecosystem/README.md) — `global_google_api_ecosystem/google_api_ecosystem.py`
- [AWS API Ecosystem](global_aws_api_ecosystem/README.md) — `global_aws_api_ecosystem/aws_api_ecosystem.py`
- [Microsoft API Ecosystem](global_microsoft_api_ecosystem/README.md) — `global_microsoft_api_ecosystem/microsoft_api_ecosystem.py`
- [Apple API Ecosystem](global_apple_api_ecosystem/README.md) — `global_apple_api_ecosystem/apple_api_ecosystem.py`

These are provider-owned catalog/index modules, not live connectors. The central provider catalog remains the registry for discovery. Other vendors should follow the same provider-owned folder pattern when their API ecosystem is added; only include products and platforms actually offered by that vendor.

## API endpoints

- `GET /api/v1/global-api-ecosystem/status`
- `GET /api/v1/global-api-ecosystem/ecosystems`
- `GET /api/v1/global-api-ecosystem/providers`
- `GET /api/v1/global-api-ecosystem/providers/{provider_id}`
- `GET /api/v1/global-api-ecosystem/ai-providers`

See `docs/GLOBAL_API_ECOSYSTEM_PROVIDER_HIERARCHY.md` for provider hierarchy, status definitions and integration gates.

The runtime `backend/`, master `BACKEND/`, and visual/documentation `🖥️ BACKEND 🖥️/` layers remain separate. Catalog membership alone never means a provider is live-connected.


## Provider ownership + shared category routing (canonical rule)

Every provider has its own provider-owned API ecosystem folder for its own products, platforms, service catalogs, authentication requirements, scopes, rate limits, and adapter status. Provider-owned folders do **not** replace the shared category ecosystems. A provider capability is also indexed in the appropriate shared category folder so cross-provider capabilities can use a common interface.

Examples of the intended routing:

| Provider capability | Provider-owned catalog | Shared category ecosystem |
|---|---|---|
| Google Cloud SQL / Google database services | `global_google_api_ecosystem` | `global_database_api_ecosystem` |
| Amazon RDS / DynamoDB | `global_aws_api_ecosystem` | `global_database_api_ecosystem` |
| Azure SQL / Microsoft database services | `global_microsoft_api_ecosystem` | `global_database_api_ecosystem` |
| Apple app/device-related services | `global_apple_api_ecosystem` | Relevant `APP`, `SYSTEM`, `SECURITY`, or `PLATFORMS` family |
| Google Cloud Storage / Drive | `global_google_api_ecosystem` | `global_storage_api_ecosystem` |
| Amazon S3 / EBS | `global_aws_api_ecosystem` | `global_storage_api_ecosystem` |
| Azure Blob Storage / OneDrive | `global_microsoft_api_ecosystem` | `global_storage_api_ecosystem` |
| Google Cloud compute / AWS EC2 / Azure compute | Provider's own folder | `global_server_api_ecosystem` and/or `global_cloud_api_ecosystem` |

The registry's `list_provider_category_routes(provider_id=None)` returns the provider-to-category path index; pass a provider ID (for example `google`, `aws`, `microsoft`, or `apple`) to get only that provider's routes. `list_provider_ecosystems(family="DATABASE")` lists providers registered for the database family.

**Important:** route/catalog presence is not proof that a product API is enabled or connected. Actual access requires the provider's official API, correct credentials/scopes, an implemented adapter, and passing integration tests. Never store secrets in this repository.

## GLOBAL ADULT INDUSTRY ECOSYSTEM

The adult-industry catalog is maintained separately at `global_adult_industry_api_ecosystem/`. It starts with AbeloHost, ViceTemple, FapHouse, Pornhub, and Naughty America as catalog-only provider records and groups relevant hosting, video/platform and website families. The initial owner-authenticated catalog endpoints are `GET /api/v1/global-adult-industry-ecosystem/status` and `GET /api/v1/global-adult-industry-ecosystem/providers`. These endpoints report catalog data only; no provider API connectivity is implied. Expand the directory only with verified provider identities and official API/partner documentation, while respecting adult-only access, consent, privacy, licensing, and local law.
