"""Read-only Individual Adult Privacy Security metadata contract; no API or persistence."""
MODULE={
  "module_id": "INDIVIDUAL-ADULT-PRIVACY-SECURITY-CORE-ECOSYSTEM",
  "directory": "individual_adult_privacy_security_core_ecosystem",
  "name": "Individual Adult Privacy Security",
  "master_entry_ids": [
    "S02_human_rights",
    "S02_adults"
  ],
  "parent_id": "GLOBAL-INDIVIDUAL-CORE-ECOSYSTEM",
  "status": "CORE_CATALOG_ONLY",
  "connected": False,
  "api_transport_in_core": False,
  "persistence_enabled": False
}
def get_module_metadata(): return dict(MODULE)
