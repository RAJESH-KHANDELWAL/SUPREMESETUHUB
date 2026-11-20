"""Manager for the Infrastructure Provisioning and Automation AWS Core domain."""
from ..domain_runtime import AwsCoreDomainManager
class InfrastructureProvisioningAndAutomationDomainManager(AwsCoreDomainManager):
 DOMAIN_ID="INFRASTRUCTURE_PROVISIONING_AND_AUTOMATION"
def get_manager()->InfrastructureProvisioningAndAutomationDomainManager:return InfrastructureProvisioningAndAutomationDomainManager()
__all__=["InfrastructureProvisioningAndAutomationDomainManager","get_manager"]
