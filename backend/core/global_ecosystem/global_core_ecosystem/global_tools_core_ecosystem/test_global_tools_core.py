"""Global Tools Core structural and behaviour tests."""
from importlib import import_module
from .catalog import list_providers
from .product_catalog import list_products
from .domain_catalog import DOMAIN_DEFINITIONS
from .domain_runtime import ToolsCoreDomainManager
from .manager import get_manager
from .contracts import TenantContext
from .policy import ToolsCorePolicy

def test_inventory():
    providers = list_providers()
    products = list_products()
    assert len(providers) == 28
    assert len(products) == 124
    assert len(DOMAIN_DEFINITIONS) == 20
    assert {x["provider_id"] for x in products} <= {x["provider_id"] for x in providers}
    assert len({x["provider_id"] for x in providers}) == len(providers)
    assert len({x["product_id"] for x in products}) == len(products)

def test_domain_managers():
    for domain_id in DOMAIN_DEFINITIONS:
        manager = ToolsCoreDomainManager(domain_id)
        assert manager.status()["domain_id"] == domain_id
        assert manager.list_offerings()["success"]

def test_health_is_honest():
    status = get_manager().status()
    assert status["success"]
    assert status["live_connections_verified"] is False

def test_policy_requires_tenant():
    try:
        ToolsCorePolicy.require_tenant(None)
    except PermissionError:
        pass
    else:
        raise AssertionError("missing tenant must be denied")
    ToolsCorePolicy.require_tenant(TenantContext("tenant", "actor"))

def test_validator():
    from .tools.validate_tools_catalog import validate
    result = validate()
    assert result["success"], result["errors"]
    assert result["provider_count"] == 28
    assert result["product_family_count"] == 124

def test_each_provider_facade_resolves():
    for provider in list_providers():
        module = import_module(f"{__package__}.{provider['provider_id']}_tools_core_ecosystem.manager")
        assert module.get_manager().status()["provider_id"] == provider["provider_id"]
