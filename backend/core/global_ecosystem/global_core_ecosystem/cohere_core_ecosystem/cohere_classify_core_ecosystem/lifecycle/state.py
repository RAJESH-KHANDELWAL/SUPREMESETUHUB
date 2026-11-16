"""Lifecycle vocabulary for the classify capability."""
from enum import Enum

class CapabilityState(str, Enum):
    DISABLED = "disabled"
    CONFIGURED = "configured"
    READY = "ready"
    DEGRADED = "degraded"
