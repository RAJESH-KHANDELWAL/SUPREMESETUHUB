"""Storage responsibility taxonomy shared by all domain packages."""
from __future__ import annotations
from typing import Any
DOMAIN_DEFINITIONS: dict[str,dict[str,str]] = {
  "PROVIDER_GOVERNANCE": {
    "name": "Provider Governance",
    "purpose": "Provider identity, registration, eligibility, ownership and provider lifecycle."
  },
  "OBJECT_STORAGE": {
    "name": "Object Storage",
    "purpose": "Buckets, containers, objects, namespaces, metadata and object lifecycle."
  },
  "FILE_STORAGE": {
    "name": "File Storage",
    "purpose": "Managed file shares, network file systems, protocols and file access metadata."
  },
  "BLOCK_STORAGE": {
    "name": "Block Storage",
    "purpose": "Volumes, disks, snapshots and attachment metadata."
  },
  "PERSONAL_CLOUD_DRIVES": {
    "name": "Personal Cloud Drives",
    "purpose": "Personal files, folders, sync clients and user-owned cloud-drive metadata."
  },
  "COLLABORATIVE_DOCUMENT_STORAGE": {
    "name": "Collaborative Document Storage",
    "purpose": "Team document libraries, shared workspaces, permissions and version metadata."
  },
  "BACKUP_AND_RECOVERY": {
    "name": "Backup and Recovery",
    "purpose": "Backup plans, restore points, retention, recovery objectives and restore authorization."
  },
  "ARCHIVE_AND_RETENTION": {
    "name": "Archive and Retention",
    "purpose": "Cold/archive tiers, retention schedules, legal holds and lifecycle rules."
  },
  "DATA_TRANSFER_AND_MIGRATION": {
    "name": "Data Transfer and Migration",
    "purpose": "Bulk transfer, migration planning, transfer jobs and validation metadata."
  },
  "SYNC_AND_REPLICATION": {
    "name": "Sync and Replication",
    "purpose": "Sync policies, replication topology, consistency and conflict metadata."
  },
  "SHARING_AND_ACCESS": {
    "name": "Sharing and Access",
    "purpose": "Sharing links, access scopes, permissions, IAM boundaries and access reviews."
  },
  "ENCRYPTION_AND_KEY_BOUNDARIES": {
    "name": "Encryption and Key Boundaries",
    "purpose": "Encryption metadata, key references, customer-managed key boundaries and rotation state."
  },
  "STORAGE_SECURITY_AND_COMPLIANCE": {
    "name": "Storage Security and Compliance",
    "purpose": "Threat protection, audit metadata, compliance posture and data residency."
  },
  "OBSERVABILITY_AND_COST": {
    "name": "Observability and Cost",
    "purpose": "Capacity, usage, metrics, quotas, billing references and cost optimization metadata."
  },
  "EDGE_AND_HYBRID_STORAGE": {
    "name": "Edge and Hybrid Storage",
    "purpose": "Hybrid gateways, edge caches, local/cloud tiering and connected storage metadata."
  },
  "LIFECYCLE_AND_VERSIONING": {
    "name": "Lifecycle and Versioning",
    "purpose": "Object versions, snapshots, lifecycle policies, immutability and deletion boundaries."
  },
  "TENANCY_AND_DATA_GOVERNANCE": {
    "name": "Tenancy and Data Governance",
    "purpose": "Tenant isolation, data classification, ownership, residency and governance metadata."
  }
}
def list_storage_domain_inventory() -> list[dict[str,Any]]:
    return [{"domain_id":k,**v,"status":"STORAGE_DOMAIN_AVAILABLE"} for k,v in DOMAIN_DEFINITIONS.items()]
def storage_domain_summary() -> dict[str,Any]:
    items=list_storage_domain_inventory()
    return {"success":True,"domain_count":len(items),"domains":items}
