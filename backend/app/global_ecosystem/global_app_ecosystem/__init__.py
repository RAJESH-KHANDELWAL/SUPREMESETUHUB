"""Independent GLOBAL APP ECOSYSTEM public interface."""
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
__all__ = ["list_component_types","get_component_type","AppComponent","AppComponentRegistry","AppComponentAdapter","AppAdapterRegistry","AppLifecycle","InvalidLifecycleTransition","runtime_status","app_diagnostics","GlobalAppEcosystemService","EcosystemService","GlobalAppEcosystemManager"]
