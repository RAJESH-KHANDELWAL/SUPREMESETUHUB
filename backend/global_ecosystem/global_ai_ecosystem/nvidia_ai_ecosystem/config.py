"""Environment-backed configuration for NVIDIA AI; secrets never belong in source."""
from __future__ import annotations
import os
from dataclasses import dataclass
from .catalog import PROVIDER

@dataclass(frozen=True, slots=True)
class ProviderConfig:
    credential: str | None
    endpoint: str | None

    @classmethod
    def from_env(cls) -> "ProviderConfig":
        return cls(credential=os.getenv("NVIDIA_API_KEY"), endpoint=os.getenv("NVIDIA_AI_ENDPOINT") or PROVIDER["api_endpoint"])

    def validate(self) -> None:
        if not self.credential:
            raise RuntimeError("Set NVIDIA_API_KEY before using NVIDIA hosted inference.")
        if not self.endpoint:
            raise RuntimeError("Configure NVIDIA_AI_ENDPOINT before using NVIDIA AI.")
