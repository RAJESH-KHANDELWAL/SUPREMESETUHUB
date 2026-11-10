"""Bharat-to-global cloud provider ecosystem namespace."""
from .catalog import get_cloud_provider,list_cloud_providers,validate_cloud_catalog
from .capabilities import CLOUD_CAPABILITIES
from .scope import CLOUD_SCOPES
__all__=["get_cloud_provider","list_cloud_providers","validate_cloud_catalog","CLOUD_CAPABILITIES","CLOUD_SCOPES"]
