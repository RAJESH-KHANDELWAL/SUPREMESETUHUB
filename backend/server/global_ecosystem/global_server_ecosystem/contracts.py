"""SERVER-owned contracts for adapters; implementations stay in their own layers."""
from typing import Any, Protocol, runtime_checkable
@runtime_checkable
class ApiLayerContract(Protocol):
    def describe_routes(self) -> dict[str, Any]: ...
@runtime_checkable
class CoreLayerContract(Protocol):
    def validate_request(self, request: dict[str, Any]) -> dict[str, Any]: ...
@runtime_checkable
class EngineLayerContract(Protocol):
    def dispatch(self, operation: str, payload: dict[str, Any]) -> dict[str, Any]: ...
@runtime_checkable
class DatabaseLayerContract(Protocol):
    def read_server_record(self, server_id: str) -> dict[str, Any] | None: ...
@runtime_checkable
class StorageLayerContract(Protocol):
    def resolve_artifact(self, artifact_id: str) -> dict[str, Any] | None: ...
@runtime_checkable
class ServerProviderContract(Protocol):
    provider_id: str
    def describe(self) -> dict[str, Any]: ...
__all__ = ["ApiLayerContract", "CoreLayerContract", "EngineLayerContract",
           "DatabaseLayerContract", "StorageLayerContract", "ServerProviderContract"]