"""Read-only Individual Adult Content Production Studio metadata contract; no API or persistence."""
MODULE={
  "module_id": "INDIVIDUAL-ADULT-CONTENT-PRODUCTION-STUDIO-CORE-ECOSYSTEM",
  "directory": "individual_adult_content_production_studio_core_ecosystem",
  "name": "Individual Adult Content Production Studio",
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
