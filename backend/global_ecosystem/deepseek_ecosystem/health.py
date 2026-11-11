"""Configuration-only health reporting; no live DeepSeek call is made."""
from __future__ import annotations
import os
from .constants import API_KEY_ENV, STATUS_KEY_CONFIGURED, STATUS_CONNECTION_UNVERIFIED
from .models import DeepSeekHealth

def get_health() -> dict:
    """Report server-side key presence without returning its value."""
    configured = bool(os.getenv(API_KEY_ENV, "").strip())
    status = STATUS_KEY_CONFIGURED if configured else STATUS_CONNECTION_UNVERIFIED
    return DeepSeekHealth(configured=configured, status=status).to_dict()

__all__ = ["get_health"]
