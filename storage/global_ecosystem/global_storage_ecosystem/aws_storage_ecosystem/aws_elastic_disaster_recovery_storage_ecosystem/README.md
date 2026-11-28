# AWS_ELASTIC_DISASTER_RECOVERY_STORAGE_ECOSYSTEM

- **Folder:** `aws_elastic_disaster_recovery_storage_ecosystem/`
- **Category:** ELASTIC_DISASTER_RECOVERY
- **Group:** BACKUP_AND_RECOVERY
- **Provider:** AWS
- **Service namespace:** AWS Elastic Disaster Recovery
- **State:** Category foundation scaffold; external connection is not configured.

## Responsibility
Disaster recovery source server, replication, recovery launch and failback metadata.

## Package contents
- `__init__.py` — package exports
- `ecosystem_config.py` — runtime configuration boundary
- `ecosystem_manifest.json` — category identity and readiness metadata
- `ecosystem_models.py` — category metadata model
- `ecosystem_service.py` — description and health-state contract
- `service.py` — category service boundary
- `api/routes.py` — framework-neutral read-only catalog handler
- `models/record.py` — metadata record
- `schemas/manifest.schema.json` — manifest schema
- `php/aws_elastic_disaster_recovery_storage_ecosystem.php` — PHP metadata reader
- `tests/test_foundation.py` — offline scaffold tests

## Safety and integration boundary
This folder is a storage category namespace, not proof of a live AWS service connection or entitlement. Do not mark it connected until the applicable AWS API, region/service availability, IAM permissions, authorized credentials, provider-specific health checks and end-to-end tests are verified. No upload, download, delete, backup, restore or replication operation is enabled by this scaffold. Never commit credentials or personal data.
