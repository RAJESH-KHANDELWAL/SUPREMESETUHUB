from backend.google.google_ecosystem.service import GoogleEcosystemService, GOOGLE_PRODUCTS


def test_google_ecosystem_catalog_covers_major_product_families():
    ids = set(GOOGLE_PRODUCTS)
    expected = {
        "gmail", "drive", "calendar", "docs", "sheets", "meet",
        "google_workspace_admin", "google_classroom", "google_appsheet",
        "google_apps_script", "google_blogger", "cloud", "firebase",
        "firebase_authentication", "cloud_firestore", "firebase_hosting",
        "google_cloud_iam", "google_secret_manager", "google_cloud_logging",
        "google_cloud_monitoring", "google_cloud_build", "bigquery",
        "google_gemini", "vertex_ai", "google_vertex_ai_search",
        "google_dialogflow", "google_ads", "google_adsense", "google_admob",
        "google_merchant_center", "google_street_view", "youtube", "photos",
        "google_wallet", "google_pay", "google_nest", "google_pixel",
    }
    assert expected <= ids
    assert len(ids) >= 120


def test_catalog_entries_have_required_metadata():
    for product_id, product in GOOGLE_PRODUCTS.items():
        assert product_id
        assert product.get("name")
        assert product.get("category")
        assert "integration_mode" in product
        assert "availability" in product


def test_catalog_expansion_does_not_claim_live_connections():
    status = GoogleEcosystemService().status()
    assert status["live_connection_verified"] is False
    assert status["token_storage_status"] == "NOT_IMPLEMENTED"
    assert all(item["connected"] is False for item in status["products"])
