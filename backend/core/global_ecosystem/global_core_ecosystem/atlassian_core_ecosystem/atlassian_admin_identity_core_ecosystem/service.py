"""Family-specific Atlassian Core service entry point."""
from ..module_service import AtlassianProductCoreService

class AdminIdentityCoreService(AtlassianProductCoreService):
    ECOSYSTEM_ID = "ATLASSIAN-ADMIN-IDENTITY-CORE-ECOSYSTEM"
