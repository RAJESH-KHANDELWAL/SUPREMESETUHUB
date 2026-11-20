"""Manager for the Networking and Edge AWS Core domain."""
from ..domain_runtime import AwsCoreDomainManager
class NetworkingAndEdgeDomainManager(AwsCoreDomainManager):
 DOMAIN_ID="NETWORKING_AND_EDGE"
def get_manager()->NetworkingAndEdgeDomainManager:return NetworkingAndEdgeDomainManager()
__all__=["NetworkingAndEdgeDomainManager","get_manager"]
