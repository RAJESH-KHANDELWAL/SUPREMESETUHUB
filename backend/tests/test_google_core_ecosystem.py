from backend.core.global_ecosystem.global_core_ecosystem.google_core_ecosystem import (
    GoogleCoreEcosystemService,
    GoogleCoreOrchestrator,
    GoogleCorePolicy,
    TenantContext,
    get_google_core_catalog,
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
    assert health["product_count"] == 23
    assert health["live_connections_verified"] == 0
    assert health["api_calls_performed"] == 0


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
        capability,
        TenantContext(tenant_id="tenant-test", actor_id="user-test"),
    )
    assert allowed["success"] is True
    assert allowed["status"] == "CORE_POLICY_PASSED_API_AUTH_STILL_REQUIRED"
    assert allowed["data"]["api_call_performed"] is False


def test_google_core_service_does_not_claim_live_connection():
    status = GoogleCoreEcosystemService().status()
    assert status["module_count"] == 23
    assert status["live_connection_verified"] is False
