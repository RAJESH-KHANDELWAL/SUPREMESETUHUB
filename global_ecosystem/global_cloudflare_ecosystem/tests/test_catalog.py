from global_ecosystem.global_cloudflare_ecosystem import get_cloudflare_catalog, validate_cloudflare_catalog

def test_catalog_is_structurally_valid():
    assert validate_cloudflare_catalog()==()

def test_catalog_does_not_claim_live_connection():
    data=get_cloudflare_catalog()
    assert data["integration_status"]=="catalog_only"
    assert data["live_connection_verified"] is False

def test_catalog_returns_detached_data():
    data=get_cloudflare_catalog()
    data["products"].clear()
    assert get_cloudflare_catalog()["products"]
