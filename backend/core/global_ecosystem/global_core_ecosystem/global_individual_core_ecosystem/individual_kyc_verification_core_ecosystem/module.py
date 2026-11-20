"""Read-only Individual KYC Verification metadata contract; no API or persistence."""
MODULE={
  "module_id": "INDIVIDUAL-KYC-VERIFICATION-CORE-ECOSYSTEM",
  "directory": "individual_kyc_verification_core_ecosystem",
  "name": "Individual KYC Verification",
  "master_entry_ids": [
    "S02_human_identity",
    "S02_human_rights"
  ],
  "parent_id": "GLOBAL-INDIVIDUAL-CORE-ECOSYSTEM",
  "status": "CORE_CATALOG_ONLY",
  "connected": False,
  "api_transport_in_core": False,
  "persistence_enabled": False
}
def get_module_metadata(): return dict(MODULE)
