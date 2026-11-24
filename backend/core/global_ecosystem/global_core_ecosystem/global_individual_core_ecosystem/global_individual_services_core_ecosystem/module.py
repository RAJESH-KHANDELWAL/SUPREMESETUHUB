"""Read-only Global Individual Services metadata contract; no API or persistence."""
MODULE={
  "module_id": "GLOBAL-INDIVIDUAL-SERVICES-CORE-ECOSYSTEM",
  "directory": "global_individual_services_core_ecosystem",
  "name": "Global Individual Services",
  "master_entry_ids": [
    "S02_individual",
    "S02_human_identity",
    "S02_community"
  ],
  "parent_id": "GLOBAL-INDIVIDUAL-CORE-ECOSYSTEM",
  "status": "CORE_CATALOG_ONLY",
  "connected": False,
  "api_transport_in_core": False,
  "persistence_enabled": False
}
def get_module_metadata(): return dict(MODULE)
