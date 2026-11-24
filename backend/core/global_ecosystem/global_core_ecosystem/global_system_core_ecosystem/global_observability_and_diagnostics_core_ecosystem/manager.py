"""Domain facade backed by the shared System Core runtime."""
from ..domain_runtime import SystemCoreDomainManager

class ObservabilityAndDiagnosticsSystemCoreDomainManager(SystemCoreDomainManager):
    DOMAIN_ID = "OBSERVABILITY_AND_DIAGNOSTICS"
    def __init__(self) -> None:
        super().__init__(self.DOMAIN_ID)

def get_manager() -> ObservabilityAndDiagnosticsSystemCoreDomainManager:
    return ObservabilityAndDiagnosticsSystemCoreDomainManager()
