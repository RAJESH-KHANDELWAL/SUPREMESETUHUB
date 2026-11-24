"""Manager for the COMMUNICATION_SOCIAL_MEDIA integration domain."""
from ..domain_runtime import IntegrationDomainManager
class CommunicationSocialMediaDomainManager(IntegrationDomainManager):
    DOMAIN_ID="COMMUNICATION_SOCIAL_MEDIA"
def get_manager(): return CommunicationSocialMediaDomainManager()
__all__=["CommunicationSocialMediaDomainManager","get_manager"]
