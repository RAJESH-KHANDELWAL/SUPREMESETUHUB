"""STORAGE ecosystem service for storage catalog and server artifact metadata."""
from .registry import list_providers, get_provider
from .server_artifact_repository import ServerArtifactRepository

class EcosystemService:
    domain = "STORAGE"
    ecosystem = "GLOBAL_STORAGE_ECOSYSTEM"

    def __init__(self, repository=None):
        self.server_artifacts = repository or ServerArtifactRepository()

    def describe(self):
        providers = list_providers()
        return {
            "domain": self.domain, "ecosystem": self.ecosystem,
            "providers": providers, "provider_count": len(providers),
            "server_artifact_count": self.server_artifacts.count(),
            "live_provider_connections_enabled": False,
            "binary_file_operations_enabled": False,
            "metadata_backend": "IN_MEMORY_REFERENCE_ADAPTER",
            "durable_storage_enabled": False,
        }

    def list_providers(self):
        items = list_providers()
        return {"success": True, "count": len(items), "providers": items}

    def get_provider(self, provider_id):
        try:
            return {"success": True, "provider": get_provider(provider_id)}
        except KeyError:
            return {"success": False, "error": "STORAGE_PROVIDER_NOT_FOUND"}

    def register_server_artifact(self, artifact):
        try:
            return {"success": True, "artifact": self.server_artifacts.create(artifact)}
        except (TypeError, ValueError) as exc:
            return {"success": False, "error": "STORAGE_ARTIFACT_REGISTER_FAILED", "message": str(exc)}

    def get_server_artifact(self, artifact_id):
        item = self.server_artifacts.get(artifact_id)
        return {"success": True, "artifact": item} if item is not None else None

    def list_server_artifacts(self, server_id):
        items = self.server_artifacts.list_for_server(server_id)
        return {"success": True, "count": len(items), "artifacts": items}

    def update_server_artifact_status(self, artifact_id, status):
        item = self.server_artifacts.update_status(artifact_id, status)
        return {"success": True, "artifact": item} if item is not None else None
