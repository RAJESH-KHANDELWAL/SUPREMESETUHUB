"""Read-only Individual Account Access metadata contract; no API or persistence."""
MODULE={
  "module_id": "INDIVIDUAL-ACCOUNT-ACCESS-CORE-ECOSYSTEM",
  "directory": "individual_account_access_core_ecosystem",
  "name": "Individual Account Access",
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
