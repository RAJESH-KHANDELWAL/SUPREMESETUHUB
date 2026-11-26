"""Behavior and structure tests for Global Storage Core."""
from importlib import import_module
from .catalog import get_storage_core_catalog
from .domain_catalog import DOMAIN_DEFINITIONS,storage_domain_summary
from .manager import get_manager

def test_provider_product_domain_inventory_is_consistent():
 c=get_storage_core_catalog()
 assert len(c["providers"])==5
 assert len(c["products"])==25
 assert len(c["domains"])==17
 assert len({p["provider_id"] for p in c["providers"]})==len(c["providers"])
 assert len({p["product_id"] for p in c["products"]})==len(c["products"])
 assert all(p["connected"] is False and p["live_connection_verified"] is False for p in c["providers"])
 assert all(p["live_connection_verified"] is False and p["installation_verified"] is False and p["entitlement_verified"] is False for p in c["products"])

def test_all_domain_managers_resolve_products():
 package_root="backend.core.global_ecosystem.global_core_ecosystem.global_storage_core_ecosystem"
 for domain_id,package in DOMAIN_PACKAGES.items():
  module=import_module(f"{package_root}.{package}")
  manager=module.get_manager()
  assert manager.DOMAIN_ID==domain_id
  assert manager.status()["success"] is True

def test_provider_manager_exports_read_only_status():
 package_root="backend.core.global_ecosystem.global_core_ecosystem.global_storage_core_ecosystem"
 for provider_id,package in PROVIDER_PACKAGES.items():
  manager=import_module(f"{package_root}.{package}").get_manager()
  assert manager.status()["provider_id"]==provider_id
  assert manager.status()["live_connection_verified"] is False

def test_manager_health_and_policy_boundaries():
 m=get_manager(); h=m.health()
 assert h["provider_count"]==5
 assert h["product_count"]==25
 assert h["domain_count"]==len(DOMAIN_DEFINITIONS)
 assert h["live_connections_verified"]==0
 assert storage_domain_summary()["domain_count"]==len(DOMAIN_DEFINITIONS)

def test_tenant_context_and_capability_guardrails():
 from .contracts import TenantContext
 from .policy import StorageCorePolicy,StorageCorePolicyError
 StorageCorePolicy.require_tenant_context(TenantContext("tenant-1","actor-1"))
 try: StorageCorePolicy.require_tenant_context(None)
 except StorageCorePolicyError: pass
 else: raise AssertionError("missing tenant context must be rejected")

DOMAIN_PACKAGES={
  "PROVIDER_GOVERNANCE": "global_provider_governance_core_ecosystem",
  "OBJECT_STORAGE": "global_object_storage_core_ecosystem",
  "FILE_STORAGE": "global_file_storage_core_ecosystem",
  "BLOCK_STORAGE": "global_block_storage_core_ecosystem",
  "PERSONAL_CLOUD_DRIVES": "global_personal_cloud_drives_core_ecosystem",
  "COLLABORATIVE_DOCUMENT_STORAGE": "global_collaborative_document_storage_core_ecosystem",
  "BACKUP_AND_RECOVERY": "global_backup_and_recovery_core_ecosystem",
  "ARCHIVE_AND_RETENTION": "global_archive_and_retention_core_ecosystem",
  "DATA_TRANSFER_AND_MIGRATION": "global_data_transfer_and_migration_core_ecosystem",
  "SYNC_AND_REPLICATION": "global_sync_and_replication_core_ecosystem",
  "SHARING_AND_ACCESS": "global_sharing_and_access_core_ecosystem",
  "ENCRYPTION_AND_KEY_BOUNDARIES": "global_encryption_and_key_boundaries_core_ecosystem",
  "STORAGE_SECURITY_AND_COMPLIANCE": "global_storage_security_and_compliance_core_ecosystem",
  "OBSERVABILITY_AND_COST": "global_observability_and_cost_core_ecosystem",
  "EDGE_AND_HYBRID_STORAGE": "global_edge_and_hybrid_storage_core_ecosystem",
  "LIFECYCLE_AND_VERSIONING": "global_lifecycle_and_versioning_core_ecosystem",
  "TENANCY_AND_DATA_GOVERNANCE": "global_tenancy_and_data_governance_core_ecosystem"
}
PROVIDER_PACKAGES={
  "apple": "apple_storage_core_ecosystem",
  "aws": "aws_storage_core_ecosystem",
  "digitalocean": "digitalocean_storage_core_ecosystem",
  "google": "google_storage_core_ecosystem",
  "microsoft": "microsoft_storage_core_ecosystem"
}
