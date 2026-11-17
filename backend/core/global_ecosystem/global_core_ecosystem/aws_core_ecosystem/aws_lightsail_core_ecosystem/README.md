# AWS Lightsail Core Ecosystem

Provider: Amazon Web Services  
Core parent: AWS-CORE-ECOSYSTEM  
API boundary: `backend/api/global_ecosystem/global_api_ecosystem/aws_api_ecosystem/aws_lightsail_api_ecosystem/`

This package owns AWS Lightsail service identity, capability metadata, lifecycle and policy boundaries. It does not resolve credentials, sign AWS requests, invoke SDK clients, call AWS APIs, persist resources or execute jobs.

## Registered Core capabilities
- `INSTANCE_METADATA`
- `CONTAINER_SERVICE_METADATA`
- `MANAGED_DATABASE_METADATA`
- `LIGHTSAIL_NETWORKING_METADATA`
- `SNAPSHOT_LIFECYCLE_BOUNDARY`

## Security
Use the actual AWS account, region, principal, resource ARN and IAM policy at the API/application layer. Elevated or destructive operations require explicit authorization and audit.

Readiness: `CORE_CATALOG_ONLY`  
API availability: unverified  
Live connection: not verified
