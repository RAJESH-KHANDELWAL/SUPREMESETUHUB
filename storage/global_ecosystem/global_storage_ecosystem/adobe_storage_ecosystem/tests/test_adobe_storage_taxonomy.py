from ..ecosystem_taxonomy import load_taxonomy, list_ecosystems, find_ecosystem
def test_taxonomy_has_nine_categories():
    taxonomy = load_taxonomy()
    assert taxonomy["ecosystem_id"] == "ADOBE_STORAGE_ECOSYSTEM"
    assert sum(len(group["categories"]) for group in taxonomy["groups"]) == 9
def test_catalog_rows_are_not_connected():
    rows = list_ecosystems()
    assert len(rows) == 9
    assert all(row["status"] == "CATALOG_ONLY" for row in rows)
    assert all(row["external_connection_state"] == "NOT_CONFIGURED" for row in rows)
def test_lookup_by_category():
    assert find_ecosystem("frameio") is not None
