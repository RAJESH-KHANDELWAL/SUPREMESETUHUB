"""Manager for the ADULT_MODERATION_SAFETY_TAKEDOWN integration domain."""
from ..domain_runtime import IntegrationDomainManager
class AdultModerationSafetyTakedownDomainManager(IntegrationDomainManager):
    DOMAIN_ID="ADULT_MODERATION_SAFETY_TAKEDOWN"
def get_manager(): return AdultModerationSafetyTakedownDomainManager()
__all__=["AdultModerationSafetyTakedownDomainManager","get_manager"]
