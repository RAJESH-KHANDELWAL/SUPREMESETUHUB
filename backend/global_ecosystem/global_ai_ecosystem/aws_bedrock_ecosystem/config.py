"""AWS Bedrock configuration using the AWS SDK credential chain."""
from __future__ import annotations
import os
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class ProviderConfig:
    region: str | None
    endpoint: str | None = None

    @classmethod
    def from_env(cls) -> "ProviderConfig":
        return cls(region=os.getenv("AWS_REGION") or os.getenv("AWS_DEFAULT_REGION"), endpoint=os.getenv("AWS_BEDROCK_ENDPOINT"))

    def validate(self) -> None:
        if not self.region:
            raise RuntimeError("Set AWS_REGION or AWS_DEFAULT_REGION for AWS Bedrock.")
        # Credentials are intentionally resolved by the AWS SDK's standard
        # credential provider chain (role, profile, environment, etc.).
