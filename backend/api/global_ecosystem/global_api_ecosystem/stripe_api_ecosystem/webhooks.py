"""Stripe webhook signature verification helpers."""
from __future__ import annotations

import json
from typing import Any

import stripe

from .config import StripeConfig


def verify_webhook(payload: bytes, signature: str, config: StripeConfig) -> dict[str, Any]:
    """Verify the Stripe-Signature header and return the parsed event."""
    if not config.webhook_secret:
        raise ValueError("STRIPE_WEBHOOK_SECRET is required for webhook verification")
    try:
        event = stripe.Webhook.construct_event(payload, signature, config.webhook_secret)
    except (ValueError, stripe.error.SignatureVerificationError) as exc:
        raise ValueError("Invalid Stripe webhook payload or signature") from exc
    return dict(event)
