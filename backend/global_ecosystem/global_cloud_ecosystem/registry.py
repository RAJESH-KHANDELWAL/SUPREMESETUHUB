"""Read-only facade for the cloud provider catalog."""
from .catalog import get_cloud_provider,list_cloud_providers,validate_cloud_catalog
__all__=["get_cloud_provider","list_cloud_providers","validate_cloud_catalog"]
