"""Read-only Individual Documents Digital Locker metadata contract; no API or persistence."""
MODULE={
  "module_id": "INDIVIDUAL-DOCUMENTS-DIGITAL-LOCKER-CORE-ECOSYSTEM",
  "directory": "individual_documents_digital_locker_core_ecosystem",
  "name": "Individual Documents Digital Locker",
  "master_entry_ids": [
    "S02_human_identity",
    "S02_individual"
  ],
  "parent_id": "GLOBAL-INDIVIDUAL-CORE-ECOSYSTEM",
  "status": "CORE_CATALOG_ONLY",
  "connected": false,
  "api_transport_in_core": false,
  "persistence_enabled": false
}
def get_module_metadata(): return dict(MODULE)
