"""Service identifiers and endpoint metadata for Oracle Cloud Infrastructure."""

OCI_SERVICES = {
    "identity": {
        "service": "Identity",
        "description": "Compartments, users, groups, policies and IAM resources.",
        "api_family": "Identity and Access Management",
    },
    "compute": {
        "service": "Compute",
        "description": "Compute instances, images and instance configurations.",
        "api_family": "Compute",
    },
    "network": {
        "service": "VirtualNetwork",
        "description": "Virtual cloud networks, subnets, gateways and security lists.",
        "api_family": "Networking",
    },
    "object_storage": {
        "service": "ObjectStorage",
        "description": "Namespaces, buckets and object operations.",
        "api_family": "Storage",
    },
    "database": {
        "service": "Database",
        "description": "Database systems, Autonomous Databases and lifecycle operations.",
        "api_family": "Database",
    },
    "generative_ai": {
        "service": "GenerativeAi",
        "description": "Generative AI resources and endpoints where enabled.",
        "api_family": "AI",
    },
}

def get_service_metadata(service_id: str) -> dict[str, str] | None:
    """Return a copy of service metadata for a known OCI service identifier."""
    item = OCI_SERVICES.get(service_id.strip().lower())
    return dict(item) if item else None


__all__ = ["OCI_SERVICES", "get_service_metadata"]
