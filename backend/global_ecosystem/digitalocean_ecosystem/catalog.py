"""Provider-specific DigitalOcean products and capability metadata.

This is a documented catalog, not a claim that every product is enabled or
available in every account, region, or plan.
"""
from .models import Capability

CAPABILITIES = (
    Capability("droplets", "Droplets", "compute", "Create and manage cloud virtual machines.", ("droplet",), destructive=True),
    Capability("kubernetes", "DigitalOcean Kubernetes", "compute", "Managed Kubernetes clusters and node pools.", ("kubernetes_cluster", "node_pool"), destructive=True),
    Capability("app_platform", "App Platform", "application_platform", "Deploy and operate applications from source or container images.", ("app", "deployment")),
    Capability("functions", "Functions", "serverless", "Serverless function deployment and invocation.", ("function",)),
    Capability("managed_databases", "Managed Databases", "data", "Managed database clusters, users, pools, and backups.", ("database_cluster", "database_user"), destructive=True),
    Capability("spaces", "Spaces Object Storage", "storage", "S3-compatible object storage buckets and objects.", ("bucket", "object"), destructive=True),
    Capability("volumes", "Block Storage Volumes", "storage", "Attachable block storage volumes and snapshots.", ("volume", "snapshot"), destructive=True),
    Capability("container_registry", "Container Registry", "containers", "Private image registry and repository management.", ("registry", "repository")),
    Capability("load_balancers", "Load Balancers", "networking", "Traffic distribution and health-check configuration.", ("load_balancer",), destructive=True),
    Capability("vpcs", "Virtual Private Cloud", "networking", "Private network and subnet configuration.", ("vpc",)),
    Capability("firewalls", "Cloud Firewalls", "security", "Network access rules for supported resources.", ("firewall",), destructive=True),
    Capability("domains_dns", "Domains and DNS", "networking", "Domain records and DNS zone management.", ("domain", "record"), destructive=True),
    Capability("floating_ips", "Reserved IPs", "networking", "Manage reserved IP addresses and assignments.", ("reserved_ip",), destructive=True),
    Capability("snapshots", "Snapshots and Images", "backup", "Create and manage resource snapshots and images.", ("snapshot", "image"), destructive=True),
    Capability("monitoring", "Monitoring and Alerts", "observability", "Metrics, alert policies, and notification configuration.", ("alert_policy",)),
    Capability("projects", "Projects and Resource Organization", "governance", "Group resources into projects and manage assignments.", ("project",)),
    Capability("account", "Account and Regions", "administration", "Read account metadata, regions, and supported sizes.", ("account", "region", "size")),
)

CAPABILITY_BY_ID = {item.id: item for item in CAPABILITIES}


def list_capabilities(category=None):
    items = CAPABILITIES
    if category:
        items = tuple(item for item in items if item.category == category)
    return [item.to_dict() for item in items]


def get_capability(capability_id):
    item = CAPABILITY_BY_ID.get(capability_id)
    return item.to_dict() if item else None


def search_capabilities(query):
    needle = (query or "").strip().casefold()
    if not needle:
        return []
    return [
        item.to_dict() for item in CAPABILITIES
        if needle in " ".join((item.id, item.name, item.category, item.description)).casefold()
    ]
