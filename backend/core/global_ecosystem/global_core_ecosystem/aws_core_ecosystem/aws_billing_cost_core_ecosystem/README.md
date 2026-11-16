# AWS Billing and Cost Management Core Ecosystem

Provider: Amazon Web Services  
Core parent: AWS-CORE-ECOSYSTEM  
API boundary: `backend/api/global_ecosystem/global_api_ecosystem/aws_api_ecosystem/aws_billing_cost_api_ecosystem/`

This package owns AWS Billing and Cost Management service identity, capability metadata, lifecycle and policy boundaries. It does not resolve credentials, sign AWS requests, invoke SDK clients, call AWS APIs, persist resources or execute jobs.

## Registered Core capabilities
- `BILLING_ACCOUNT_METADATA`
- `COST_EXPLORER_QUERY_METADATA`
- `BUDGET_POLICY_METADATA`
- `COST_ALLOCATION_TAG_METADATA`
- `USAGE_REPORTING_BOUNDARY`

## Security
Use the actual AWS account, region, principal, resource ARN and IAM policy at the API/application layer. Elevated or destructive operations require explicit authorization and audit.

Readiness: `CORE_CATALOG_ONLY`  
API availability: unverified  
Live connection: not verified
