from global_ecosystem.global_cloudflare_ecosystem import (
    get_cloudflare_catalog, validate_cloudflare_catalog,
)

def test_catalog_is_structurally_valid():
    assert validate_cloudflare_catalog() == ()

def test_catalog_does_not_claim_live_connection():
    catalog = get_cloudflare_catalog()
    assert catalog["integration_status"] == "catalog_only"
    assert catalog["live_connection_verified"] is False

def test_catalog_returns_detached_data():
    catalog = get_cloudflare_catalog()
    catalog["products"].clear()
    assert get_cloudflare_catalog()["products"]
