"""Stable provider-neutral contracts for SERVER CORE."""
from __future__ import annotations
from typing import Any, Protocol, runtime_checkable
from .models import ServerIdentity, ServerLifecycleState

@runtime_checkable
class ServerProviderContract(Protocol):
    provider_id: str
    def health(self) -> dict[str, Any]: ...
    def execute(self, operation: str, payload: dict[str, Any] | None = None) -> Any: ...

@runtime_checkable
class ServerInventoryContract(Protocol):
    def register(self, identity: ServerIdentity) -> dict[str, Any]: ...
    def get(self, server_id: str) -> dict[str, Any] | None: ...
    def list(self) -> list[dict[str, Any]]: ...

@runtime_checkable
class ServerLifecycleContract(Protocol):
    def transition(self, server_id: str, state: ServerLifecycleState) -> dict[str, Any] | None: ...
