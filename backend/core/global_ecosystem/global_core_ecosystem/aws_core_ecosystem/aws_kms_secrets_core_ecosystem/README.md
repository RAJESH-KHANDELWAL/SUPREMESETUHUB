# AWS KMS and Secrets Manager Core Ecosystem

Provider: Amazon Web Services  
Core parent: AWS-CORE-ECOSYSTEM  
API boundary: `backend/api/global_ecosystem/global_api_ecosystem/aws_api_ecosystem/aws_kms_secrets_api_ecosystem/`

This package owns AWS KMS and Secrets Manager service identity, capability metadata, lifecycle and policy boundaries. It does not resolve credentials, sign AWS requests, invoke SDK clients, call AWS APIs, persist resources or execute jobs.

## Registered Core capabilities
- `KMS_KEY_METADATA`
- `CRYPTOGRAPHIC_OPERATION_POLICY_BOUNDARY`
- `SECRETS_METADATA`
- `SECRET_ROTATION_POLICY_METADATA`
- `SECURE_PARAMETER_REFERENCE`

## Security
Use the actual AWS account, region, principal, resource ARN and IAM policy at the API/application layer. Elevated or destructive operations require explicit authorization and audit.

Readiness: `CORE_CATALOG_ONLY`  
API availability: unverified  
Live connection: not verified
