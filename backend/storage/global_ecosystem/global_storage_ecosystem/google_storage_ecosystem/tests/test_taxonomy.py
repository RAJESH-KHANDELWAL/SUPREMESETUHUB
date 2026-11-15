"""Offline tests for the Google taxonomy catalog."""
from ..ecosystem_taxonomy import load_taxonomy, list_ecosystems, find_ecosystem
def test_catalog_naming_and_scope():
    data = load_taxonomy()
    assert data["provider"] == "GOOGLE"
    rows = list_ecosystems()
    assert len(rows) >= 100
    assert all(r["name"].startswith("GOOGLE_") and r["name"].endswith("_STORAGE_ECOSYSTEM") for r in rows)
def test_adult_classification_is_not_a_provider_claim():
    row = find_ecosystem("PORNOGRAPHIC_CONTENT")
    assert row is not None and row["status"] == "CATALOG_ONLY"
    assert row["provider_product_verified"] == "false"
def test_governance_controls():
    prohibited = load_taxonomy()["governance"]["prohibited_content"]
    assert "child sexual abuse material" in prohibited
    assert "non-consensual intimate imagery" in prohibited
