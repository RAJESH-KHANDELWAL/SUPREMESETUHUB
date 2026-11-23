"""Public interface for the Global APP Core Ecosystem."""
from .manager import GlobalAppCoreManager, get_manager
from .service import GlobalAppCoreService

__all__ = ["GlobalAppCoreManager", "GlobalAppCoreService", "get_manager"]
