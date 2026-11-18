# AWS Database (RDS, Aurora and DynamoDB) Core Ecosystem

Provider: Amazon Web Services  
Core parent: AWS-CORE-ECOSYSTEM  
API boundary: `backend/api/global_ecosystem/global_api_ecosystem/aws_api_ecosystem/aws_database_api_ecosystem/`

This package owns AWS Database (RDS, Aurora and DynamoDB) service identity, capability metadata, lifecycle and policy boundaries. It does not resolve credentials, sign AWS requests, invoke SDK clients, call AWS APIs, persist resources or execute jobs.

## Registered Core capabilities
- `RDS_INSTANCE_METADATA`
- `AURORA_CLUSTER_METADATA`
- `DYNAMODB_TABLE_METADATA`
- `BACKUP_AND_RESTORE_POLICY_METADATA`
- `DATABASE_LIFECYCLE_BOUNDARY`

## Security
Use the actual AWS account, region, principal, resource ARN and IAM policy at the API/application layer. Elevated or destructive operations require explicit authorization and audit.

Readiness: `CORE_CATALOG_ONLY`  
API availability: unverified  
Live connection: not verified
