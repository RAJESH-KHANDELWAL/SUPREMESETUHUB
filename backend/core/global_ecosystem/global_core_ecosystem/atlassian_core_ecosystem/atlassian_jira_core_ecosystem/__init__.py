"""Public exports for atlassian_jira_core_ecosystem."""
from .service import JiraCoreService
from .manager import JiraCoreManager,get_manager
__all__=["JiraCoreService","JiraCoreManager","get_manager"]
