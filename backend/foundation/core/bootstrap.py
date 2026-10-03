from backend.foundation.core.service import FoundationService
from backend.foundation.core.integrity import FoundationIntegrity
from backend.foundation.core.orchestrator import FoundationOrchestrator

from backend.foundation.identity.manager import FoundationIdentityManager
from backend.foundation.registry.registry import FoundationRegistry
from backend.foundation.dependencies.manager import FoundationDependencyManager
from backend.foundation.audit.service import FoundationAuditService
from backend.foundation.security.manager import FoundationSecurityManager
from backend.foundation.sync.manager import FoundationSyncManager
from backend.foundation.file_manager.manager import FoundationFileManager


class FoundationBootstrap:
    """
    MAIN BASE FOUNDATION

    Central bootstrap point for the complete Foundation layer.
    """

    NAME = "MAIN BASE FOUNDATION"
    VERSION = "1.0.0"

    def __init__(self):
        self.service = FoundationService()
        self.integrity = FoundationIntegrity()
        self.orchestrator = FoundationOrchestrator()

        self.identity = FoundationIdentityManager()
        self.registry = FoundationRegistry()
        self.dependencies = FoundationDependencyManager()
        self.audit = FoundationAuditService()
        self.security = FoundationSecurityManager()
        self.sync = FoundationSyncManager()
        self.file_manager = FoundationFileManager()

    def boot(self):
        foundation = self.service.initialize()
        integrity = self.integrity.verify()
        identity = self.identity.initialize()

        self.audit.record(
            event="FOUNDATION_BOOT",
            source="FoundationBootstrap",
            details={
                "version": self.VERSION
            }
        )

        return {
            "foundation": self.NAME,
            "version": self.VERSION,
            "status": "RUNNING",
            "service": foundation,
            "integrity": integrity,
            "identity": identity,
            "registry": self.registry.list_components(),
            "dependencies": self.dependencies.list_dependencies(),
            "audit": self.audit.list_events(),
            "security": self.security.list_checks(),
            "sync": self.sync.status(),
            "file_manager": self.file_manager.list_files(),
        }

    def health(self):
        integrity = self.integrity.verify()

        return {
            "foundation": self.NAME,
            "version": self.VERSION,
            "status": (
                "HEALTHY"
                if integrity["verified"]
                else "UNHEALTHY"
            ),
            "integrity": integrity,
        }

    def shutdown(self):
        self.audit.record(
            event="FOUNDATION_SHUTDOWN",
            source="FoundationBootstrap"
        )

        return self.service.shutdown()
