"""Read-only Individual Education Learning metadata contract; no API or persistence."""
MODULE={
  "module_id": "INDIVIDUAL-EDUCATION-LEARNING-CORE-ECOSYSTEM",
  "directory": "individual_education_learning_core_ecosystem",
  "name": "Individual Education Learning",
  "master_entry_ids": [
    "S02_education",
    "S02_knowledge",
    "S02_skills_and_talents"
  ],
  "parent_id": "GLOBAL-INDIVIDUAL-CORE-ECOSYSTEM",
  "status": "CORE_CATALOG_ONLY",
  "connected": false,
  "api_transport_in_core": false,
  "persistence_enabled": false
}
def get_module_metadata(): return dict(MODULE)
