"""Lifecycle vocabulary for the command capability."""
from enum import Enum

class CapabilityState(str, Enum):
    DISABLED = "disabled"
    CONFIGURED = "configured"
    READY = "ready"
    DEGRADED = "degraded"
