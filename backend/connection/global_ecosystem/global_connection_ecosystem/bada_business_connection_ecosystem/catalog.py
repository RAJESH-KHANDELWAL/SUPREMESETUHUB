"""Bada Business connection capabilities; not a copy of its resource catalog."""

BADA_BUSINESS_CONNECTION_CAPABILITIES = {
    "resource_catalog_access": "Resolve canonical Bada Business resources through the existing backend catalog.",
    "integration_registration": "Register integration connection metadata in the bada_business namespace.",
    "approval_control": "Require explicit approval before connection authorization.",
    "adapter_dispatch": "Delegate live connection operations to an injected adapter.",
    "connection_health": "Expose safe status for Bada Business integration connections.",
}


def get_bada_business_connection_catalog():
    return {
        "name": "BADA BUSINESS CONNECTION ECOSYSTEM",
        "namespace": "bada_business",
        "version": "1.0",
        "capabilities": dict(BADA_BUSINESS_CONNECTION_CAPABILITIES),
        "canonical_resource_catalog": "backend.global_ecosystem.global_bada_business_ecosystem.platform_resources.catalog",
    }
