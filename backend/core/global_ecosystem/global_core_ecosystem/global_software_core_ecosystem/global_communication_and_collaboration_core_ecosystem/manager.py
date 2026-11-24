"""Domain manager for Communication and Collaboration."""
from ..domain_runtime import SoftwareCoreDomainManager
class CommunicationAndCollaborationManager(SoftwareCoreDomainManager):
    DOMAIN_ID="COMMUNICATION_AND_COLLABORATION"
def get_manager(): return CommunicationAndCollaborationManager()
