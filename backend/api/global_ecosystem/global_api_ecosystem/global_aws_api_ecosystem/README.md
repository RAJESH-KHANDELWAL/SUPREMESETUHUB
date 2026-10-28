# AWS API ECOSYSTEM

This is the provider-owned Amazon Web Services ecosystem within GLOBAL API ECOSYSTEM. It groups AWS identity, console, official products, developer APIs and service families under one AWS-specific boundary.

## AWS-owned / AWS-operated areas
- **Platforms:** AWS Management Console, AWS Marketplace, AWS Organizations, AWS IAM Identity Center and AWS developer tooling.
- **API families:** AWS SDKs, service APIs, STS/IAM, CloudFormation, CloudWatch, billing/cost APIs, API Gateway and service-specific control planes.
- **Compute and hosting:** EC2, Lightsail, Lambda, ECS/EKS, Elastic Beanstalk and supported application hosting services.
- **Storage and database:** S3, EBS, EFS, RDS, DynamoDB, ElastiCache and supported backup APIs.
- **Networking and domain:** VPC, Route 53 DNS and Route 53 Domains where registration is available for the account/TLD.
- **Security and operations:** IAM, KMS, Secrets Manager, CloudTrail, Config, GuardDuty and monitoring APIs.
- **AI and data:** Bedrock, SageMaker and applicable analytics/data services.

## Integration rules
1. This is a catalog/architecture boundary, not proof of live connectivity.
2. Use least-privilege IAM roles/policies and temporary credentials where possible.
3. Keep access keys and secrets outside Git; use environment variables or managed secret storage.
4. Provisioning, DNS updates, domain purchases and billing actions require explicit authorization, idempotency, audit logging and tested error handling.
5. Check the target service, account permissions, region, quota and product eligibility before enabling an operation.

## Canonical cross-links
- Provider adapter: `backend/integrations/providers/aws.py`
- Central registry: `backend/api/global_api_ecosystem_catalog.py`
- Related platform index: `../global_platforms_api_ecosystem/`
- Related families: AI, Cloud, Database, Developer, Domain, Hosting, Security, Server, Storage, Web and Website.
