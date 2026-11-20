"""Read-only Individual Adult Subscription Membership metadata contract; no API or persistence."""
MODULE={
  "module_id": "INDIVIDUAL-ADULT-SUBSCRIPTION-MEMBERSHIP-CORE-ECOSYSTEM",
  "directory": "individual_adult_subscription_membership_core_ecosystem",
  "name": "Individual Adult Subscription Membership",
  "master_entry_ids": [
    "S02_adults",
    "S02_individual"
  ],
  "parent_id": "GLOBAL-INDIVIDUAL-CORE-ECOSYSTEM",
  "status": "CORE_CATALOG_ONLY",
  "connected": false,
  "api_transport_in_core": false,
  "persistence_enabled": false
}
def get_module_metadata(): return dict(MODULE)
