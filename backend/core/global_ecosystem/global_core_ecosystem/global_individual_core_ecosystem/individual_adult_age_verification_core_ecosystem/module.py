"""Read-only Individual Adult Age Verification metadata contract; no API or persistence."""
MODULE={
  "module_id": "INDIVIDUAL-ADULT-AGE-VERIFICATION-CORE-ECOSYSTEM",
  "directory": "individual_adult_age_verification_core_ecosystem",
  "name": "Individual Adult Age Verification",
  "master_entry_ids": [
    "S02_adults",
    "S02_human_rights"
  ],
  "parent_id": "GLOBAL-INDIVIDUAL-CORE-ECOSYSTEM",
  "status": "CORE_CATALOG_ONLY",
  "connected": false,
  "api_transport_in_core": false,
  "persistence_enabled": false
}
def get_module_metadata(): return dict(MODULE)
