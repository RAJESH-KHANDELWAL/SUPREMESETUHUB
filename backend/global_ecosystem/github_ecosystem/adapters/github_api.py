"""GitHub API adapter contract; authenticated client is injected by runtime."""
from dataclasses import dataclass
from typing import Any, Mapping, Protocol

class GitHubClient(Protocol):
    def request(self, method: str, path: str, *, params=None, json=None) -> Mapping[str, Any]:
        """Perform an authorized API request in the integration layer."""

@dataclass(frozen=True)
class AdapterStatus:
    provider: str = "github"
    adapter_contract_available: bool = True
    client_injected: bool = False
    live_connection_verified: bool = False

def adapter_status(client=None):
    return AdapterStatus(client_injected=client is not None).__dict__
