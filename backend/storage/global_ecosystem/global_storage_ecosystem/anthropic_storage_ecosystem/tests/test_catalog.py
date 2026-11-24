from ..anthropic_storage_ecosystem import CHILD_ECOSYSTEMS, describe, load_manifest


def test_child_catalog_matches_manifest():
    manifest = load_manifest()
    assert tuple(manifest["child_storage_ecosystems"]) == CHILD_ECOSYSTEMS
    assert len(CHILD_ECOSYSTEMS) == 8


def test_describe_does_not_claim_live_connection():
    result = describe()
    assert result["connection_state"] == "NOT_CONFIGURED"
    assert result["external_connections_verified"] is False
    assert result["taxonomy_only"] is True
