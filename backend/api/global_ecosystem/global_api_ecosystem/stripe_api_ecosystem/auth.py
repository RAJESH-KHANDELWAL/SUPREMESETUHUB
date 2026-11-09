"""Stripe authentication helpers.

Stripe secret keys are bearer credentials. This module never stores credentials.
"""
from __future__ import annotations

from .config import StripeConfig


def build_auth_headers(config: StripeConfig) -> dict[str, str]:
    """Build request headers for Stripe's secret-key authentication."""
    return config.headers()
