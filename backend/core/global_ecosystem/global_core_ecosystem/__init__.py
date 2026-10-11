"""GLOBAL CORE ECOSYSTEM implementation package inside CORE → GLOBAL ECOSYSTEM."""
from .catalog import get_catalog, get_category_catalog, get_registration_catalog
from .manager import EcosystemManager, GlobalEcosystemManager
from .models import EcosystemIdentity, GlobalEcosystemIdentity
from .registry import EcosystemRegistry, GlobalEcosystemRegistry
from .referral_service import SupremeReferralService

__all__ = [
    "get_catalog", "get_category_catalog", "get_registration_catalog",
    "EcosystemManager", "GlobalEcosystemManager",
    "EcosystemIdentity", "GlobalEcosystemIdentity",
    "EcosystemRegistry", "GlobalEcosystemRegistry", "SupremeReferralService",
]
