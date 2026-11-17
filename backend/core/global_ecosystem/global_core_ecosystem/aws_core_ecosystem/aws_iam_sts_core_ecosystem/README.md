# AWS IAM and STS Core Ecosystem

Provider: Amazon Web Services  
Core parent: AWS-CORE-ECOSYSTEM  
API boundary: `backend/api/global_ecosystem/global_api_ecosystem/aws_api_ecosystem/aws_iam_sts_api_ecosystem/`

This package owns AWS IAM and STS service identity, capability metadata, lifecycle and policy boundaries. It does not resolve credentials, sign AWS requests, invoke SDK clients, call AWS APIs, persist resources or execute jobs.

## Registered Core capabilities
- `IAM_IDENTITY_METADATA`
- `ROLE_AND_POLICY_METADATA`
- `TRUST_RELATIONSHIP_METADATA`
- `TEMPORARY_CREDENTIALS_BOUNDARY`
- `IDENTITY_GOVERNANCE_METADATA`

## Security
Use the actual AWS account, region, principal, resource ARN and IAM policy at the API/application layer. Elevated or destructive operations require explicit authorization and audit.

Readiness: `CORE_CATALOG_ONLY`  
API availability: unverified  
Live connection: not verified
