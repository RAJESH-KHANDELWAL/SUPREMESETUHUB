from ..catalog import get_catalog
def test_catalog_covers_bharat_to_global_and_maturity():
    data = get_catalog()
    assert "bharat_india" in data["geographic_scopes"]
    assert "global_cross_border" in data["geographic_scopes"]
    assert data["maturity_levels"][0] == "normal"
    assert data["maturity_levels"][-1] == "supreme"
    assert "adult_only_content_technology" in data["domains"]
