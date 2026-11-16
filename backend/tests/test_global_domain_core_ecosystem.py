from backend.core.global_ecosystem.global_core_ecosystem.global_domain_core_ecosystem import (
    DomainCorePolicy, DomainTenantContext, GlobalDomainCoreEcosystemService,
    GlobalDomainCoreOrchestrator, get_domain_provider, list_domain_providers,
)


def test_domain_provider_inventory_matches_supplied_snapshot():
    providers = list_domain_providers()
    assert len(providers) == 78
    assert len({item["provider_id"] for item in providers}) == 78
    assert all(item["status"] == "CORE_CATALOG_ONLY" for item in providers)
    assert all(item["live_connection_verified"] is False for item in providers)


def test_provider_lookup_is_case_insensitive():
    assert get_domain_provider("GoDaddy")["provider_id"] == "godaddy"
    assert get_domain_provider("missing-provider") is None


def test_orchestrator_reports_catalog_not_live_connections():
    health = GlobalDomainCoreOrchestrator().health()
    assert health["provider_count"] == 78
    assert health["live_connections_verified"] == 0
    assert health["api_calls_performed"] == 0


def test_policy_requires_tenant_context_and_registered_capability():
    provider = get_domain_provider("cloudflare")
    try:
        DomainCorePolicy.require_tenant_context(None)
        assert False, "missing tenant context must be denied"
    except PermissionError:
        pass
    DomainCorePolicy.validate_capability(provider, provider["capabilities"][0])
    context = DomainTenantContext(tenant_id="tenant-test", actor_id="actor-test")
    context.validate()


def test_secret_fields_are_recursively_filtered():
    safe = DomainCorePolicy.sanitize({"name": "provider", "nested": {"api_token": "x", "ok": True}})
    assert safe == {"name": "provider", "nested": {"ok": True}}


def test_service_does_not_claim_live_connection():
    status = GlobalDomainCoreEcosystemService().status()
    assert status["provider_count"] == 78
    assert status["live_connection_verified"] is False
