"""Global Domain Core inventory and contract tests."""
from .catalog import get_catalog, PROVIDER_DIRECTORIES, DOMAIN_DEFINITIONS
from .domain_runtime import DomainCoreRuntime
from .manager import get_manager
def test_provider_inventory_is_nonempty_and_unique():
    assert len(PROVIDER_DIRECTORIES)>50
    assert len(set(PROVIDER_DIRECTORIES))==len(PROVIDER_DIRECTORIES)
def test_domain_catalog_has_expected_definitions():
    assert len(DOMAIN_DEFINITIONS)>=15
    assert all(v.get("purpose") for v in DOMAIN_DEFINITIONS.values())
def test_manager_status_is_catalog_only():
    status=get_manager().status()
    assert status["success"] is True
    assert status["live_connection_verified"] is False
def test_domain_service_unknown_domain_is_safe():
    result=get_manager().get_domain_manager("NOT_A_DOMAIN").status()
    assert result["success"] is False
