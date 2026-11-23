"""Family-specific Atlassian Core service entry point."""
from ..module_service import AtlassianProductCoreService

class ConfluenceCoreService(AtlassianProductCoreService):
    ECOSYSTEM_ID = "ATLASSIAN-CONFLUENCE-CORE-ECOSYSTEM"
