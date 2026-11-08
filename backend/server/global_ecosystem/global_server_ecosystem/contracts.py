"""SERVER-owned adapter protocols; no duplicated layer implementation."""
from __future__ import annotations
from typing import Any, Protocol, runtime_checkable
LAYER_NAMES = ("API", "CORE", "ENGINE", "DATABASE", "STORAGE")
@runtime_checkable
class ApiBoundaryContract(Protocol):
    def describe_routes(self) -> dict[str, Any]: ...
@runtime_checkable
class CoreBoundaryContract(Protocol):
    def validate_request(self, request: dict[str, Any]) -> dict[str, Any]: ...
@runtime_checkable
class EngineBoundaryContract(Protocol):
    def dispatch(self, operation: str, payload: dict[str, Any]) -> dict[str, Any]: ...
@runtime_checkable
class DatabaseBoundaryContract(Protocol):
    def read_server_record(self, server_id: str) -> dict[str, Any] | None: ...
@runtime_checkable
class StorageBoundaryContract(Protocol):
    def resolve_artifact(self, artifact_id: str) -> dict[str, Any] | None: ...
