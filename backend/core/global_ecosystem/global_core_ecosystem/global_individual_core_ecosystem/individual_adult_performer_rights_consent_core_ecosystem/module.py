"""Read-only Individual Adult Performer Rights Consent metadata contract; no API or persistence."""
MODULE={
  "module_id": "INDIVIDUAL-ADULT-PERFORMER-RIGHTS-CONSENT-CORE-ECOSYSTEM",
  "directory": "individual_adult_performer_rights_consent_core_ecosystem",
  "name": "Individual Adult Performer Rights Consent",
  "master_entry_ids": [
    "S02_human_rights",
    "S02_adults"
  ],
  "parent_id": "GLOBAL-INDIVIDUAL-CORE-ECOSYSTEM",
  "status": "CORE_CATALOG_ONLY",
  "connected": false,
  "api_transport_in_core": false,
  "persistence_enabled": false
}
def get_module_metadata(): return dict(MODULE)
