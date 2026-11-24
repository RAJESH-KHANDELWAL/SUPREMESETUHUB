# AWS CORE ECOSYSTEM

**Provider:** Amazon Web Services (AWS)  
**Parent:** GLOBAL CORE ECOSYSTEM  
**API catalog:** `backend/api/global_ecosystem/global_api_ecosystem/aws_api_ecosystem/`

## Purpose
AWS Core is the provider-owned, metadata-first control plane for the 16 AWS service families already registered in this repository. It owns canonical service identity, account/tenant context contracts, domain classification, capability metadata, policy boundaries, readiness and cross-family discovery.

## Canonical root architecture (Google Core aligned)
- `manager.py`: canonical `AwsCoreManager` and `get_manager()`.
- `manager.php`: PHP interoperability facade over the AWS Core contract.
- `catalog.py`: provider and 16-family registry.
- `contracts.py`: AWS account context, credential references, readiness and result contracts.
- `policy.py`: capability classification, account-context validation and safe summaries.
- `module_service.py`: shared read-only service-family manager.
- `product_catalog.py`: 16 service-family offering inventory.
- `domain_catalog.py`: 13 AWS-specific domains and family mapping.
- `domain_runtime.py`: shared read-only domain manager.
- `orchestrator.py`: health, product, domain, offering and dependency discovery.
- `service.py`: provider-level status facade.
- `product_ecosystem_index.json`: machine-readable family/domain package map.
- `test_google_core_alignment.py`: structural and behavior tests.

## Service-family packages
- `aws_api_gateway_core_ecosystem` — `AwsApiGatewayCoreService`
- `aws_bedrock_sagemaker_core_ecosystem` — `AwsBedrockSagemakerCoreService`
- `aws_billing_cost_core_ecosystem` — `AwsBillingCostCoreService`
- `aws_cloudformation_core_ecosystem` — `AwsCloudformationCoreService`
- `aws_cloudtrail_core_ecosystem` — `AwsCloudtrailCoreService`
- `aws_cloudwatch_core_ecosystem` — `AwsCloudwatchCoreService`
- `aws_containers_core_ecosystem` — `AwsContainersCoreService`
- `aws_database_core_ecosystem` — `AwsDatabaseCoreService`
- `aws_ec2_compute_core_ecosystem` — `AwsEc2ComputeCoreService`
- `aws_iam_sts_core_ecosystem` — `AwsIamStsCoreService`
- `aws_kms_secrets_core_ecosystem` — `AwsKmsSecretsCoreService`
- `aws_lambda_core_ecosystem` — `AwsLambdaCoreService`
- `aws_lightsail_core_ecosystem` — `AwsLightsailCoreService`
- `aws_route53_dns_core_ecosystem` — `AwsRoute53DnsCoreService`
- `aws_s3_storage_core_ecosystem` — `AwsS3StorageCoreService`
- `aws_vpc_networking_core_ecosystem` — `AwsVpcNetworkingCoreService`

Each family keeps its AWS-specific manifest, config, service, contracts, capabilities, lifecycle, security and ten standard subfolders. Family managers delegate to the existing family service; no duplicate API implementation is introduced.

## Domain packages
- `aws_application_integration_and_api_management_core_ecosystem` — Application Integration and API Management
- `aws_ai_ml_and_intelligence_core_ecosystem` — AI, Machine Learning and Intelligence
- `aws_billing_cost_and_governance_core_ecosystem` — Billing, Cost and Governance
- `aws_compute_and_containers_core_ecosystem` — Compute and Containers
- `aws_database_and_data_services_core_ecosystem` — Database and Data Services
- `aws_domain_and_name_services_core_ecosystem` — Domain and Name Services
- `aws_infrastructure_provisioning_and_automation_core_ecosystem` — Infrastructure Provisioning and Automation
- `aws_networking_and_edge_core_ecosystem` — Networking and Edge
- `aws_observability_and_audit_core_ecosystem` — Observability and Audit
- `aws_organization_and_governance_core_ecosystem` — Organization and Governance
- `aws_security_and_identity_core_ecosystem` — Security and Identity
- `aws_storage_and_data_management_core_ecosystem` — Storage and Data Management
- `aws_developer_and_application_platform_core_ecosystem` — Developer and Application Platform

## Shared packages
- `aws_shared_compatibility_core_ecosystem`
- `aws_shared_configuration_core_ecosystem`
- `aws_shared_contracts_core_ecosystem`
- `aws_shared_documentation_core_ecosystem`
- `aws_shared_events_core_ecosystem`
- `aws_shared_exceptions_core_ecosystem`
- `aws_shared_orchestration_core_ecosystem`
- `aws_shared_security_core_ecosystem`
- `aws_shared_testing_core_ecosystem`
- `aws_shared_utilities_core_ecosystem`
- `aws_shared_validation_core_ecosystem`

## Layer boundaries
| Layer | Owns |
|---|---|
| AWS Core | Provider/service identity, taxonomy, capability metadata, policy, lifecycle, readiness and discovery |
| AWS API Ecosystem | SDK clients, SigV4 signing, IAM role/web identity resolution, API transport and response normalization |
| Integrations | Provider adapter registration and environment readiness |
| Storage / Database | Durable state, resource snapshots, schemas, transactions and retention |
| Runtime / Engine | Jobs, retries, queues, scheduling and execution |
| Application / UI | User sessions, tenant authorization, consent, approvals and workflows |

Core does not authenticate to AWS, resolve credentials, sign requests, call AWS endpoints, persist cloud state, launch jobs or mutate infrastructure.

## Security and readiness
Prefer IAM roles, workload identity federation and short-lived credentials. Never store raw AWS keys, session tokens or private keys in Core. Opaque credential references and trusted tenant/account context only. Least-privilege IAM and resource ownership checks remain mandatory in the API/application layers. Elevated, destructive, write, deploy, rotation, revocation and spend-affecting operations require explicit approval and audit. Core capability metadata is not an IAM grant.

All 16 families remain `CORE_CATALOG_ONLY`; API availability is unverified (`null`), live connections verified: 0, credentials stored: 0, AWS API calls performed by Core: 0. These are metadata/control-plane claims only, not proof of account authorization or production connectivity.
