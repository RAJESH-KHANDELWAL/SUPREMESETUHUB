"""Global Tools Core structural and behaviour tests."""
from .catalog import list_providers
from .product_catalog import list_products
from .domain_catalog import DOMAIN_DEFINITIONS
from .domain_runtime import ToolsCoreDomainManager
from .manager import get_manager
from .contracts import TenantContext
from .policy import ToolsCorePolicy
def test_inventory():
 assert len(list_providers())==11 and len(list_products())==56 and len(DOMAIN_DEFINITIONS)==20
 assert {x["provider_id"] for x in list_products()} <= {x["provider_id"] for x in list_providers()}
def test_domain_managers():
 for k in DOMAIN_DEFINITIONS:
  m=ToolsCoreDomainManager(k); assert m.status()["domain_id"]==k and m.list_offerings()["success"]
def test_health_is_honest():
 s=get_manager().status(); assert s["success"] and s["live_connections_verified"] is False
def test_policy_requires_tenant():
 try: ToolsCorePolicy.require_tenant(None)
 except PermissionError: pass
 else: raise AssertionError("missing tenant must be denied")
 ToolsCorePolicy.require_tenant(TenantContext("tenant","actor"))
def test_validator():
 from .tools.validate_tools_catalog import validate
 assert validate()["success"]
