from ..catalog_api import AdobeStorageCatalog
def test_catalog_lists_and_filters():
    catalog = AdobeStorageCatalog()
    assert len(catalog.list()) == 9
    assert len(catalog.list("DOCUMENTS")) == 1
    assert catalog.get("frameio") is not None
    assert catalog.get("unknown") is None
def test_health_does_not_claim_external_connection():
    result = AdobeStorageCatalog().health()
    assert result["external_connections_verified"] is False
