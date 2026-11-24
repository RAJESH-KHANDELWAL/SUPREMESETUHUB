# IBM API ECOSYSTEM

Canonical provider root for IBM-owned enterprise, AI, cloud and infrastructure APIs in SUPREMESETUHUB.

## Provider structure

- `ibm_api_ecosystem.py` — provider registry metadata, family inventory and safe catalog listing.
- Each `ibm_*_api_ecosystem/` child directory owns its IBM service-family catalog and future adapter boundary.
- Shared provider readiness adapter: `backend/integrations/providers/ibm.py`.
- Shared integration registration: `backend/integrations/registry.py`.
- IBM company profile discovery is maintained separately under the Companies ecosystem.
- IBM hosting and VPS cross-references remain in the shared Hosting/VPS category ecosystems.

## IBM API family tree

- **IBM CLOUD PLATFORM API ECOSYSTEM** — `ibm_cloud_platform_api_ecosystem/` — IBM Cloud platform services, account context, regions, resource groups, service instances and platform lifecycle APIs.
- **IBM IAM AND IDENTITY API ECOSYSTEM** — `ibm_iam_identity_api_ecosystem/` — IBM Cloud IAM users, service IDs, API keys, trusted profiles, access groups, policies and authorization.
- **IBM WATSONX AI API ECOSYSTEM** — `ibm_watsonx_ai_api_ecosystem/` — watsonx.ai foundation-model inference, model deployments, prompt assets and supported AI lifecycle APIs.
- **IBM WATSONX DATA API ECOSYSTEM** — `ibm_watsonx_data_api_ecosystem/` — watsonx.data service instances, engines, catalogs and supported data operations.
- **IBM DB2 DATABASE API ECOSYSTEM** — `ibm_db2_database_api_ecosystem/` — Db2 database services, instance management, SQL access and supported administrative APIs.
- **IBM CLOUDANT API ECOSYSTEM** — `ibm_cloudant_api_ecosystem/` — Cloudant databases, documents, indexes, replication and account-level operations.
- **IBM CLOUD OBJECT STORAGE API ECOSYSTEM** — `ibm_cloud_object_storage_api_ecosystem/` — IBM Cloud Object Storage buckets, objects, multipart operations, lifecycle and access configuration.
- **IBM VPC COMPUTE AND NETWORKING API ECOSYSTEM** — `ibm_vpc_compute_networking_api_ecosystem/` — Virtual server instances, images, volumes, subnets, VPCs, security groups, gateways and network interfaces.
- **IBM KUBERNETES AND CONTAINERS API ECOSYSTEM** — `ibm_kubernetes_containers_api_ecosystem/` — IBM Cloud Kubernetes Service, Red Hat OpenShift on IBM Cloud and container registry management boundaries.
- **IBM CODE ENGINE AND SERVERLESS API ECOSYSTEM** — `ibm_code_engine_serverless_api_ecosystem/` — Code Engine projects, applications, jobs, builds and supported serverless workload operations.
- **IBM API CONNECT AND GATEWAY API ECOSYSTEM** — `ibm_api_connect_gateway_api_ecosystem/` — API Connect management, catalogs, spaces, products, APIs and gateway administration where licensed and enabled.
- **IBM SECURITY AND KEY PROTECT API ECOSYSTEM** — `ibm_security_key_protect_api_ecosystem/` — Key Protect key lifecycle, cryptographic operations, security posture and supported security-service APIs.
- **IBM SECRETS MANAGER API ECOSYSTEM** — `ibm_secrets_manager_api_ecosystem/` — Secrets Manager instances, secret groups, secret lifecycle, rotation and retrieval controls.
- **IBM MONITORING AND ACTIVITY TRACKER API ECOSYSTEM** — `ibm_monitoring_activity_tracker_api_ecosystem/` — Monitoring metrics, alerting, dashboards, Activity Tracker events and operational audit integrations.
- **IBM RESOURCE CONTROLLER AND CATALOG API ECOSYSTEM** — `ibm_resource_controller_catalog_api_ecosystem/` — Resource Controller, Global Catalog, service instances, plans, resource bindings and account inventory.
- **IBM BILLING USAGE AND COST API ECOSYSTEM** — `ibm_billing_usage_cost_api_ecosystem/` — Usage records, billing reports, cost and consumption data where available to the account.

## Authentication and setup

IBM APIs do not use one universal credential for every product. For IBM Cloud APIs, the common pattern is an IBM Cloud IAM API key exchanged for a short-lived IAM bearer token; individual services may require additional instance identifiers, endpoints, HMAC credentials, product entitlements or service-specific authorization.

Configure server-side deployment secrets only:

- `IBM_CLOUD_API_KEY` — IBM Cloud IAM API key for the configured account/service access.
- `IBM_CLOUD_REGION` — default IBM Cloud region where a regional service endpoint is required.
- `IBM_CLOUD_ACCOUNT_ID` — optional account context when required by a specific operation.
- `IBM_CLOUD_RESOURCE_GROUP_ID` — optional resource-group context for scoped operations.

Do not add service-specific secrets to source control. Use workload identity or short-lived credentials where supported. Never expose API keys, bearer tokens, HMAC secrets or secret values to browser code or logs.

## Security and operational requirements

- Apply least-privilege IAM policies and service-specific roles.
- Enforce tenant, account, project, region and resource authorization on every operation.
- Validate service endpoint and region before requests.
- Add request timeouts, bounded retries, rate-limit handling, audit logs and secret rotation.
- Separate read-only discovery from create/update/delete operations.
- Require explicit confirmation for destructive infrastructure, identity, key or secret operations.
- Do not assume a service is available in every account, plan or region.

## Shared integration adapter

The shared adapter at `backend/integrations/providers/ibm.py` reports configuration readiness only. It does not exchange IAM keys for tokens, validate credentials with IBM, or make a live service API request.

## Status semantics

- `NEEDS_CONFIGURATION`: required environment settings are absent.
- `CONFIGURED_NOT_VERIFIED`: required settings are present; no successful IBM API operation is implied.
- `CONNECTED`: may be reported only after authenticated IBM IAM validation and a service-specific API smoke test succeed.

Child folders are catalog/documentation boundaries, not completed live connectors. Implement and test each IBM API family independently against current official documentation and account entitlements.

## Official references

- IBM: https://www.ibm.com/
- IBM Cloud: https://www.ibm.com/cloud
- IBM Documentation: https://www.ibm.com/docs/
- IBM Cloud API documentation: https://cloud.ibm.com/apidocs
