# AWS CLOUDWATCH API ECOSYSTEM

Canonical AWS service-family catalog under `aws_api_ecosystem/`.

## Scope

Metrics, alarms, dashboards, logs and observability APIs.

## Implementation contract

- Keep AWS-owned API definitions and service metadata in this child ecosystem.
- Use the shared AWS provider adapter at `backend/integrations/providers/aws.py` for provider readiness.
- Use IAM least privilege, short-lived credentials and tenant-scoped authorization.
- Keep credentials in the deployment secret manager; never commit keys or tokens.
- Add service-specific schemas, request validation, audit logging, timeouts, quotas and tests before enabling operations.
- Require explicit authorization and confirmation for infrastructure changes or destructive operations.

## Status

Catalog scaffold only. This README does not claim that a live AWS service connection or executable service adapter exists. Mark a service connected only after deployment-level authentication and service-specific smoke tests pass.
