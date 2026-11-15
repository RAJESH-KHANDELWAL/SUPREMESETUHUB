"""Offline contract tests for the Anthropic storage catalog."""
from anthropic_storage_ecosystem import CHILD_ECOSYSTEMS, load_manifest
from catalog_api import AnthropicStorageCatalog

def test_manifest_and_catalog_match():
    manifest = load_manifest()
    catalog = AnthropicStorageCatalog()
    assert manifest["ecosystem_id"] == "ANTHROPIC_STORAGE_ECOSYSTEM"
    assert tuple(manifest["child_storage_ecosystems"]) == CHILD_ECOSYSTEMS
    assert len(catalog.list()) == len(CHILD_ECOSYSTEMS)

def test_catalog_does_not_claim_live_connection():
    assert AnthropicStorageCatalog().health()["external_connections_verified"] is False
