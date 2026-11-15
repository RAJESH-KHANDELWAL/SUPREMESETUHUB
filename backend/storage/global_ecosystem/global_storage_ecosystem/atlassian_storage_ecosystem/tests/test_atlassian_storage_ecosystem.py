"""Offline tests for the Atlassian storage catalog."""
from ..atlassian_storage_ecosystem import CHILD_ECOSYSTEMS, describe, load_manifest


def test_manifest_matches_product_catalog():
    manifest = load_manifest()
    assert len(manifest["product_catalog"]) == 8
    assert tuple(item["package"] for item in manifest["product_catalog"]) == CHILD_ECOSYSTEMS


def test_catalog_does_not_claim_live_connections():
    result = describe()
    assert result["taxonomy_only"] is True
    assert result["external_connections_verified"] is False
    assert result["connection_state"] == "NOT_CONFIGURED"
