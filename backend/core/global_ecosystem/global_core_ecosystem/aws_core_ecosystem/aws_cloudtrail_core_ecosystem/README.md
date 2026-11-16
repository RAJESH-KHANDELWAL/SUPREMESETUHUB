# AWS CloudTrail Core Ecosystem

Provider: Amazon Web Services  
Core parent: AWS-CORE-ECOSYSTEM  
API boundary: `backend/api/global_ecosystem/global_api_ecosystem/aws_api_ecosystem/aws_cloudtrail_api_ecosystem/`

This package owns AWS CloudTrail service identity, capability metadata, lifecycle and policy boundaries. It does not resolve credentials, sign AWS requests, invoke SDK clients, call AWS APIs, persist resources or execute jobs.

## Registered Core capabilities
- `AUDIT_TRAIL_METADATA`
- `EVENT_HISTORY_QUERY_BOUNDARY`
- `EVENT_SELECTOR_METADATA`
- `GOVERNANCE_EVIDENCE_METADATA`

## Security
Use the actual AWS account, region, principal, resource ARN and IAM policy at the API/application layer. Elevated or destructive operations require explicit authorization and audit.

Readiness: `CORE_CATALOG_ONLY`  
API availability: unverified  
Live connection: not verified
