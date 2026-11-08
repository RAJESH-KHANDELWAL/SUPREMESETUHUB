"""Stripe configuration loaded from environment variables."""
from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Mapping


@dataclass(frozen=True)
class StripeConfig:
    secret_key: str
    api_base_url: str = "https://api.stripe.com"
    api_version: str | None = None
    webhook_secret: str | None = None
    connect_timeout: float = 10.0
    read_timeout: float = 30.0

    @classmethod
    def from_env(cls, env: Mapping[str, str] | None = None) -> "StripeConfig":
        source = os.environ if env is None else env
        key = source.get("STRIPE_SECRET_KEY", "").strip()
        if not key:
            raise ValueError("STRIPE_SECRET_KEY is required")
        base = source.get("STRIPE_API_BASE_URL", "https://api.stripe.com").strip()
        if not base.startswith("https://"):
            raise ValueError("Stripe API base URL must use HTTPS")
        return cls(
            secret_key=key,
            api_base_url=base.rstrip("/"),
            api_version=source.get("STRIPE_API_VERSION") or None,
            webhook_secret=source.get("STRIPE_WEBHOOK_SECRET") or None,
        )

    def headers(self) -> dict[str, str]:
        headers = {"Authorization": f"Bearer {self.secret_key}", "Accept": "application/json"}
        if self.api_version:
            headers["Stripe-Version"] = self.api_version
        return headers
