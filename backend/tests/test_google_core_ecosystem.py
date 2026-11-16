from backend.core.global_ecosystem.global_core_ecosystem.google_core_ecosystem import (
    GoogleCoreEcosystemService,
    GoogleCoreOrchestrator,
    GoogleCorePolicy,
    TenantContext,
    get_google_core_catalog,
    google_domain_summary,
)
from backend.core.global_ecosystem.global_core_ecosystem.google_core_ecosystem.google_drive_core_ecosystem.service import (
    GoogleDriveCoreService,
)


def test_google_core_catalog_has_23_registered_product_families():
    catalog = get_google_core_catalog()
    assert catalog["ecosystem_id"] == "GOOGLE-CORE-ECOSYSTEM"
    assert len(catalog["children"]) == 23


def test_google_core_orchestrator_reports_catalog_not_live_connections():
    health = GoogleCoreOrchestrator().health()
    assert health["product_family_count"] == 23
    assert health["domain_count"] == 19
    assert health["runtime_offering_count"] == 129
    assert health["live_connections_verified"] == 0
    assert health["api_calls_performed"] == 0


def test_google_domain_inventory_covers_all_existing_runtime_offerings():
    summary = google_domain_summary()
    assert summary["domain_count"] == 19
    assert summary["offering_count"] == 129
    assert summary["assigned_offering_count"] == 129
    assert len(summary["domains"]) == 19
    assert sum(item["offering_count"] for item in summary["domains"]) == 129


def test_product_core_service_exposes_drive_capabilities_without_api_calls():
    service = GoogleDriveCoreService()
    status = service.status()
    assert status["ecosystem_id"] == "GOOGLE-DRIVE-CORE-ECOSYSTEM"
    assert status["api_transport_in_core"] is False
    assert status["live_connection_verified"] is False
    assert service.capabilities()["count"] > 0


def test_capability_policy_requires_tenant_context_and_registered_capability():
    service = GoogleDriveCoreService()
    capability = service.capabilities()["capabilities"][0]["name"]
    denied = service.authorize_capability(capability, None)
    assert denied["success"] is False
    assert denied["status"] == "POLICY_DENIED"
    allowed = service.authorize_capability(
        capability, TenantContext(tenant_id="tenant-test", actor_id="user-test")
    )
    assert allowed["success"] is True
    assert allowed["status"] == "CORE_POLICY_PASSED_API_AUTH_STILL_REQUIRED"
    assert allowed["data"]["api_call_performed"] is False


def test_google_core_service_does_not_claim_live_connection():
    status = GoogleCoreEcosystemService().status()
    assert status["module_count"] == 23
    assert status["domain_count"] == 19
    assert status["runtime_offering_count"] == 129
    assert status["live_connection_verified"] is False


def test_google_core_inventory_includes_all_existing_google_runtime_offerings():
    summary = GoogleCoreOrchestrator().offerings()
    assert summary["offering_count"] == 129
    assert summary["mapped_count"] + summary["specialized_review_count"] == 129
    assert all("availability" in item for item in summary["offerings"])
    assert all("core_family_id" in item for item in summary["offerings"])


def test_product_information_only_entries_are_not_claimed_as_api_connections():
    offerings = GoogleCoreOrchestrator().offerings()["offerings"]
    informational = [item for item in offerings if item["integration_mode"] == "PRODUCT_INFORMATION_ONLY"]
    assert informational
    assert all(item["api_available"] is False for item in informational)


def test_all_23_google_product_core_services_are_importable_and_catalog_backed():
    from importlib import import_module
    products = [
        "google_admin_sdk", "google_ads", "google_analytics", "google_business_profile",
        "google_calendar", "google_chat", "google_cloud", "google_contacts", "google_docs",
        "google_drive", "google_firebase", "google_forms", "google_gemini", "google_gmail",
        "google_identity_oauth", "google_maps_platform", "google_meet", "google_people",
        "google_search_console", "google_sheets", "google_slides", "google_vertex_ai", "google_youtube",
    ]
    root = "backend.core.global_ecosystem.global_core_ecosystem.google_core_ecosystem"
    assert len(products) == 23
    for product in products:
        module = import_module(f"{root}.{product}_core_ecosystem.service")
        service_types = [
            value for value in vars(module).values()
            if isinstance(value, type) and value.__module__ == module.__name__
        ]
        assert service_types, product
        status = service_types[0]().status()
        assert status["core_layer"] == "GOOGLE_CORE"
        assert status["live_connection_verified"] is False


def test_legacy_gmail_core_import_points_to_shared_product_core_service():
    from backend.core.global_ecosystem.global_core_ecosystem.google_core_ecosystem.gmail_core import GoogleGmailCoreService
    assert GoogleGmailCoreService().status()["ecosystem_id"] == "GOOGLE-GMAIL-CORE-ECOSYSTEM"
