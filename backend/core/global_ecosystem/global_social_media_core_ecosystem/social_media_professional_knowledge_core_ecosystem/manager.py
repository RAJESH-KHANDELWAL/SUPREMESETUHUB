from ..domain_runtime import SocialMediaCoreDomainManager
class DomainManager(SocialMediaCoreDomainManager):
    DOMAIN_ID="PROFESSIONAL_KNOWLEDGE_AND_DISCUSSION"
def get_manager()->DomainManager:return DomainManager()
__all__=["DomainManager","get_manager"]
