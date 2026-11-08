"""STORAGE-owned artifact metadata repository (in-memory reference adapter)."""
from __future__ import annotations
from copy import deepcopy
from threading import RLock
from .models import ServerArtifact

class ServerArtifactRepository:
    def __init__(self):
        self._artifacts = {}
        self._lock = RLock()

    def create(self, artifact: ServerArtifact):
        artifact.validate()
        key = artifact.artifact_id.strip()
        row = deepcopy(artifact.__dict__)
        row["artifact_id"] = key
        with self._lock:
            if key in self._artifacts:
                raise ValueError(f"SERVER_ARTIFACT_ALREADY_EXISTS: {key}")
            self._artifacts[key] = row
            return deepcopy(row)

    def get(self, artifact_id: str):
        with self._lock:
            value = self._artifacts.get(str(artifact_id).strip())
            return deepcopy(value) if value is not None else None

    def list_for_server(self, server_id: str):
        key = str(server_id).strip()
        with self._lock:
            return [deepcopy(v) for v in self._artifacts.values() if v["server_id"] == key]

    def update_status(self, artifact_id: str, status: str):
        with self._lock:
            key = str(artifact_id).strip()
            current = self._artifacts.get(key)
            if current is None:
                return None
            self._artifacts[key] = {**current, "status": str(status).strip().upper()}
            return deepcopy(self._artifacts[key])

    def count(self):
        with self._lock:
            return len(self._artifacts)
