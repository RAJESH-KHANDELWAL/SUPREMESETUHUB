"""Family-specific Atlassian Core service entry point."""
from ..module_service import AtlassianProductCoreService

class JiraCoreService(AtlassianProductCoreService):
    ECOSYSTEM_ID = "ATLASSIAN-JIRA-CORE-ECOSYSTEM"
