"""Environment-backed configuration for DeepSeek; secrets never belong in source."""
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
        endpoint_var = "DEEPSEEK_ENDPOINT"
        return cls(
            credential=os.getenv(PROVIDER["credential_env"]),
            endpoint=os.getenv(endpoint_var) or PROVIDER["api_endpoint"],
        )

    def validate(self) -> None:
        if not self.credential:
            raise RuntimeError(f"Set {PROVIDER['credential_env']} before using {PROVIDER['name']}.")
        if not self.endpoint:
            raise RuntimeError(f"Configure an endpoint for {PROVIDER['name']}.")
