from global_domain_ecosystem.catalog import get_domain_catalog
from global_domain_ecosystem.classification import classify_domain
from global_domain_ecosystem.adult_domains import validate_adult_domain

def test_catalog_has_bharat_global_and_supreme():
    data = get_domain_catalog()
    assert "bharat_india" in data["geographic_scopes"]
    assert "global_cross_border" in data["geographic_scopes"]
    assert "supreme_long_horizon" in data["maturity_levels"]

def test_adult_category_is_explicit_and_separate():
    assert classify_domain("adult_entertainment")["group"] == "adult_only_media_and_services"

def test_adult_validation_requires_safeguards():
    assert not validate_adult_domain([])["eligible_for_design_review"]
