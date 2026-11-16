"""Provider-wide lifecycle state vocabulary."""
from enum import Enum


class EcosystemState(str, Enum):
    DISABLED = "disabled"
    REGISTERED = "registered"
    INTERFACE_ONLY = "interface_only"
    CONTRACT_ONLY = "contract_only"
    READY = "ready"
    DEGRADED = "degraded"
    ERROR = "error"
