"""Read-only Individual Dating Relationships metadata contract; no API or persistence."""
MODULE={
  "module_id": "INDIVIDUAL-DATING-RELATIONSHIPS-CORE-ECOSYSTEM",
  "directory": "individual_dating_relationships_core_ecosystem",
  "name": "Individual Dating Relationships",
  "master_entry_ids": [
    "S02_individual",
    "S02_adults",
    "S02_human_behaviour"
  ],
  "parent_id": "GLOBAL-INDIVIDUAL-CORE-ECOSYSTEM",
  "status": "CORE_CATALOG_ONLY",
  "connected": False,
  "api_transport_in_core": False,
  "persistence_enabled": False
}
def get_module_metadata(): return dict(MODULE)
