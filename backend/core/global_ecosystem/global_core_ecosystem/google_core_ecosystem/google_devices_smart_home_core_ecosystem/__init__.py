"""CONSUMER DEVICES AND SMART HOME Google Core domain package."""
from .manager import DevicesSmartHomeDomainManager, get_manager

DOMAIN_ID = "CONSUMER_DEVICES_AND_SMART_HOME"
__all__ = ["DOMAIN_ID", "DevicesSmartHomeDomainManager", "get_manager"]
