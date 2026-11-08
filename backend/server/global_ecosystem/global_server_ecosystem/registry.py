"""Thread-safe in-process registry for SERVER runtime nodes.

This registry is runtime state only; it is not a DATABASE or persistence layer.
"""
from threading import RLock
from typing import Any

class ServerRegistry:
    def __init__(self):
        self._servers: dict[str, Any] = {}
        self._lock = RLock()

    @staticmethod
    def _key(server_id: str) -> str:
        key = str(server_id or "").strip()
        if not key:
            raise ValueError("server_id is required")
        return key

    def register(self, server: Any, *, replace: bool = False):
        key = self._key(getattr(server, "server_id", ""))
        with self._lock:
            if key in self._servers and not replace:
                raise ValueError(f"SERVER node already registered: {key}")
            self._servers[key] = server
        return server

    def get(self, server_id: str):
        with self._lock:
            return self._servers.get(self._key(server_id))

    def list(self):
        with self._lock:
            return tuple(self._servers[key] for key in sorted(self._servers))

    def unregister(self, server_id: str) -> bool:
        with self._lock:
            return self._servers.pop(self._key(server_id), None) is not None

    def count(self) -> int:
        with self._lock:
            return len(self._servers)

    def status(self) -> dict[str, Any]:
        with self._lock:
            return {"registered_servers": len(self._servers),
                    "server_ids": sorted(self._servers),
                    "registry_type": "IN_MEMORY_RUNTIME_REGISTRY",
                    "durable_persistence": False}

__all__ = ["ServerRegistry"]
