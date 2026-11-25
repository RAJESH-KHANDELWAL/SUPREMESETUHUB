"""Automation & Workflow domain package."""
from .manager import AutomationWorkflowDomainManager, get_manager
DOMAIN_ID="AUTOMATION_WORKFLOW"
__all__=["DOMAIN_ID","AutomationWorkflowDomainManager","get_manager"]
