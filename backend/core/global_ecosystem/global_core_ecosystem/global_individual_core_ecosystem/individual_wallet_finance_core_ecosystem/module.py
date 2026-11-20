"""Read-only Individual Wallet Finance metadata contract; no API or persistence."""
MODULE={
  "module_id": "INDIVIDUAL-WALLET-FINANCE-CORE-ECOSYSTEM",
  "directory": "individual_wallet_finance_core_ecosystem",
  "name": "Individual Wallet Finance",
  "master_entry_ids": [
    "S02_individual",
    "S02_human_identity"
  ],
  "parent_id": "GLOBAL-INDIVIDUAL-CORE-ECOSYSTEM",
  "status": "CORE_CATALOG_ONLY",
  "connected": false,
  "api_transport_in_core": false,
  "persistence_enabled": false
}
def get_module_metadata(): return dict(MODULE)
