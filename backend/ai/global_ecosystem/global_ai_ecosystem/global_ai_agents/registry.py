"""Explicit in-memory registry for agent profile metadata."""
from __future__ import annotations
from threading import RLock
from typing import Any
from .catalog import AGENT_CATALOG

class AgentRegistry:
    """Register agent profiles explicitly; never starts an agent runtime."""
    def __init__(self) -> None:
        self._lock = RLock()
        self._agents: dict[str, dict[str, Any]] = {}

    def register(self, agent_id: str, profile: dict[str, Any]) -> dict[str, Any]:
        key = agent_id.strip().lower()
        if not key:
            raise ValueError("AI_AGENT_ID_REQUIRED")
        if not isinstance(profile, dict):
            raise TypeError("AI_AGENT_PROFILE_MUST_BE_A_MAPPING")
        required = {"name", "category", "description", "capabilities"}
        if required - profile.keys():
            raise ValueError("AI_AGENT_PROFILE_FIELDS_MISSING")
        normalized = dict(profile)
        normalized["capabilities"] = sorted(set(normalized["capabilities"]))
        with self._lock:
            self._agents[key] = normalized
        return self.get(key)

    def get(self, agent_id: str) -> dict[str, Any]:
        key = agent_id.strip().lower()
        with self._lock:
            profile = self._agents.get(key) or AGENT_CATALOG.get(key)
            if profile is None:
                raise KeyError("AI_AGENT_NOT_FOUND")
            return {"id": key, **dict(profile)}

    def list(self) -> list[dict[str, Any]]:
        with self._lock:
            keys = set(AGENT_CATALOG) | set(self._agents)
        return [self.get(key) for key in sorted(keys)]

    def unregister(self, agent_id: str) -> bool:
        with self._lock:
            return self._agents.pop(agent_id.strip().lower(), None) is not None
