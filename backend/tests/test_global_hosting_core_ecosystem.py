from backend.core.global_ecosystem.global_core_ecosystem.global_hosting_core_ecosystem import (
    GlobalHostingCoreEcosystemService, GlobalHostingCoreOrchestrator,
    HostingCorePolicy, HostingTenantContext, get_hosting_provider,
    list_hosting_capability_packages, list_hosting_providers,
)

def test_hosting_inventory_matches_supplied_snapshot():
    providers = list_hosting_providers()
    packages = list_hosting_capability_packages()
    assert len(providers) == 111
    assert len({item["provider_id"] for item in providers}) == 111
    assert len(packages) == 7
    assert len(providers) + len(packages) == 118
    assert all(item["status"] == "CORE_CATALOG_ONLY" for item in providers)
    assert all(item["live_connection_verified"] is False for item in providers)
    assert all(item["api_available"] is None for item in providers)

def test_provider_lookup_and_category_filter():
    assert get_hosting_provider("Hostinger")["provider_id"] == "hostinger"
    assert get_hosting_provider("unknown") is None
    assert all(item["category"] == "PLATFORM_AS_A_SERVICE"
               for item in list_hosting_providers(category="PLATFORM_AS_A_SERVICE"))

def test_policy_requires_authenticated_tenant_context():
    try:
        HostingCorePolicy.require_tenant_context(None)
        assert False, "missing tenant context must be denied"
    except PermissionError:
        pass
    context = HostingTenantContext(tenant_id="tenant-test", actor_id="actor-test")
    context.validate()

def test_policy_recursively_filters_secret_fields():
    result = HostingCorePolicy.sanitize({"name":"host", "nested":{"access_key":"x","ok":True}})
    assert result == {"name":"host","nested":{"ok":True}}

def test_health_and_service_never_claim_live_connections():
    health = GlobalHostingCoreOrchestrator().health()
    assert health["provider_count"] == 111
    assert health["capability_package_count"] == 7
    assert health["hosting_related_child_folder_count"] == 118
    assert health["live_connection_verified_count"] == 0
    assert health["api_calls_performed"] == 0
    status = GlobalHostingCoreEcosystemService().status()
    assert status["live_connection_verified"] is False
