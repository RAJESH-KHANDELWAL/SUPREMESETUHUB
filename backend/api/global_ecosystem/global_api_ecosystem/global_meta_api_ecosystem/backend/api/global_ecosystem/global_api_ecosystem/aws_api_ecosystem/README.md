# AWS API ECOSYSTEM

Canonical provider root for Amazon Web Services APIs and cloud services in SUPREMESETUHUB.

## Provider structure

- `aws_api_ecosystem.py` — provider registry, API-family metadata and safe catalog listing.
- Each `aws_*_api_ecosystem/` child directory owns its AWS service-family catalog and future adapter boundary.
- Shared provider readiness adapter: `backend/integrations/providers/aws.py`.
- Shared integration registration: `backend/integrations/registry.py`.

## AWS API family tree

- **AWS IAM AND STS API ECOSYSTEM** — `aws_iam_sts_api_ecosystem/` — Identity, access management, roles, policies, temporary credentials and security token operations.
- **AWS EC2 COMPUTE API ECOSYSTEM** — `aws_ec2_compute_api_ecosystem/` — EC2 instances, images, volumes, snapshots and compute lifecycle operations.
- **AWS LIGHTSAIL API ECOSYSTEM** — `aws_lightsail_api_ecosystem/` — Lightsail instances, containers, databases, networking and snapshots.
- **AWS LAMBDA API ECOSYSTEM** — `aws_lambda_api_ecosystem/` — Lambda functions, versions, aliases, invocation and event source mappings.
- **AWS CONTAINERS API ECOSYSTEM** — `aws_containers_api_ecosystem/` — ECS, EKS, ECR and supported container orchestration services.
- **AWS S3 STORAGE API ECOSYSTEM** — `aws_s3_storage_api_ecosystem/` — S3 buckets, objects, lifecycle, encryption, access policies and storage controls.
- **AWS DATABASE API ECOSYSTEM** — `aws_database_api_ecosystem/` — RDS, Aurora, DynamoDB and database control-plane APIs.
- **AWS ROUTE 53 DNS API ECOSYSTEM** — `aws_route53_dns_api_ecosystem/` — Route 53 hosted zones, records, health checks and DNS routing policies.
- **AWS VPC NETWORKING API ECOSYSTEM** — `aws_vpc_networking_api_ecosystem/` — VPCs, subnets, route tables, gateways, security groups and network interfaces.
- **AWS CLOUDWATCH API ECOSYSTEM** — `aws_cloudwatch_api_ecosystem/` — Metrics, alarms, dashboards, logs and observability APIs.
- **AWS CLOUDTRAIL API ECOSYSTEM** — `aws_cloudtrail_api_ecosystem/` — Audit trails, event history, event selectors and governance integrations.
- **AWS KMS AND SECRETS API ECOSYSTEM** — `aws_kms_secrets_api_ecosystem/` — KMS keys, cryptographic operations, Secrets Manager and secure parameter storage.
- **AWS BEDROCK AND SAGEMAKER API ECOSYSTEM** — `aws_bedrock_sagemaker_api_ecosystem/` — Amazon Bedrock foundation-model services and SageMaker AI/ML platform APIs.
- **AWS BILLING AND COST API ECOSYSTEM** — `aws_billing_cost_api_ecosystem/` — Billing, Cost Explorer, budgets, usage and cost allocation APIs.
- **AWS API GATEWAY ECOSYSTEM** — `aws_api_gateway_ecosystem/` — API Gateway REST, HTTP and WebSocket APIs, stages, deployments and authorizers.
- **AWS CLOUDFORMATION API ECOSYSTEM** — `aws_cloudformation_api_ecosystem/` — CloudFormation stacks, change sets, templates and infrastructure provisioning.

## Authentication and setup

Prefer IAM roles, workload identity federation or web identity credentials over long-lived access keys. Configure the AWS region and the minimum required identity configuration in the deployment environment or managed secret store:

- `AWS_REGION`
- IAM role / web identity configuration where supported; or
- `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` only when role-based credentials are not available.

Never commit credentials, expose them in browser code, include them in URLs, or write them to logs.

## Security and operational requirements

- Apply least-privilege IAM policies and scope permissions to the exact service actions and resources.
- Keep credentials server-side and use short-lived role credentials wherever possible.
- Enforce tenant/user authorization before performing cloud operations.
- Add request timeouts, bounded retries, rate limits, audit logs and cost controls.
- Require explicit confirmation for destructive infrastructure actions.
- Separate read-only discovery from create, update and delete permissions.
- Validate region, account identity, resource ownership and service availability before execution.

## Status semantics

`NEEDS_CONFIGURATION` means required environment settings are absent.
`CONFIGURED_NOT_VERIFIED` means settings are present, not that AWS authentication or a service operation succeeded.
Catalog presence does not imply that a service adapter is implemented or connected. Only successful deployment-level credential validation and service-specific smoke tests may mark a connection verified.

## Non-duplication rule

AWS-owned services remain canonical under this provider root. Global AI, Cloud, Database, Security, Storage, Server and Developer ecosystems should link to these canonical AWS service catalogs rather than copy their implementations.
