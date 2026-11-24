"""Environment-backed configuration for Together AI; secrets stay outside source control."""
from __future__ import annotations

import os
from dataclasses import dataclass

from .catalog import PROVIDER


@dataclass(frozen=True, slots=True)
class ProviderConfig:
    credential: str | None
    endpoint: str

    @classmethod
    def from_env(cls) -> "ProviderConfig":
        return cls(
            credential=os.getenv(PROVIDER["credential_env"]),
            endpoint=os.getenv("TOGETHER_ENDPOINT") or PROVIDER["api_endpoint"],
        )

    def validate(self) -> None:
        if not self.credential:
            raise RuntimeError(f"Set {PROVIDER['credential_env']} before using {PROVIDER['name']}.")
        if not self.endpoint:
            raise RuntimeError(f"Configure the endpoint for {PROVIDER['name']}.")
