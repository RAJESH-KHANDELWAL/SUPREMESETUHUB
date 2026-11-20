"""Read-only Individual Adult Live Streaming metadata contract; no API or persistence."""
MODULE={
  "module_id": "INDIVIDUAL-ADULT-LIVE-STREAMING-CORE-ECOSYSTEM",
  "directory": "individual_adult_live_streaming_core_ecosystem",
  "name": "Individual Adult Live Streaming",
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
