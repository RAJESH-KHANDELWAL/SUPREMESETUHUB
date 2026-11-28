"""Manager for the Compute and Containers AWS Core domain."""
from ..domain_runtime import AwsCoreDomainManager
class ComputeAndContainersDomainManager(AwsCoreDomainManager):
 DOMAIN_ID="COMPUTE_AND_CONTAINERS"
def get_manager()->ComputeAndContainersDomainManager:return ComputeAndContainersDomainManager()
__all__=["ComputeAndContainersDomainManager","get_manager"]
