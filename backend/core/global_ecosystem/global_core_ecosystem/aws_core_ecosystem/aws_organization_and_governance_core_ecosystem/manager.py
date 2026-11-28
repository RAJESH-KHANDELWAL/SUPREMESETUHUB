"""Manager for the Organization and Governance AWS Core domain."""
from ..domain_runtime import AwsCoreDomainManager
class OrganizationAndGovernanceDomainManager(AwsCoreDomainManager):
 DOMAIN_ID="ORGANIZATION_AND_GOVERNANCE"
def get_manager()->OrganizationAndGovernanceDomainManager:return OrganizationAndGovernanceDomainManager()
__all__=["OrganizationAndGovernanceDomainManager","get_manager"]
