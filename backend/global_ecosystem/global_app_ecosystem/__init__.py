"""Bharat-to-global application ecosystem domain package."""
from importlib import import_module
from .catalog import list_component_types, get_component_type
from .models import AppComponent
from .registry import AppComponentRegistry
from .component_base import AppComponentAdapter
from .component_registry import AppAdapterRegistry
from .lifecycle import AppLifecycle, InvalidLifecycleTransition
from .runtime import runtime_status
from .diagnostics import app_diagnostics
from .service import GlobalAppEcosystemService, EcosystemService
from .manager import GlobalAppEcosystemManager
from .providers import list_app_providers, get_app_provider, validate_app_provider_registry
from .capabilities import list_app_types, list_app_capability_groups
from .scope import APP_MATURITY_LEVELS, APP_CAPABILITY_LEVELS, APP_SCOPE_DOMAINS, get_scope_catalog, get_domain, list_domain_ids

def list_domain_packages():
    """Load each top-level domain package and return its catalog profile."""
    return tuple(
        import_module(f"{__name__}.{domain_id}_ecosystem").get_catalog()
        for domain_id in list_domain_ids()
    )

def get_domain_package(domain_id: str):
    """Load one known top-level domain package; return None for unknown IDs."""
    if domain_id not in list_domain_ids():
        return None
    module = import_module(f"{__name__}.{domain_id}_ecosystem")
    return module.get_catalog()

__all__ = [
 "list_component_types","get_component_type","AppComponent","AppComponentRegistry",
 "AppComponentAdapter","AppAdapterRegistry","AppLifecycle","InvalidLifecycleTransition",
 "runtime_status","app_diagnostics","GlobalAppEcosystemService","EcosystemService",
 "GlobalAppEcosystemManager","list_app_providers","get_app_provider",
 "validate_app_provider_registry","list_app_types","list_app_capability_groups",
 "APP_MATURITY_LEVELS","APP_CAPABILITY_LEVELS","APP_SCOPE_DOMAINS","get_scope_catalog","get_domain","list_domain_ids",
 "list_domain_packages","get_domain_package",
]
