"""APPLE_STOREKIT_CORE_ECOSYSTEM product-family Core package."""
from .service import AppleStorekitCoreService
from .manager import AppleStorekitCoreManager, get_manager
__all__=["AppleStorekitCoreService","AppleStorekitCoreManager","get_manager"]
