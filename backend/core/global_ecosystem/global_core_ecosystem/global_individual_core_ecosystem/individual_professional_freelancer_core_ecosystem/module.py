"""Read-only Individual Professional Freelancer metadata contract; no API or persistence."""
MODULE={
  "module_id": "INDIVIDUAL-PROFESSIONAL-FREELANCER-CORE-ECOSYSTEM",
  "directory": "individual_professional_freelancer_core_ecosystem",
  "name": "Individual Professional Freelancer",
  "master_entry_ids": [
    "S02_individual",
    "S02_skills_and_talents"
  ],
  "parent_id": "GLOBAL-INDIVIDUAL-CORE-ECOSYSTEM",
  "status": "CORE_CATALOG_ONLY",
  "connected": false,
  "api_transport_in_core": false,
  "persistence_enabled": false
}
def get_module_metadata(): return dict(MODULE)
