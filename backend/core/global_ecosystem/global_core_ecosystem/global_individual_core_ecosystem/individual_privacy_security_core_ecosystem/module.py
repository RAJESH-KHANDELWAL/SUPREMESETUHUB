"""Read-only Individual Privacy Security metadata contract; no API or persistence."""
MODULE={
  "module_id": "INDIVIDUAL-PRIVACY-SECURITY-CORE-ECOSYSTEM",
  "directory": "individual_privacy_security_core_ecosystem",
  "name": "Individual Privacy Security",
  "master_entry_ids": [
    "S02_human_rights",
    "S02_human_identity"
  ],
  "parent_id": "GLOBAL-INDIVIDUAL-CORE-ECOSYSTEM",
  "status": "CORE_CATALOG_ONLY",
  "connected": false,
  "api_transport_in_core": false,
  "persistence_enabled": false
}
def get_module_metadata(): return dict(MODULE)
