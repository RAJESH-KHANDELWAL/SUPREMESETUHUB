"""Domain manager for DevOps and Delivery."""
from ..domain_runtime import SoftwareCoreDomainManager
class DevopsAndDeliveryManager(SoftwareCoreDomainManager):
    DOMAIN_ID="DEVOPS_AND_DELIVERY"
def get_manager(): return DevopsAndDeliveryManager()
