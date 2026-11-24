"""Environment-backed configuration for Hugging Face; secrets never belong in source."""
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
        return cls(credential=os.getenv("HF_TOKEN"), endpoint=os.getenv("HF_ENDPOINT") or PROVIDER["api_endpoint"])

    def validate(self) -> None:
        if not self.credential:
            raise RuntimeError("Set HF_TOKEN before using Hugging Face hosted inference.")
        if not self.endpoint:
            raise RuntimeError("Configure HF_ENDPOINT before using Hugging Face.")
