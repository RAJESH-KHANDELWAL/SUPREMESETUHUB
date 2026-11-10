"""Bharat-to-global cloud ecosystem namespace: providers, capabilities, scope and workloads."""
from .catalog import get_cloud_provider, list_cloud_providers, validate_cloud_catalog
from .capabilities import CLOUD_CAPABILITIES
from .scope import CLOUD_SCOPES
from .workloads import get_cloud_workload, list_cloud_workloads, validate_cloud_workloads

__all__ = [
    "get_cloud_provider", "list_cloud_providers", "validate_cloud_catalog",
    "CLOUD_CAPABILITIES", "CLOUD_SCOPES",
    "get_cloud_workload", "list_cloud_workloads", "validate_cloud_workloads",
]
