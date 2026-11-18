"""DigitalOcean API adapter contract.

Implementations should be injected by the integration runtime. This module
intentionally avoids HTTP clients, credential loading, and side effects.
"""
from dataclasses import dataclass
from typing import Any, Mapping, Protocol


class DigitalOceanClient(Protocol):
    def request(self, method: str, path: str, *, params=None, json=None) -> Mapping[str, Any]:
        """Execute an authenticated provider request in the integration layer."""


@dataclass(frozen=True)
class AdapterStatus:
    provider: str = "digitalocean"
    adapter_contract_available: bool = True
    client_injected: bool = False
    live_connection_verified: bool = False


def adapter_status(client=None):
    return AdapterStatus(client_injected=client is not None).__dict__
