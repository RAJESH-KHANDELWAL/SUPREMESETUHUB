from backend.core.global_ecosystem.global_core_ecosystem.global_server_core_ecosystem import (
    CoreResult, Readiness, SecretReference, ServerCoreOrchestrator,
    ServerCorePolicy, ServerCoreService, TenantContext, get_catalog,
    server_core_domain_summary,
)
from backend.core.global_ecosystem.global_core_ecosystem.global_server_core_ecosystem.module_service import ServerProviderCoreService


def test_server_core_catalog_preserves_provider_and_scope_counts():
    catalog = get_catalog()
    assert catalog["ecosystem_id"] == "GLOBAL-SERVER-CORE-ECOSYSTEM"
    assert catalog["provider_count"] == 7
    assert catalog["core_domain_count"] == 16
    assert catalog["workload_domain_count"] == 20
    assert [item["tier_id"] for item in catalog["service_tiers"]] == [
        "NORMAL", "BASIC", "STANDARD", "PREMIUM", "PROFESSIONAL", "ENTERPRISE", "SUPREME"
    ]


def test_server_core_domain_summary_is_registry_backed():
    summary = server_core_domain_summary()
    assert summary["domain_count"] == 16
    assert summary["workload_domain_count"] == 20
    assert len(summary["domains"]) == 16


def test_server_core_health_does_not_claim_live_provider_connections():
    health = ServerCoreOrchestrator().health()
    assert health["status"] == "CORE_CATALOG_AVAILABLE"
    assert health["readiness"] == Readiness.METADATA_AVAILABLE.value
    assert health["live_provider_connections_verified"] == 0
    assert health["api_calls_performed"] == 0
    assert health["remote_operations_enabled"] is False


def test_policy_requires_tenant_context_and_registered_provider_capability():
    class AWSCore(ServerProviderCoreService):
        PROVIDER_ID = "AWS"
    service = AWSCore()
    capability = service.capabilities()["capabilities"][0]["name"]
    denied = service.authorize_capability(capability, None)
    assert denied["success"] is False
    assert denied["status"] == "POLICY_DENIED"
    allowed = service.authorize_capability(
        capability, TenantContext(tenant_id="tenant-test", actor_id="actor-test")
    )
    assert allowed["success"] is True
    assert allowed["data"]["api_call_performed"] is False
    assert allowed["status"] == "CORE_POLICY_PASSED_PROVIDER_AUTH_STILL_REQUIRED"


def test_secret_reference_is_opaque_and_policy_redacts_nested_secrets():
    ref = SecretReference(provider="vault", reference="kv/server/provider", version="1")
    assert ref.reference == "kv/server/provider"
    safe = ServerCorePolicy.safe_summary({
        "provider": "aws",
        "metadata": {"region": "ap-south-1", "access_token": "must-not-leak",
                     "nested": [{"private_key": "must-not-leak", "label": "safe"}]},
    })
    assert "access_token" not in safe["metadata"]
    assert "private_key" not in safe["metadata"]["nested"][0]
    assert safe["metadata"]["nested"][0]["label"] == "safe"


def test_server_core_service_identity_registration_is_process_local():
    service = ServerCoreService()
    result = service.register_identity({
        "server_id": "test-server-001", "provider_id": "AWS",
        "server_type": "vps", "server_role": "test",
        "country": "IN", "region": "ap-south-1",
        "environment": "test", "metadata": {"purpose": "unit-test"},
    })
    assert result["success"] is True
    assert result["persistence"] == "PROCESS_LOCAL_ONLY"
    assert service.get_identity("test-server-001")["success"] is True


def test_dependency_map_is_metadata_only():
    result = ServerCoreOrchestrator().dependency_map()
    assert result["success"] is True
    assert len(result["edges"]) == 7
    assert all(edge["live_connection_verified"] is False for edge in result["edges"])
    assert all(edge["api_calls_performed"] == 0 for edge in result["edges"])


def test_tenant_and_secret_contracts_reject_invalid_types():
    import pytest

    with pytest.raises(ValueError, match="TENANT_ID_REQUIRED"):
        TenantContext(tenant_id=None, actor_id="actor").validate()
    with pytest.raises(ValueError, match="ACTOR_ID_REQUIRED"):
        TenantContext(tenant_id="tenant", actor_id=" ").validate()
    with pytest.raises(ValueError, match="SECRET_PROVIDER_REQUIRED"):
        SecretReference(provider=None, reference="secret/path")
    with pytest.raises(ValueError, match="SECRET_REFERENCE_REQUIRED"):
        SecretReference(provider="vault", reference=" ")



def test_backend_server_and_global_server_are_separate_main_registrations():
    from backend.core.global_ecosystem.global_core_ecosystem.manager import GlobalEcosystemManager

    manager = GlobalEcosystemManager()
    backend_server = manager.get("BACKEND-SERVER-ECOSYSTEM")
    global_server = manager.get("GLOBAL-SERVER-ECOSYSTEM")
    server_core = manager.get("GLOBAL-SERVER-CORE-ECOSYSTEM")

    assert backend_server is not None
    assert global_server is not None
    assert server_core is not None
    assert len({backend_server["ecosystem_id"], global_server["ecosystem_id"], server_core["ecosystem_id"]}) == 3
    assert backend_server["parent_id"] == manager.ROOT_ID
    assert global_server["parent_id"] == manager.ROOT_ID
    assert server_core["parent_id"] == manager.CORE_ID
