"""MAIN BASE FOUNDATION connection models."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Connection:
    """Represent a provider/server connection and its ecosystem namespace."""

    connection_id: str
    provider_id: str
    server_id: str
    connection_type: str
    protocol: str
    endpoint: Optional[str] = None
    namespace: str = "global"
    status: str = "REGISTERED"
    authorized: bool = False
    enabled: bool = True
    error: Optional[str] = None
