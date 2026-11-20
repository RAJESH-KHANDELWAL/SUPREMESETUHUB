"""Read-only Individual Wellness Health Resources metadata contract; no API or persistence."""
MODULE={
  "module_id": "INDIVIDUAL-WELLNESS-HEALTH-RESOURCES-CORE-ECOSYSTEM",
  "directory": "individual_wellness_health_resources_core_ecosystem",
  "name": "Individual Wellness Health Resources",
  "master_entry_ids": [
    "S02_individual",
    "S02_human_development"
  ],
  "parent_id": "GLOBAL-INDIVIDUAL-CORE-ECOSYSTEM",
  "status": "CORE_CATALOG_ONLY",
  "connected": False,
  "api_transport_in_core": False,
  "persistence_enabled": False
}
def get_module_metadata(): return dict(MODULE)
