"""Contracts owned exclusively by the SERVER domain."""
from typing import Any, Protocol, runtime_checkable

@runtime_checkable
class ServerProviderContract(Protocol):
    provider_id: str
    def describe(self) -> dict[str, Any]: ...
    def health(self) -> dict[str, Any]: ...
    def execute(self, operation: str, payload: dict[str, Any] | None = None) -> dict[str, Any]: ...

@runtime_checkable
class ServerRuntimeContract(Protocol):
    def health(self) -> dict[str, Any]: ...
    def status(self) -> dict[str, Any]: ...

@runtime_checkable
class ServerOperationContract(Protocol):
    def execute(self, operation: str, payload: dict[str, Any] | None = None) -> dict[str, Any]: ...

__all__ = ["ServerProviderContract", "ServerRuntimeContract", "ServerOperationContract"]
