"""Manager for the CONSUMER_DEVICES_AND_SMART_HOME Google Core domain."""
from ..domain_runtime import GoogleCoreDomainManager


class DevicesSmartHomeDomainManager(GoogleCoreDomainManager):
    DOMAIN_ID = "CONSUMER_DEVICES_AND_SMART_HOME"


def get_manager() -> DevicesSmartHomeDomainManager:
    return DevicesSmartHomeDomainManager()


__all__ = ["DevicesSmartHomeDomainManager", "get_manager"]
