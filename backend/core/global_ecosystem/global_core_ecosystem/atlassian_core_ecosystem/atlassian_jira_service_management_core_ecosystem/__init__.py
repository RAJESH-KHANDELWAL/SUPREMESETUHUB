"""Public exports for atlassian_jira_service_management_core_ecosystem."""
from .service import JiraServiceManagementCoreService
from .manager import JiraServiceManagementCoreManager,get_manager
__all__=["JiraServiceManagementCoreService","JiraServiceManagementCoreManager","get_manager"]
