"""Environment-backed configuration for Cohere; secrets never belong in source."""
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
        return cls(credential=os.getenv(PROVIDER["credential_env"]), endpoint=os.getenv("COHERE_ENDPOINT") or PROVIDER["api_endpoint"])

    def validate(self) -> None:
        if not self.credential:
            raise RuntimeError("Set COHERE_API_KEY before using Cohere.")
        if not self.endpoint:
            raise RuntimeError("Configure COHERE_ENDPOINT before using Cohere.")
