"""Discoverable domain packages in the Global App Ecosystem."""
from importlib import import_module
from ..scope import list_domain_ids

def list_domain_packages():
    """Load each domain package and return its catalog profile."""
    return tuple(
        import_module(f"{__name__}.{domain_id}_ecosystem").get_catalog()
        for domain_id in list_domain_ids()
    )

def get_domain_package(domain_id: str):
    """Load one known domain package; return None for unknown IDs."""
    if domain_id not in list_domain_ids():
        return None
    module = import_module(f"{__name__}.{domain_id}_ecosystem")
    return module.get_catalog()

__all__ = ["list_domain_packages", "get_domain_package"]
