from backend.api.domain_hosting_catalog import public_domain_hosting_catalog


def test_public_catalog_is_inquiry_only_and_discloses_no_fake_prices():
    result = public_domain_hosting_catalog()

    assert result["success"] is True
    assert result["mode"] == "inquiry_only"
    assert result["currency"] is None
    assert len(result["services"]) >= 5
    assert all(service["checkout_enabled"] is False for service in result["services"])
    assert all(service["provider_connection"] == "not_configured" for service in result["services"])
    assert all("price" not in service for service in result["services"])
    assert "live domain availability" in result["notice"]
