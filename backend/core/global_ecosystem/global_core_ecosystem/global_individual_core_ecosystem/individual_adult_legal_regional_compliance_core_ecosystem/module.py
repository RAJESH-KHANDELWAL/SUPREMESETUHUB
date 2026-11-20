"""Read-only Individual Adult Legal Regional Compliance metadata contract; no API or persistence."""
MODULE={
  "module_id": "INDIVIDUAL-ADULT-LEGAL-REGIONAL-COMPLIANCE-CORE-ECOSYSTEM",
  "directory": "individual_adult_legal_regional_compliance_core_ecosystem",
  "name": "Individual Adult Legal Regional Compliance",
  "master_entry_ids": [
    "S02_human_rights",
    "S02_adults"
  ],
  "parent_id": "GLOBAL-INDIVIDUAL-CORE-ECOSYSTEM",
  "status": "CORE_CATALOG_ONLY",
  "connected": False,
  "api_transport_in_core": False,
  "persistence_enabled": False
}
def get_module_metadata(): return dict(MODULE)
