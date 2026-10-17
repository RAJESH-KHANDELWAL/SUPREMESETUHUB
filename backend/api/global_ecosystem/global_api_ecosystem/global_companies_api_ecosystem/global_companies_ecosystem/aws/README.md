# AWS API ECOSYSTEM

Canonical AWS company-specific API ecosystem package under GLOBAL COMPANIES API ECOSYSTEM.

- Parent provider catalog: `backend/api/global_api_ecosystem_catalog.py`
- Shared readiness adapter: `backend/integrations/providers/aws.py`
- Related existing platform package: AWS Console under GLOBAL PLATFORMS API ECOSYSTEM.

Prefer workload roles or web identity with least-privilege policies. The shared adapter checks configuration presence only; it does not verify AWS identity, S3 permissions or any live AWS API operation. Add non-destructive live checks and recovery tests before enabling production workflows.
