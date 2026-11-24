"""CRM ecosystem facade over the existing canonical CRM service."""

from backend.crm.service import CRMService
from .catalog import get_global_crm_catalog


class GlobalCRMService:
    """Expose shared CRM behavior without duplicating repository or models."""

    def __init__(self, crm_service=None):
        self.crm_service = crm_service or CRMService()

    def status(self):
        catalog = get_global_crm_catalog()
        return {
            "success": True,
            **catalog,
            "service_available": True,
            "storage_backend": "backend.database.service.DatabaseService",
        }

    def report(self, owner_user_id: str):
        if not str(owner_user_id).strip():
            raise ValueError("owner_user_id is required")
        return self.crm_service.report(owner_user_id)

    def list_contacts(self, owner_user_id: str, **filters):
        if not str(owner_user_id).strip():
            raise ValueError("owner_user_id is required")
        return self.crm_service.list_contacts(owner_user_id, **filters)

    def create_contact(self, owner_user_id: str, actor_user_id: str, data: dict):
        if not str(owner_user_id).strip() or not str(actor_user_id).strip():
            raise ValueError("owner_user_id and actor_user_id are required")
        return self.crm_service.create_contact(owner_user_id, actor_user_id, data)

    def preview_import(self, owner_user_id: str, provider: str, records: list[dict], column_map=None):
        if not str(owner_user_id).strip():
            raise ValueError("owner_user_id is required")
        return self.crm_service.preview_import(owner_user_id, provider, records, column_map)
