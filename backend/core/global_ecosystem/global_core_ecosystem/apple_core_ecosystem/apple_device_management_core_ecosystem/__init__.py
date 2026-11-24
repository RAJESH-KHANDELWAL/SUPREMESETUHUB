"""APPLE_DEVICE_MANAGEMENT_CORE_ECOSYSTEM product-family Core package."""
from .service import AppleDeviceManagementCoreService
from .manager import AppleDeviceManagementCoreManager, get_manager
__all__=["AppleDeviceManagementCoreService","AppleDeviceManagementCoreManager","get_manager"]
