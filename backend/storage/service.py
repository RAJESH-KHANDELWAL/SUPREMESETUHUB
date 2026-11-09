"""MAIN BASE FOUNDATION storage facade.

Delegates metadata initialization to the existing storage infrastructure
service so the core boot path does not maintain a second storage schema.
"""

from backend.infrastructure.storage.service import StorageService as StorageInfrastructureService


class StorageService:
    def __init__(self):
        self.infrastructure = None

    def initialize(self):
        if self.infrastructure is None:
            self.infrastructure = StorageInfrastructureService()
        self.infrastructure.initialize()
        return {
            "storage": "MAIN BASE FOUNDATION",
            "status": "Ready",
            "backing_service": "backend.infrastructure.storage.StorageService",
            "metadata_store": "SQLite",
        }
