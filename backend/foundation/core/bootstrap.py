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

from backend.foundation.audit.global_ecosystem.global_audit_ecosystem.manager import GlobalAuditEcosystemManager
from backend.foundation.core.global_ecosystem.global_core_ecosystem.manager import GlobalCoreEcosystemManager
from backend.foundation.dependencies.global_ecosystem.global_dependencies_ecosystem.manager import GlobalDependenciesEcosystemManager
from backend.foundation.file_manager.global_ecosystem.global_file_manager_ecosystem.manager import GlobalFileManagerEcosystemManager
from backend.foundation.identity.global_ecosystem.global_identity_ecosystem.manager import GlobalIdentityEcosystemManager
from backend.foundation.registry.global_ecosystem.global_registry_ecosystem.manager import GlobalRegistryEcosystemManager
from backend.foundation.security.global_ecosystem.global_security_ecosystem.manager import GlobalSecurityEcosystemManager
from backend.foundation.sync.global_ecosystem.global_sync_ecosystem.manager import GlobalSyncEcosystemManager


class FoundationBootstrap:
    """Central bootstrap point for the complete Foundation layer."""

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

        # Ecosystem managers wrap the existing Foundation components.
        # They do not create duplicate identity, registry, or service logic.
        self.ecosystems = {
            "audit": GlobalAuditEcosystemManager(self.audit),
            "core": GlobalCoreEcosystemManager(self.service.foundation),
            "dependencies": GlobalDependenciesEcosystemManager(self.dependencies),
            "file_manager": GlobalFileManagerEcosystemManager(self.file_manager),
            "identity": GlobalIdentityEcosystemManager(self.identity),
            "registry": GlobalRegistryEcosystemManager(self.registry),
            "security": GlobalSecurityEcosystemManager(self.security),
            "sync": GlobalSyncEcosystemManager(self.sync),
        }

    def _ecosystem_status(self):
        return {
            name: manager.status()
            for name, manager in self.ecosystems.items()
        }

    def boot(self):
        foundation = self.service.initialize()
        integrity = self.integrity.verify()
        identity = self.identity.initialize()

        self.audit.record(
            event="FOUNDATION_BOOT",
            source="FoundationBootstrap",
            details={"version": self.VERSION},
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
            "ecosystems": self._ecosystem_status(),
        }

    def health(self):
        integrity = self.integrity.verify()
        ecosystems = self._ecosystem_status()
        ecosystems_integrated = all(
            item["status"] == "INTEGRATED"
            for item in ecosystems.values()
        )

        healthy = integrity["verified"] and ecosystems_integrated
        return {
            "foundation": self.NAME,
            "version": self.VERSION,
            "status": "HEALTHY" if healthy else "UNHEALTHY",
            "integrity": integrity,
            "ecosystems": ecosystems,
        }

    def shutdown(self):
        self.audit.record(
            event="FOUNDATION_SHUTDOWN",
            source="FoundationBootstrap",
        )
        return self.service.shutdown()
