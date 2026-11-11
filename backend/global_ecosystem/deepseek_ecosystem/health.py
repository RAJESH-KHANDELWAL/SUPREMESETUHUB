"""Configuration-only health reporting; no live DeepSeek request is made."""
from __future__ import annotations
import os
from .constants import API_KEY_ENV
from .models import DeepSeekHealth

def get_health() -> dict:
    configured = bool(os.getenv(API_KEY_ENV, "").strip())
    status = "KEY_CONFIGURED_NOT_CONNECTION_TESTED" if configured else "CONNECTION_NOT_VERIFIED"
    return DeepSeekHealth(configured=configured, status=status).to_dict()

__all__ = ["get_health"]
