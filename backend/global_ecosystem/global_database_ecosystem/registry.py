"""In-memory metadata registry; not a database connection or persistence engine."""
from __future__ import annotations
from threading import RLock
from typing import Iterable
from .models import DatabaseCapability, DatabasePlatform, DataWorkload

class DatabaseEcosystemRegistry:
    """Thread-safe registry for catalog metadata and workload classification."""
    def __init__(self) -> None:
        self._lock = RLock()
        self._capabilities: dict[str, DatabaseCapability] = {}
        self._platforms: dict[str, DatabasePlatform] = {}
        self._workloads: dict[str, DataWorkload] = {}

    def register_capability(self, item: DatabaseCapability) -> None:
        with self._lock:
            if item.capability_id in self._capabilities:
                raise ValueError(f"capability already registered: {item.capability_id}")
            self._capabilities[item.capability_id] = item

    def register_platform(self, item: DatabasePlatform) -> None:
        with self._lock:
            if item.platform_id in self._platforms:
                raise ValueError(f"platform already registered: {item.platform_id}")
            self._platforms[item.platform_id] = item

    def register_workload(self, item: DataWorkload) -> None:
        with self._lock:
            if item.workload_id in self._workloads:
                raise ValueError(f"workload already registered: {item.workload_id}")
            self._workloads[item.workload_id] = item

    def get_platform(self, platform_id: str) -> DatabasePlatform:
        with self._lock:
            try:
                return self._platforms[platform_id]
            except KeyError as exc:
                raise KeyError(f"unknown database platform: {platform_id}") from exc

    def list_platforms(self, *, database_model: str | None = None) -> tuple[DatabasePlatform, ...]:
        with self._lock:
            values = tuple(self._platforms.values())
        if database_model is not None:
            values = tuple(item for item in values if item.database_model == database_model)
        return tuple(sorted(values, key=lambda item: item.platform_id))

    def list_workloads(self, *, industry: str | None = None) -> tuple[DataWorkload, ...]:
        with self._lock:
            values = tuple(self._workloads.values())
        if industry is not None:
            values = tuple(item for item in values if item.industry == industry)
        return tuple(sorted(values, key=lambda item: item.workload_id))

    def load_workloads(self, items: Iterable[DataWorkload]) -> None:
        """Register a batch atomically; rejects duplicates without partial mutation."""
        batch = tuple(items)
        ids = [item.workload_id for item in batch]
        if len(ids) != len(set(ids)):
            raise ValueError("duplicate workload IDs in batch")
        with self._lock:
            duplicates = set(ids).intersection(self._workloads)
            if duplicates:
                raise ValueError(f"workload already registered: {sorted(duplicates)[0]}")
            self._workloads.update({item.workload_id: item for item in batch})
