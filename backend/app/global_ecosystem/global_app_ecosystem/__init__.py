"""Compatibility facade for the canonical GLOBAL APP ecosystem package.

The domain implementation lives under backend.global_ecosystem.global_app_ecosystem.
This legacy import path remains available to existing APP and ENGINE consumers.
"""
from backend.global_ecosystem.global_app_ecosystem import (
    AppAdapterRegistry,
    AppComponent,
    AppComponentAdapter,
    AppComponentRegistry,
    AppLifecycle,
    EcosystemService,
    GlobalAppEcosystemManager,
    GlobalAppEcosystemService,
    InvalidLifecycleTransition,
    app_diagnostics,
    get_component_type,
    list_component_types,
    runtime_status,
)

__all__ = [
    "AppAdapterRegistry", "AppComponent", "AppComponentAdapter",
    "AppComponentRegistry", "AppLifecycle", "EcosystemService",
    "GlobalAppEcosystemManager", "GlobalAppEcosystemService",
    "InvalidLifecycleTransition", "app_diagnostics",
    "get_component_type", "list_component_types", "runtime_status",
]
