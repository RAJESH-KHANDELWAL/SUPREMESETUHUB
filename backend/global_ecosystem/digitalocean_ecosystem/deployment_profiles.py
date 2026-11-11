"""Technology-neutral workload profiles mapped to catalog capability IDs.

These are architecture starting points, not DigitalOcean plan/pricing claims.
Capacity, region availability, quotas, and product compatibility require review.
"""
from .workload_domains import MATURITY_LEVELS

DEPLOYMENT_PROFILES = {
    "normal": {
        "name": "Normal / Basic",
        "capabilities": ("app_platform", "account"),
        "focus": ("single application", "basic observability", "backups planned"),
    },
    "standard": {
        "name": "Standard",
        "capabilities": ("app_platform", "managed_databases", "monitoring"),
        "focus": ("separated application and data", "health monitoring"),
    },
    "professional": {
        "name": "Professional",
        "capabilities": ("app_platform", "managed_databases", "spaces", "monitoring"),
        "focus": ("object storage", "operational monitoring", "backup policy"),
    },
    "advanced": {
        "name": "Advanced",
        "capabilities": ("kubernetes", "managed_databases", "spaces", "load_balancers", "monitoring"),
        "focus": ("container orchestration", "traffic distribution", "resilience design"),
    },
    "expert": {
        "name": "Expert",
        "capabilities": ("kubernetes", "managed_databases", "vpcs", "firewalls", "load_balancers", "monitoring"),
        "focus": ("network segmentation", "security controls", "scaling strategy"),
    },
    "enterprise": {
        "name": "Enterprise",
        "capabilities": ("kubernetes", "managed_databases", "vpcs", "firewalls", "load_balancers", "spaces", "monitoring"),
        "focus": ("multi-team governance", "disaster recovery design", "auditable operations"),
    },
    "industrial": {
        "name": "Industrial",
        "capabilities": ("droplets", "kubernetes", "vpcs", "firewalls", "monitoring", "snapshots"),
        "focus": ("edge and device integration planning", "segmented networks", "recovery planning"),
    },
    "research": {
        "name": "Research",
        "capabilities": ("droplets", "kubernetes", "spaces", "managed_databases", "monitoring"),
        "focus": ("reproducible environments", "data lifecycle", "experiment observability"),
    },
    "frontier": {
        "name": "Frontier",
        "capabilities": ("kubernetes", "droplets", "spaces", "managed_databases", "load_balancers", "monitoring"),
        "focus": ("experimental workload isolation", "benchmarking", "capacity validation"),
    },
    "supreme": {
        "name": "Supreme",
        "capabilities": ("kubernetes", "droplets", "managed_databases", "spaces", "vpcs", "firewalls", "load_balancers", "snapshots", "monitoring"),
        "focus": ("multi-region architecture review", "high-assurance governance", "tested recovery objectives"),
    },
}

def get_deployment_profile(level):
    profile = DEPLOYMENT_PROFILES.get((level or "").strip().casefold())
    if not profile:
        return None
    return {
        "level": level.strip().casefold(),
        "name": profile["name"],
        "capabilities": list(profile["capabilities"]),
        "focus": list(profile["focus"]),
        "provider_plan_verified": False,
        "note": "Reference architecture only; validate product availability, quotas, capacity, cost, and region support.",
    }

def validate_profiles():
    known = set(DEPLOYMENT_PROFILES)
    unknown = known.difference(MATURITY_LEVELS)
    return {"valid": not unknown, "unknown_levels": sorted(unknown)}
