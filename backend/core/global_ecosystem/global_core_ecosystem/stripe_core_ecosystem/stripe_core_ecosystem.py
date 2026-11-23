"""Public Stripe Core compatibility entry point."""
from .catalog import STRIPE_CORE_ECOSYSTEM,get_stripe_core_catalog,list_stripe_core_modules
from .manager import StripeCoreManager,get_manager
from .service import StripeCoreEcosystemService
__all__=["STRIPE_CORE_ECOSYSTEM","get_stripe_core_catalog","list_stripe_core_modules","StripeCoreEcosystemService","StripeCoreManager","get_manager"]
