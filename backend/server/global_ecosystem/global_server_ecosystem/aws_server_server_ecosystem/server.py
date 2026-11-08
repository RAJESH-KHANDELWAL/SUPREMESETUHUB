"""SERVER-layer entry point for the Amazon Web Services provider namespace.

This module exposes SERVER-owned provider metadata and the existing adapter
binding. It does not create a remote connection or claim provisioning support.
"""
from .provider import PROVIDER_ID, DISPLAY_NAME, OWNING_DOMAIN, ADAPTER_CLASS

LAYER = "SERVER"
PACKAGE_KIND = "PROVIDER_SERVER_ECOSYSTEM"


def describe_server_provider():
    return {
        "layer": LAYER,
        "provider_id": PROVIDER_ID,
        "display_name": DISPLAY_NAME,
        "owning_domain": OWNING_DOMAIN,
        "package_kind": PACKAGE_KIND,
        "adapter_class": ADAPTER_CLASS.__name__,
        "connection_status": "NOT_PROBED",
    }


__all__ = ["LAYER", "PACKAGE_KIND", "describe_server_provider"]
