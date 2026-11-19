"""Family-specific Atlassian Core service entry point."""
from ..module_service import AtlassianProductCoreService

class JiraServiceManagementCoreService(AtlassianProductCoreService):
    ECOSYSTEM_ID = "ATLASSIAN-JIRA-SERVICE-MANAGEMENT-CORE-ECOSYSTEM"
