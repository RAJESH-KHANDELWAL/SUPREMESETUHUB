"""Read-only Individual Sexual Wellness Education metadata contract; no API or persistence."""
MODULE={
  "module_id": "INDIVIDUAL-SEXUAL-WELLNESS-EDUCATION-CORE-ECOSYSTEM",
  "directory": "individual_sexual_wellness_education_core_ecosystem",
  "name": "Individual Sexual Wellness Education",
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
