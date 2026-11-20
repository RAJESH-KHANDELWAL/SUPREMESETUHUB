"""Read-only Individual Cloud Storage metadata contract; no API or persistence."""
MODULE={
  "module_id": "INDIVIDUAL-CLOUD-STORAGE-CORE-ECOSYSTEM",
  "directory": "individual_cloud_storage_core_ecosystem",
  "name": "Individual Cloud Storage",
  "master_entry_ids": [
    "S02_individual",
    "S02_human_identity"
  ],
  "parent_id": "GLOBAL-INDIVIDUAL-CORE-ECOSYSTEM",
  "status": "CORE_CATALOG_ONLY",
  "connected": False,
  "api_transport_in_core": False,
  "persistence_enabled": False
}
def get_module_metadata(): return dict(MODULE)
