"""MAIN BASE FOUNDATION connection system and ecosystem interfaces."""

from .manager import ConnectionManager
from .models import Connection
from .global_ecosystem.global_connection_ecosystem import GlobalConnectionManager, GlobalConnectionService
from .global_ecosystem.global_connection_ecosystem.bada_business_connection_ecosystem import (
    BadaBusinessConnectionManager,
    BadaBusinessConnectionService,
)

__all__ = [
    "ConnectionManager",
    "Connection",
    "GlobalConnectionManager",
    "GlobalConnectionService",
    "BadaBusinessConnectionManager",
    "BadaBusinessConnectionService",
]
