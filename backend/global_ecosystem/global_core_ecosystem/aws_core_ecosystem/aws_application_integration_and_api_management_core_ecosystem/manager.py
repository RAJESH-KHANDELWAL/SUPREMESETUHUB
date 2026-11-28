"""Manager for the Application Integration and API Management AWS Core domain."""
from ..domain_runtime import AwsCoreDomainManager
class ApplicationIntegrationAndApiManagementDomainManager(AwsCoreDomainManager):
 DOMAIN_ID="APPLICATION_INTEGRATION_AND_API_MANAGEMENT"
def get_manager()->ApplicationIntegrationAndApiManagementDomainManager:return ApplicationIntegrationAndApiManagementDomainManager()
__all__=["ApplicationIntegrationAndApiManagementDomainManager","get_manager"]
