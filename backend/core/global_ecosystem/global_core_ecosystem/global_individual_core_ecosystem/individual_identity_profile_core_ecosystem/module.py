"""Read-only Individual Identity Profile metadata contract; no API or persistence."""
MODULE={
  "module_id": "INDIVIDUAL-IDENTITY-PROFILE-CORE-ECOSYSTEM",
  "directory": "individual_identity_profile_core_ecosystem",
  "name": "Individual Identity Profile",
  "master_entry_ids": [
    "S02_human_identity",
    "S02_individual"
  ],
  "parent_id": "GLOBAL-INDIVIDUAL-CORE-ECOSYSTEM",
  "status": "CORE_CATALOG_ONLY",
  "connected": False,
  "api_transport_in_core": False,
  "persistence_enabled": False
}
def get_module_metadata(): return dict(MODULE)
