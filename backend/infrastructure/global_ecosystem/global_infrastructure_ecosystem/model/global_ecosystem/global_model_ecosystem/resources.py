"""Normalized resource categories and resource type vocabulary."""
RESOURCE_CATEGORIES = {
    "compute": ("server", "dedicated_server", "vps", "cloud_server", "virtual_machine", "container"),
    "network": ("network", "subnet", "ip_address", "dns_zone", "firewall", "load_balancer", "vpn"),
    "storage": ("block_storage", "file_storage", "object_storage", "backup"),
    "data": ("database", "database_instance", "database_cluster", "cache"),
    "platform": ("hosting", "domain", "website", "application", "email"),
    "delivery": ("cdn", "edge_distribution", "api_gateway"),
    "security": ("certificate", "secret_reference", "identity", "access_policy"),
    "operations": ("monitor", "alert", "deployment", "recovery_plan"),
}

def list_resource_types() -> dict[str, tuple[str, ...]]:
    return {category: tuple(types) for category, types in RESOURCE_CATEGORIES.items()}
