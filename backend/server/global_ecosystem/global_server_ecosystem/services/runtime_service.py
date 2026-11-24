"""SERVER process-runtime diagnostics service."""
from ..runtime import runtime_status

class ServerRuntimeService:
    def health(self):
        return runtime_status()

    def describe(self):
        return {
            "service": "GLOBAL SERVER RUNTIME",
            "ownership": "SERVER",
            "runtime": self.health(),
            "persistence": "NOT_PROVIDED_BY_SERVER_RUNTIME",
        }

__all__ = ["ServerRuntimeService"]
