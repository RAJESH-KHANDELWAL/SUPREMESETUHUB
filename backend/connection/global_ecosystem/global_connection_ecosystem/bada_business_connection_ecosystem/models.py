"""Bada Business connection request model."""

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class BadaBusinessConnectionRequest:
    connection_id: str
    provider_id: str
    server_id: str
    connection_type: str
    protocol: str
    endpoint: Optional[str] = None
