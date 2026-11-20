"""Read-only Individual Service Tiers Normal to Supreme metadata contract; no API or persistence."""
MODULE={
  "module_id": "INDIVIDUAL-SERVICE-TIERS-NORMAL-TO-SUPREME-CORE-ECOSYSTEM",
  "directory": "individual_service_tiers_normal_to_supreme_core_ecosystem",
  "name": "Individual Service Tiers Normal to Supreme",
  "master_entry_ids": [
    "S02_individual"
  ],
  "parent_id": "GLOBAL-INDIVIDUAL-CORE-ECOSYSTEM",
  "status": "CORE_CATALOG_ONLY",
  "connected": false,
  "api_transport_in_core": false,
  "persistence_enabled": false
}
def get_module_metadata(): return dict(MODULE)
