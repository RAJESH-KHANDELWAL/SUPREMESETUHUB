from backend.google.google_ecosystem.service import GoogleEcosystemService, GOOGLE_PRODUCTS
from backend.api.google_ecosystem import router
from backend.security.dependencies import require_admin


def test_google_product_catalog_includes_requested_services():
    products = GoogleEcosystemService().catalog()
    ids = {item["id"] for item in products}
    assert {"gmail", "drive", "google_one", "cloud", "meet", "youtube", "google_gemini", "google_business_profile", "firebase", "bigquery"} <= ids
    assert len(products) >= 50


def test_google_one_does_not_claim_a_general_public_api():
    product = GoogleEcosystemService().get_product("google_one")
    assert product["availability"] == "NO_GENERAL_PUBLIC_GOOGLE_ONE_API"
    assert product["integration_mode"] == "PRODUCT_INFORMATION_ONLY"


def test_google_registry_does_not_claim_live_connections():
    status = GoogleEcosystemService().status()
    assert status["live_connection_verified"] is False
    assert status["token_storage_status"] == "NOT_IMPLEMENTED"
    assert status["ecosystem"] == "google_ecosystem"
    assert all(item["connected"] is False for item in status["products"])


def test_google_ecosystem_router_requires_admin():
    assert any(item.dependency is require_admin for item in router.dependencies)
    for route in router.routes:
        assert any(dep.call is require_admin for dep in route.dependant.dependencies)
