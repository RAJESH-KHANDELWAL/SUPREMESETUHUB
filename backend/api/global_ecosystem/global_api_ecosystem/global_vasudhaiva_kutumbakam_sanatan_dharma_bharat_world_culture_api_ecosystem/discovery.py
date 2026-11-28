"""Small, deterministic discovery helpers for cultural resources."""
from .domain import CulturalResource
from .governance import assess_publication

def discover(resources, pillar=None, area=None, include_unapproved=False):
    """Return matching resources; public discovery excludes unapproved records."""
    results = []
    for resource in resources:
        if pillar and resource.pillar != pillar:
            continue
        if area and resource.area != area:
            continue
        if not include_unapproved and not assess_publication(resource).approved_for_public_discovery:
            continue
        results.append(resource)
    return tuple(results)
