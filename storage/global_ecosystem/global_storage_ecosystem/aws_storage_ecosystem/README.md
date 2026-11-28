# AWS Storage Ecosystem

Parent namespace for 11 AWS storage-service category packages. The hierarchy follows the category-package pattern used by GOOGLE Storage Ecosystem while keeping AWS-specific service boundaries.

## Canonical catalog
- `taxonomy/aws_storage_taxonomy.json` — canonical service taxonomy grouped by storage responsibility.
- `category_index.json` — category folder names and paths.
- Each category package contains a README, manifest, Python package scaffold, API boundary, model/schema placeholders, PHP metadata reader and offline test scaffold.

## Categories
- `aws_s3_storage_ecosystem/` — Amazon S3: Object storage namespace covering buckets, objects, versioning, lifecycle, replication and S3 storage classes.
- `aws_ebs_storage_ecosystem/` — Amazon EBS: Block storage volumes, snapshots, volume lifecycle and attachment metadata for compute workloads.
- `aws_efs_storage_ecosystem/` — Amazon EFS: Elastic shared file storage namespace, file systems, mount targets and access-point metadata.
- `aws_fsx_storage_ecosystem/` — Amazon FSx: Managed file-system families, deployment options, backup metadata and lifecycle classification.
- `aws_backup_storage_ecosystem/` — AWS Backup: Backup plans, protected resources, recovery points, vault metadata and restore lifecycle.
- `aws_storage_gateway_storage_ecosystem/` — AWS Storage Gateway: Hybrid cloud storage gateway namespace for file, volume and tape gateway metadata.
- `aws_datasync_storage_ecosystem/` — AWS DataSync: Managed data movement task metadata, source and destination references, schedules and transfer status.
- `aws_transfer_family_storage_ecosystem/` — AWS Transfer Family: Managed SFTP, FTPS, FTP and AS2 transfer endpoint and workflow metadata.
- `aws_snow_family_storage_ecosystem/` — AWS Snow Family: Offline and edge data transfer device/job metadata, shipment lifecycle and import/export classification.
- `aws_elastic_disaster_recovery_storage_ecosystem/` — AWS Elastic Disaster Recovery: Disaster recovery source server, replication, recovery launch and failback metadata.
- `aws_outposts_storage_ecosystem/` — AWS Outposts: On-premises AWS infrastructure storage placement and local capacity metadata.

## Architecture and responsibility
This package owns AWS storage-side taxonomy, identity, metadata, lifecycle classification and readiness declarations. Provider API clients, authentication, secret handling and external operations belong in their designated API/integration layers. The taxonomy does not claim that every category has a separately exposed AWS API.

## Readiness boundary
All categories are scaffolds and remain `NOT_CONFIGURED`. No live provider connection, upload, download, delete, replication, backup or restore operation is enabled. Enable a capability only after confirming the relevant AWS service/API, account and region availability, authorized IAM permissions, secure secret handling, live health checks and end-to-end tests. Never commit credentials or personal data.
