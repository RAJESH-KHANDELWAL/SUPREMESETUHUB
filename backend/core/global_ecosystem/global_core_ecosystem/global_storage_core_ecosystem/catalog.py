"""Canonical provider and product inventory for Global Storage Core."""
from __future__ import annotations
from copy import deepcopy
import json
from typing import Any
_CATALOG_JSON = r'''{
  "schema_version": "1.0.0",
  "ecosystem_id": "GLOBAL-STORAGE-CORE-ECOSYSTEM",
  "name": "GLOBAL STORAGE CORE ECOSYSTEM",
  "provider": "global",
  "ecosystem_type": "GLOBAL_STORAGE_CONTROL_PLANE",
  "parent_id": "GLOBAL-CORE-ECOSYSTEM",
  "status": "REGISTERED",
  "enabled": true,
  "scope": "Provider-neutral catalog and governance for cloud, object, file, block, personal-drive, collaborative, backup, archive, hybrid and enterprise storage services.",
  "providers": [
    {
      "provider_id": "apple",
      "name": "Apple",
      "ecosystem_id": "APPLE-STORAGE-CORE-ECOSYSTEM",
      "package": "apple_storage_core_ecosystem",
      "status": "STORAGE_CORE_CATALOG_ONLY",
      "enabled": true,
      "product_count": 3,
      "capabilities": [
        "PERSONAL_FILE_SYNC",
        "PHOTO_LIBRARY_STORAGE",
        "DEVICE_BACKUP"
      ],
      "adapter_ref": null,
      "connected": false,
      "live_connection_verified": false
    },
    {
      "provider_id": "aws",
      "name": "Amazon Web Services",
      "ecosystem_id": "AWS-STORAGE-CORE-ECOSYSTEM",
      "package": "aws_storage_core_ecosystem",
      "status": "STORAGE_CORE_CATALOG_ONLY",
      "enabled": true,
      "product_count": 7,
      "capabilities": [
        "OBJECT_STORAGE",
        "ARCHIVE_OBJECT_STORAGE",
        "MANAGED_FILE_STORAGE",
        "BLOCK_STORAGE",
        "HYBRID_STORAGE",
        "BACKUP_AND_RECOVERY"
      ],
      "adapter_ref": null,
      "connected": false,
      "live_connection_verified": false
    },
    {
      "provider_id": "digitalocean",
      "name": "DigitalOcean",
      "ecosystem_id": "DIGITALOCEAN-STORAGE-CORE-ECOSYSTEM",
      "package": "digitalocean_storage_core_ecosystem",
      "status": "STORAGE_CORE_CATALOG_ONLY",
      "enabled": true,
      "product_count": 3,
      "capabilities": [
        "OBJECT_STORAGE",
        "BLOCK_STORAGE",
        "BACKUP_AND_RECOVERY"
      ],
      "adapter_ref": null,
      "connected": false,
      "live_connection_verified": false
    },
    {
      "provider_id": "google",
      "name": "Google Cloud",
      "ecosystem_id": "GOOGLE-STORAGE-CORE-ECOSYSTEM",
      "package": "google_storage_core_ecosystem",
      "status": "STORAGE_CORE_CATALOG_ONLY",
      "enabled": true,
      "product_count": 5,
      "capabilities": [
        "OBJECT_STORAGE",
        "MANAGED_FILE_STORAGE",
        "BLOCK_STORAGE",
        "BACKUP_AND_RECOVERY",
        "DATA_TRANSFER"
      ],
      "adapter_ref": null,
      "connected": false,
      "live_connection_verified": false
    },
    {
      "provider_id": "microsoft",
      "name": "Microsoft",
      "ecosystem_id": "MICROSOFT-STORAGE-CORE-ECOSYSTEM",
      "package": "microsoft_storage_core_ecosystem",
      "status": "STORAGE_CORE_CATALOG_ONLY",
      "enabled": true,
      "product_count": 7,
      "capabilities": [
        "OBJECT_STORAGE",
        "MANAGED_FILE_STORAGE",
        "BLOCK_STORAGE",
        "ENTERPRISE_FILE_STORAGE",
        "BACKUP_AND_RECOVERY",
        "PERSONAL_FILE_SYNC",
        "COLLABORATIVE_DOCUMENT_STORAGE"
      ],
      "adapter_ref": null,
      "connected": false,
      "live_connection_verified": false
    }
  ],
  "products": [
    {
      "product_id": "icloud_drive",
      "name": "iCloud Drive",
      "provider_id": "apple",
      "provider_name": "Apple",
      "domain_id": "PERSONAL_CLOUD_DRIVES",
      "ecosystem_id": "APPLE-ICLOUD-DRIVE-STORAGE-CORE-ECOSYSTEM",
      "provider_package": "apple_storage_core_ecosystem",
      "source_reference": "APPLE_ICLOUD",
      "status": "CORE_CATALOG_ONLY",
      "enabled": true,
      "connected": false,
      "live_connection_verified": false,
      "api_adapter_ref": null,
      "installation_verified": false,
      "entitlement_verified": false
    },
    {
      "product_id": "icloud_photos",
      "name": "iCloud Photos",
      "provider_id": "apple",
      "provider_name": "Apple",
      "domain_id": "PERSONAL_CLOUD_DRIVES",
      "ecosystem_id": "APPLE-ICLOUD-PHOTOS-STORAGE-CORE-ECOSYSTEM",
      "provider_package": "apple_storage_core_ecosystem",
      "source_reference": "APPLE_ICLOUD",
      "status": "CORE_CATALOG_ONLY",
      "enabled": true,
      "connected": false,
      "live_connection_verified": false,
      "api_adapter_ref": null,
      "installation_verified": false,
      "entitlement_verified": false
    },
    {
      "product_id": "icloud_backup",
      "name": "iCloud Backup",
      "provider_id": "apple",
      "provider_name": "Apple",
      "domain_id": "BACKUP_AND_RECOVERY",
      "ecosystem_id": "APPLE-ICLOUD-BACKUP-STORAGE-CORE-ECOSYSTEM",
      "provider_package": "apple_storage_core_ecosystem",
      "source_reference": "APPLE_ICLOUD",
      "status": "CORE_CATALOG_ONLY",
      "enabled": true,
      "connected": false,
      "live_connection_verified": false,
      "api_adapter_ref": null,
      "installation_verified": false,
      "entitlement_verified": false
    },
    {
      "product_id": "s3",
      "name": "Amazon S3",
      "provider_id": "aws",
      "provider_name": "Amazon Web Services",
      "domain_id": "OBJECT_STORAGE",
      "ecosystem_id": "AWS-S3-STORAGE-CORE-ECOSYSTEM",
      "provider_package": "aws_storage_core_ecosystem",
      "source_reference": "AWS_S3",
      "status": "CORE_CATALOG_ONLY",
      "enabled": true,
      "connected": false,
      "live_connection_verified": false,
      "api_adapter_ref": null,
      "installation_verified": false,
      "entitlement_verified": false
    },
    {
      "product_id": "s3_glacier",
      "name": "Amazon S3 Glacier storage classes",
      "provider_id": "aws",
      "provider_name": "Amazon Web Services",
      "domain_id": "ARCHIVE_AND_RETENTION",
      "ecosystem_id": "AWS-S3-GLACIER-STORAGE-CORE-ECOSYSTEM",
      "provider_package": "aws_storage_core_ecosystem",
      "source_reference": "AWS_S3",
      "status": "CORE_CATALOG_ONLY",
      "enabled": true,
      "connected": false,
      "live_connection_verified": false,
      "api_adapter_ref": null,
      "installation_verified": false,
      "entitlement_verified": false
    },
    {
      "product_id": "efs",
      "name": "Amazon EFS",
      "provider_id": "aws",
      "provider_name": "Amazon Web Services",
      "domain_id": "FILE_STORAGE",
      "ecosystem_id": "AWS-EFS-STORAGE-CORE-ECOSYSTEM",
      "provider_package": "aws_storage_core_ecosystem",
      "source_reference": "AWS_EFS",
      "status": "CORE_CATALOG_ONLY",
      "enabled": true,
      "connected": false,
      "live_connection_verified": false,
      "api_adapter_ref": null,
      "installation_verified": false,
      "entitlement_verified": false
    },
    {
      "product_id": "fsx",
      "name": "Amazon FSx",
      "provider_id": "aws",
      "provider_name": "Amazon Web Services",
      "domain_id": "FILE_STORAGE",
      "ecosystem_id": "AWS-FSX-STORAGE-CORE-ECOSYSTEM",
      "provider_package": "aws_storage_core_ecosystem",
      "source_reference": "AWS_FSX",
      "status": "CORE_CATALOG_ONLY",
      "enabled": true,
      "connected": false,
      "live_connection_verified": false,
      "api_adapter_ref": null,
      "installation_verified": false,
      "entitlement_verified": false
    },
    {
      "product_id": "ebs",
      "name": "Amazon EBS",
      "provider_id": "aws",
      "provider_name": "Amazon Web Services",
      "domain_id": "BLOCK_STORAGE",
      "ecosystem_id": "AWS-EBS-STORAGE-CORE-ECOSYSTEM",
      "provider_package": "aws_storage_core_ecosystem",
      "source_reference": "AWS_EBS",
      "status": "CORE_CATALOG_ONLY",
      "enabled": true,
      "connected": false,
      "live_connection_verified": false,
      "api_adapter_ref": null,
      "installation_verified": false,
      "entitlement_verified": false
    },
    {
      "product_id": "storage_gateway",
      "name": "AWS Storage Gateway",
      "provider_id": "aws",
      "provider_name": "Amazon Web Services",
      "domain_id": "EDGE_AND_HYBRID_STORAGE",
      "ecosystem_id": "AWS-STORAGE-GATEWAY-STORAGE-CORE-ECOSYSTEM",
      "provider_package": "aws_storage_core_ecosystem",
      "source_reference": "AWS_STORAGE_GATEWAY",
      "status": "CORE_CATALOG_ONLY",
      "enabled": true,
      "connected": false,
      "live_connection_verified": false,
      "api_adapter_ref": null,
      "installation_verified": false,
      "entitlement_verified": false
    },
    {
      "product_id": "backup",
      "name": "AWS Backup",
      "provider_id": "aws",
      "provider_name": "Amazon Web Services",
      "domain_id": "BACKUP_AND_RECOVERY",
      "ecosystem_id": "AWS-BACKUP-STORAGE-CORE-ECOSYSTEM",
      "provider_package": "aws_storage_core_ecosystem",
      "source_reference": "AWS_BACKUP",
      "status": "CORE_CATALOG_ONLY",
      "enabled": true,
      "connected": false,
      "live_connection_verified": false,
      "api_adapter_ref": null,
      "installation_verified": false,
      "entitlement_verified": false
    },
    {
      "product_id": "spaces",
      "name": "DigitalOcean Spaces",
      "provider_id": "digitalocean",
      "provider_name": "DigitalOcean",
      "domain_id": "OBJECT_STORAGE",
      "ecosystem_id": "DIGITALOCEAN-SPACES-STORAGE-CORE-ECOSYSTEM",
      "provider_package": "digitalocean_storage_core_ecosystem",
      "source_reference": "DIGITALOCEAN_SPACES",
      "status": "CORE_CATALOG_ONLY",
      "enabled": true,
      "connected": false,
      "live_connection_verified": false,
      "api_adapter_ref": null,
      "installation_verified": false,
      "entitlement_verified": false
    },
    {
      "product_id": "volumes",
      "name": "DigitalOcean Volumes",
      "provider_id": "digitalocean",
      "provider_name": "DigitalOcean",
      "domain_id": "BLOCK_STORAGE",
      "ecosystem_id": "DIGITALOCEAN-VOLUMES-STORAGE-CORE-ECOSYSTEM",
      "provider_package": "digitalocean_storage_core_ecosystem",
      "source_reference": "DIGITALOCEAN_VOLUMES",
      "status": "CORE_CATALOG_ONLY",
      "enabled": true,
      "connected": false,
      "live_connection_verified": false,
      "api_adapter_ref": null,
      "installation_verified": false,
      "entitlement_verified": false
    },
    {
      "product_id": "backups",
      "name": "DigitalOcean Droplet Backups",
      "provider_id": "digitalocean",
      "provider_name": "DigitalOcean",
      "domain_id": "BACKUP_AND_RECOVERY",
      "ecosystem_id": "DIGITALOCEAN-BACKUPS-STORAGE-CORE-ECOSYSTEM",
      "provider_package": "digitalocean_storage_core_ecosystem",
      "source_reference": "DIGITALOCEAN_BACKUPS",
      "status": "CORE_CATALOG_ONLY",
      "enabled": true,
      "connected": false,
      "live_connection_verified": false,
      "api_adapter_ref": null,
      "installation_verified": false,
      "entitlement_verified": false
    },
    {
      "product_id": "cloud_storage",
      "name": "Google Cloud Storage",
      "provider_id": "google",
      "provider_name": "Google Cloud",
      "domain_id": "OBJECT_STORAGE",
      "ecosystem_id": "GOOGLE-CLOUD-STORAGE-STORAGE-CORE-ECOSYSTEM",
      "provider_package": "google_storage_core_ecosystem",
      "source_reference": "GOOGLE_CLOUD_STORAGE",
      "status": "CORE_CATALOG_ONLY",
      "enabled": true,
      "connected": false,
      "live_connection_verified": false,
      "api_adapter_ref": null,
      "installation_verified": false,
      "entitlement_verified": false
    },
    {
      "product_id": "filestore",
      "name": "Google Cloud Filestore",
      "provider_id": "google",
      "provider_name": "Google Cloud",
      "domain_id": "FILE_STORAGE",
      "ecosystem_id": "GOOGLE-FILESTORE-STORAGE-CORE-ECOSYSTEM",
      "provider_package": "google_storage_core_ecosystem",
      "source_reference": "GOOGLE_FILESTORE",
      "status": "CORE_CATALOG_ONLY",
      "enabled": true,
      "connected": false,
      "live_connection_verified": false,
      "api_adapter_ref": null,
      "installation_verified": false,
      "entitlement_verified": false
    },
    {
      "product_id": "persistent_disk",
      "name": "Google Persistent Disk",
      "provider_id": "google",
      "provider_name": "Google Cloud",
      "domain_id": "BLOCK_STORAGE",
      "ecosystem_id": "GOOGLE-PERSISTENT-DISK-STORAGE-CORE-ECOSYSTEM",
      "provider_package": "google_storage_core_ecosystem",
      "source_reference": "GOOGLE_COMPUTE_ENGINE",
      "status": "CORE_CATALOG_ONLY",
      "enabled": true,
      "connected": false,
      "live_connection_verified": false,
      "api_adapter_ref": null,
      "installation_verified": false,
      "entitlement_verified": false
    },
    {
      "product_id": "backup_dr",
      "name": "Backup and DR Service",
      "provider_id": "google",
      "provider_name": "Google Cloud",
      "domain_id": "BACKUP_AND_RECOVERY",
      "ecosystem_id": "GOOGLE-BACKUP-DR-STORAGE-CORE-ECOSYSTEM",
      "provider_package": "google_storage_core_ecosystem",
      "source_reference": "GOOGLE_BACKUP_DR",
      "status": "CORE_CATALOG_ONLY",
      "enabled": true,
      "connected": false,
      "live_connection_verified": false,
      "api_adapter_ref": null,
      "installation_verified": false,
      "entitlement_verified": false
    },
    {
      "product_id": "storage_transfer",
      "name": "Storage Transfer Service",
      "provider_id": "google",
      "provider_name": "Google Cloud",
      "domain_id": "DATA_TRANSFER_AND_MIGRATION",
      "ecosystem_id": "GOOGLE-STORAGE-TRANSFER-STORAGE-CORE-ECOSYSTEM",
      "provider_package": "google_storage_core_ecosystem",
      "source_reference": "GOOGLE_STORAGE_TRANSFER",
      "status": "CORE_CATALOG_ONLY",
      "enabled": true,
      "connected": false,
      "live_connection_verified": false,
      "api_adapter_ref": null,
      "installation_verified": false,
      "entitlement_verified": false
    },
    {
      "product_id": "azure_blob",
      "name": "Azure Blob Storage",
      "provider_id": "microsoft",
      "provider_name": "Microsoft",
      "domain_id": "OBJECT_STORAGE",
      "ecosystem_id": "MICROSOFT-AZURE-BLOB-STORAGE-CORE-ECOSYSTEM",
      "provider_package": "microsoft_storage_core_ecosystem",
      "source_reference": "AZURE_BLOB",
      "status": "CORE_CATALOG_ONLY",
      "enabled": true,
      "connected": false,
      "live_connection_verified": false,
      "api_adapter_ref": null,
      "installation_verified": false,
      "entitlement_verified": false
    },
    {
      "product_id": "azure_files",
      "name": "Azure Files",
      "provider_id": "microsoft",
      "provider_name": "Microsoft",
      "domain_id": "FILE_STORAGE",
      "ecosystem_id": "MICROSOFT-AZURE-FILES-STORAGE-CORE-ECOSYSTEM",
      "provider_package": "microsoft_storage_core_ecosystem",
      "source_reference": "AZURE_FILES",
      "status": "CORE_CATALOG_ONLY",
      "enabled": true,
      "connected": false,
      "live_connection_verified": false,
      "api_adapter_ref": null,
      "installation_verified": false,
      "entitlement_verified": false
    },
    {
      "product_id": "azure_managed_disks",
      "name": "Azure Managed Disks",
      "provider_id": "microsoft",
      "provider_name": "Microsoft",
      "domain_id": "BLOCK_STORAGE",
      "ecosystem_id": "MICROSOFT-AZURE-MANAGED-DISKS-STORAGE-CORE-ECOSYSTEM",
      "provider_package": "microsoft_storage_core_ecosystem",
      "source_reference": "AZURE_MANAGED_DISKS",
      "status": "CORE_CATALOG_ONLY",
      "enabled": true,
      "connected": false,
      "live_connection_verified": false,
      "api_adapter_ref": null,
      "installation_verified": false,
      "entitlement_verified": false
    },
    {
      "product_id": "azure_netapp_files",
      "name": "Azure NetApp Files",
      "provider_id": "microsoft",
      "provider_name": "Microsoft",
      "domain_id": "FILE_STORAGE",
      "ecosystem_id": "MICROSOFT-AZURE-NETAPP-FILES-STORAGE-CORE-ECOSYSTEM",
      "provider_package": "microsoft_storage_core_ecosystem",
      "source_reference": "AZURE_NETAPP_FILES",
      "status": "CORE_CATALOG_ONLY",
      "enabled": true,
      "connected": false,
      "live_connection_verified": false,
      "api_adapter_ref": null,
      "installation_verified": false,
      "entitlement_verified": false
    },
    {
      "product_id": "azure_backup",
      "name": "Azure Backup",
      "provider_id": "microsoft",
      "provider_name": "Microsoft",
      "domain_id": "BACKUP_AND_RECOVERY",
      "ecosystem_id": "MICROSOFT-AZURE-BACKUP-STORAGE-CORE-ECOSYSTEM",
      "provider_package": "microsoft_storage_core_ecosystem",
      "source_reference": "AZURE_BACKUP",
      "status": "CORE_CATALOG_ONLY",
      "enabled": true,
      "connected": false,
      "live_connection_verified": false,
      "api_adapter_ref": null,
      "installation_verified": false,
      "entitlement_verified": false
    },
    {
      "product_id": "onedrive",
      "name": "OneDrive",
      "provider_id": "microsoft",
      "provider_name": "Microsoft",
      "domain_id": "PERSONAL_CLOUD_DRIVES",
      "ecosystem_id": "MICROSOFT-ONEDRIVE-STORAGE-CORE-ECOSYSTEM",
      "provider_package": "microsoft_storage_core_ecosystem",
      "source_reference": "MICROSOFT_365",
      "status": "CORE_CATALOG_ONLY",
      "enabled": true,
      "connected": false,
      "live_connection_verified": false,
      "api_adapter_ref": null,
      "installation_verified": false,
      "entitlement_verified": false
    },
    {
      "product_id": "sharepoint",
      "name": "SharePoint document libraries",
      "provider_id": "microsoft",
      "provider_name": "Microsoft",
      "domain_id": "COLLABORATIVE_DOCUMENT_STORAGE",
      "ecosystem_id": "MICROSOFT-SHAREPOINT-STORAGE-CORE-ECOSYSTEM",
      "provider_package": "microsoft_storage_core_ecosystem",
      "source_reference": "MICROSOFT_365",
      "status": "CORE_CATALOG_ONLY",
      "enabled": true,
      "connected": false,
      "live_connection_verified": false,
      "api_adapter_ref": null,
      "installation_verified": false,
      "entitlement_verified": false
    }
  ],
  "domains": [
    {
      "domain_id": "PROVIDER_GOVERNANCE",
      "name": "Provider Governance",
      "purpose": "Provider identity, registration, eligibility, ownership and provider lifecycle.",
      "package": "global_provider_governance_core_ecosystem"
    },
    {
      "domain_id": "OBJECT_STORAGE",
      "name": "Object Storage",
      "purpose": "Buckets, containers, objects, namespaces, metadata and object lifecycle.",
      "package": "global_object_storage_core_ecosystem"
    },
    {
      "domain_id": "FILE_STORAGE",
      "name": "File Storage",
      "purpose": "Managed file shares, network file systems, protocols and file access metadata.",
      "package": "global_file_storage_core_ecosystem"
    },
    {
      "domain_id": "BLOCK_STORAGE",
      "name": "Block Storage",
      "purpose": "Volumes, disks, snapshots and attachment metadata.",
      "package": "global_block_storage_core_ecosystem"
    },
    {
      "domain_id": "PERSONAL_CLOUD_DRIVES",
      "name": "Personal Cloud Drives",
      "purpose": "Personal files, folders, sync clients and user-owned cloud-drive metadata.",
      "package": "global_personal_cloud_drives_core_ecosystem"
    },
    {
      "domain_id": "COLLABORATIVE_DOCUMENT_STORAGE",
      "name": "Collaborative Document Storage",
      "purpose": "Team document libraries, shared workspaces, permissions and version metadata.",
      "package": "global_collaborative_document_storage_core_ecosystem"
    },
    {
      "domain_id": "BACKUP_AND_RECOVERY",
      "name": "Backup and Recovery",
      "purpose": "Backup plans, restore points, retention, recovery objectives and restore authorization.",
      "package": "global_backup_and_recovery_core_ecosystem"
    },
    {
      "domain_id": "ARCHIVE_AND_RETENTION",
      "name": "Archive and Retention",
      "purpose": "Cold/archive tiers, retention schedules, legal holds and lifecycle rules.",
      "package": "global_archive_and_retention_core_ecosystem"
    },
    {
      "domain_id": "DATA_TRANSFER_AND_MIGRATION",
      "name": "Data Transfer and Migration",
      "purpose": "Bulk transfer, migration planning, transfer jobs and validation metadata.",
      "package": "global_data_transfer_and_migration_core_ecosystem"
    },
    {
      "domain_id": "SYNC_AND_REPLICATION",
      "name": "Sync and Replication",
      "purpose": "Sync policies, replication topology, consistency and conflict metadata.",
      "package": "global_sync_and_replication_core_ecosystem"
    },
    {
      "domain_id": "SHARING_AND_ACCESS",
      "name": "Sharing and Access",
      "purpose": "Sharing links, access scopes, permissions, IAM boundaries and access reviews.",
      "package": "global_sharing_and_access_core_ecosystem"
    },
    {
      "domain_id": "ENCRYPTION_AND_KEY_BOUNDARIES",
      "name": "Encryption and Key Boundaries",
      "purpose": "Encryption metadata, key references, customer-managed key boundaries and rotation state.",
      "package": "global_encryption_and_key_boundaries_core_ecosystem"
    },
    {
      "domain_id": "STORAGE_SECURITY_AND_COMPLIANCE",
      "name": "Storage Security and Compliance",
      "purpose": "Threat protection, audit metadata, compliance posture and data residency.",
      "package": "global_storage_security_and_compliance_core_ecosystem"
    },
    {
      "domain_id": "OBSERVABILITY_AND_COST",
      "name": "Observability and Cost",
      "purpose": "Capacity, usage, metrics, quotas, billing references and cost optimization metadata.",
      "package": "global_observability_and_cost_core_ecosystem"
    },
    {
      "domain_id": "EDGE_AND_HYBRID_STORAGE",
      "name": "Edge and Hybrid Storage",
      "purpose": "Hybrid gateways, edge caches, local/cloud tiering and connected storage metadata.",
      "package": "global_edge_and_hybrid_storage_core_ecosystem"
    },
    {
      "domain_id": "LIFECYCLE_AND_VERSIONING",
      "name": "Lifecycle and Versioning",
      "purpose": "Object versions, snapshots, lifecycle policies, immutability and deletion boundaries.",
      "package": "global_lifecycle_and_versioning_core_ecosystem"
    },
    {
      "domain_id": "TENANCY_AND_DATA_GOVERNANCE",
      "name": "Tenancy and Data Governance",
      "purpose": "Tenant isolation, data classification, ownership, residency and governance metadata.",
      "package": "global_tenancy_and_data_governance_core_ecosystem"
    }
  ],
  "shared_components": {
    "integrations": "Provider adapter registration and contract metadata only; API transport and credentials remain in API/auth layers.",
    "services": "Read-only catalog, product, domain and dependency services.",
    "tools": "Offline validation and diagnostics; no destructive storage actions."
  },
  "layer_boundary": {
    "core": [
      "provider and product identity",
      "domain taxonomy",
      "capability metadata",
      "tenant context contracts",
      "lifecycle and readiness metadata",
      "policy and dependency metadata"
    ],
    "storage": [
      "provider-specific storage operations and adapters"
    ],
    "api": [
      "OAuth and authentication flows",
      "SDK clients",
      "network transport",
      "response normalization"
    ],
    "database": [
      "database engines",
      "schemas",
      "queries",
      "transactions"
    ],
    "runtime": [
      "jobs",
      "retries",
      "queues",
      "scheduling"
    ],
    "application": [
      "user consent",
      "sessions",
      "user workflows",
      "UI"
    ]
  },
  "security": {
    "tenant_context_required": true,
    "secrets_in_catalog": false,
    "credentials_storage": "EXTERNAL_SECRET_STORE_ONLY",
    "live_connections_verified": false,
    "destructive_operations_enabled": false,
    "catalog_presence_is_not_installation": true,
    "catalog_presence_is_not_entitlement": true,
    "privileged_actions_require_explicit_authorization_and_audit": true
  },
  "counts": {
    "provider_count": 5,
    "product_count": 25,
    "domain_count": 17,
    "live_connections_verified": 0
  }
}'''
GLOBAL_STORAGE_CORE_ECOSYSTEM: dict[str, Any] = json.loads(_CATALOG_JSON)

def get_storage_core_catalog() -> dict[str, Any]: return deepcopy(GLOBAL_STORAGE_CORE_ECOSYSTEM)
def list_storage_providers(*, enabled_only: bool=False) -> list[dict[str, Any]]:
    items=get_storage_core_catalog()["providers"]
    return [p for p in items if p.get("enabled",True)] if enabled_only else items
def get_storage_provider(provider_id: str):
    key=provider_id.strip().casefold()
    if not key: return None
    return next((p for p in list_storage_providers() if p["provider_id"].casefold()==key or p["ecosystem_id"].casefold()==key),None)
