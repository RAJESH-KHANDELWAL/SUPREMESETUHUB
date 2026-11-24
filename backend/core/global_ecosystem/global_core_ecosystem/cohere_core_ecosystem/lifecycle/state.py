from enum import Enum
class EcosystemState(str, Enum):
    DISABLED = "disabled"
    CONFIGURED = "configured"
    READY = "ready"
    DEGRADED = "degraded"
