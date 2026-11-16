# AWS CORE ECOSYSTEM

**Provider:** Amazon Web Services (AWS)  
**Parent:** GLOBAL CORE ECOSYSTEM  
**API catalog:** `backend/api/global_ecosystem/global_api_ecosystem/aws_api_ecosystem/`

## Purpose
The AWS Core is the provider-owned, metadata-first control plane for the 16 AWS service families already defined by the repository's AWS API Ecosystem. It provides canonical service identity, family/domain classification, capability metadata, tenant and account context contracts, policy boundaries, lifecycle/readiness metadata and cross-family discovery.

## Product-family coverage
- **API Gateway** — `aws_api_gateway_core_ecosystem/` → `aws_api_gateway_ecosystem/`
- **Bedrock and SageMaker AI** — `aws_bedrock_sagemaker_core_ecosystem/` → `aws_bedrock_sagemaker_api_ecosystem/`
- **Billing and Cost Management** — `aws_billing_cost_core_ecosystem/` → `aws_billing_cost_api_ecosystem/`
- **CloudFormation** — `aws_cloudformation_core_ecosystem/` → `aws_cloudformation_api_ecosystem/`
- **CloudTrail** — `aws_cloudtrail_core_ecosystem/` → `aws_cloudtrail_api_ecosystem/`
- **CloudWatch** — `aws_cloudwatch_core_ecosystem/` → `aws_cloudwatch_api_ecosystem/`
- **Containers (ECS, EKS and ECR)** — `aws_containers_core_ecosystem/` → `aws_containers_api_ecosystem/`
- **Database (RDS, Aurora and DynamoDB)** — `aws_database_core_ecosystem/` → `aws_database_api_ecosystem/`
- **EC2 Compute** — `aws_ec2_compute_core_ecosystem/` → `aws_ec2_compute_api_ecosystem/`
- **IAM and STS** — `aws_iam_sts_core_ecosystem/` → `aws_iam_sts_api_ecosystem/`
- **KMS and Secrets Manager** — `aws_kms_secrets_core_ecosystem/` → `aws_kms_secrets_api_ecosystem/`
- **Lambda** — `aws_lambda_core_ecosystem/` → `aws_lambda_api_ecosystem/`
- **Lightsail** — `aws_lightsail_core_ecosystem/` → `aws_lightsail_api_ecosystem/`
- **Route 53 DNS** — `aws_route53_dns_core_ecosystem/` → `aws_route53_dns_api_ecosystem/`
- **S3 Storage** — `aws_s3_storage_core_ecosystem/` → `aws_s3_storage_api_ecosystem/`
- **VPC Networking** — `aws_vpc_networking_core_ecosystem/` → `aws_vpc_networking_api_ecosystem/`

## Layer boundaries
| Layer | Owns |
|---|---|
| AWS Core | Catalogs, service identity, capability taxonomy, policy metadata, lifecycle and discovery |
| AWS API Ecosystem | AWS SDK clients, SigV4 signing, IAM role/web identity resolution, API transport and response normalization |
| Integrations | Provider adapter registration and environment readiness |
| Storage / Database | Durable state, resource snapshots, schemas, transactions and retention |
| Runtime / Engine | Jobs, retries, queues, scheduling and orchestration execution |
| Application / UI | User sessions, tenant authorization, consent, approval and workflows |

Core does not authenticate to AWS, resolve credentials, sign requests, call AWS endpoints, persist cloud state, launch jobs or perform infrastructure mutations.

## Security model
- Prefer IAM roles, workload identity federation and short-lived credentials.
- Never store AWS access keys, secret keys, session tokens or private keys in Core.
- Core accepts opaque references and trusted tenant/account context; the API layer resolves credentials.
- Apply least-privilege IAM policies and tenant/resource ownership checks in the API/application layers.
- Classify IAM, KMS, Secrets Manager, networking, destructive infrastructure and billing actions as elevated operations.
- Require explicit approval and audit for create, update, delete, deploy, rotate, revoke and spend-affecting operations.
- Do not treat a Core capability declaration as an AWS IAM permission grant.

## Readiness semantics
All 16 families are registered as `CORE_CATALOG_ONLY`. API availability is unverified (`null`) and live AWS connections verified by this Core implementation are zero. The repository's AWS API README describes provider adapters and some scaffold statuses; this Core registration does not upgrade those statuses or prove that credentials, account access, regions, service entitlements or operations work.

## Google Core alignment
The package follows the shared Google Core architecture: provider catalog, contracts, policy, module service, product and domain catalogs, orchestrator, facade service, PHP contract, tests, product-family packages and shared support directories. AWS capabilities remain AWS-specific; Google product counts or product semantics are not copied.


## AWS account context contract

Every service-family operation must be evaluated against the 12-digit AWS account ID, AWS region, tenant ID, actor ID, effective IAM principal and resource-level policy. The Core context validator only checks required metadata shape; the API layer must independently validate the real caller identity and AWS authorization before invoking an SDK operation.
