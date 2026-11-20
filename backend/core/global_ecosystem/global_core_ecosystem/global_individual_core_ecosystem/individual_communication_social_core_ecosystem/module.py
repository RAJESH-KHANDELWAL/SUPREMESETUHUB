"""Read-only Individual Communication Social metadata contract; no API or persistence."""
MODULE={
  "module_id": "INDIVIDUAL-COMMUNICATION-SOCIAL-CORE-ECOSYSTEM",
  "directory": "individual_communication_social_core_ecosystem",
  "name": "Individual Communication Social",
  "master_entry_ids": [
    "S02_individual",
    "S02_community",
    "S02_society"
  ],
  "parent_id": "GLOBAL-INDIVIDUAL-CORE-ECOSYSTEM",
  "status": "CORE_CATALOG_ONLY",
  "connected": false,
  "api_transport_in_core": false,
  "persistence_enabled": false
}
def get_module_metadata(): return dict(MODULE)
