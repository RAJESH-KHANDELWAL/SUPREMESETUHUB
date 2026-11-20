"""Read-only India Individual Services metadata contract; no API or persistence."""
MODULE={
  "module_id": "INDIA-INDIVIDUAL-SERVICES-CORE-ECOSYSTEM",
  "directory": "india_individual_services_core_ecosystem",
  "name": "India Individual Services",
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
