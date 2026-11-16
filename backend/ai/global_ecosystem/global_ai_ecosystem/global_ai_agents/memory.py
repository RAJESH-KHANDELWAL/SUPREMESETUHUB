"""Agent memory contracts and scope controls; no storage backend is opened."""
from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class AgentMemoryPolicy:
    scope: str = "session"
    read_enabled: bool = True
    write_enabled: bool = False
    retention_days: int | None = None
    contains_sensitive_data: bool = False

    def validate(self) -> None:
        if self.scope not in {"none", "session", "user", "project"}:
            raise ValueError("AI_AGENT_MEMORY_SCOPE_INVALID")
        if self.scope == "none" and (self.read_enabled or self.write_enabled):
            raise ValueError("AI_AGENT_MEMORY_DISABLED")
        if self.contains_sensitive_data and self.write_enabled:
            raise ValueError("AI_AGENT_SENSITIVE_MEMORY_WRITE_BLOCKED")
        if self.retention_days is not None and self.retention_days < 1:
            raise ValueError("AI_AGENT_MEMORY_RETENTION_INVALID")
