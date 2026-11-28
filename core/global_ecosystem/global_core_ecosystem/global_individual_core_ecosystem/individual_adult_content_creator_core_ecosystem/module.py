"""Read-only Individual Adult Content Creator metadata contract; no API or persistence."""
MODULE={
  "module_id": "INDIVIDUAL-ADULT-CONTENT-CREATOR-CORE-ECOSYSTEM",
  "directory": "individual_adult_content_creator_core_ecosystem",
  "name": "Individual Adult Content Creator",
  "master_entry_ids": [
    "S02_adults",
    "S02_human_rights"
  ],
  "parent_id": "GLOBAL-INDIVIDUAL-CORE-ECOSYSTEM",
  "status": "CORE_CATALOG_ONLY",
  "connected": False,
  "api_transport_in_core": False,
  "persistence_enabled": False
}
def get_module_metadata(): return dict(MODULE)
