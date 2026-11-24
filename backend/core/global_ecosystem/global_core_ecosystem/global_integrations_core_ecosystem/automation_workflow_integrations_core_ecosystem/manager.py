"""Manager for the AUTOMATION_WORKFLOW integration domain."""
from ..domain_runtime import IntegrationDomainManager
class AutomationWorkflowDomainManager(IntegrationDomainManager):
    DOMAIN_ID="AUTOMATION_WORKFLOW"
def get_manager(): return AutomationWorkflowDomainManager()
__all__=["AutomationWorkflowDomainManager","get_manager"]
