"""Global connection ecosystem public interface."""

from .catalog import get_global_connection_catalog
from .manager import GlobalConnectionManager
from .service import GlobalConnectionService

__all__ = ["GlobalConnectionManager", "GlobalConnectionService", "get_global_connection_catalog"]
