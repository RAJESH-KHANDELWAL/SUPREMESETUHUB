"""Public manager for GLOBAL CRM ECOSYSTEM."""

from .service import GlobalCRMService


class GlobalCRMManager:
    def __init__(self, service=None):
        self.service = service or GlobalCRMService()

    def status(self):
        return self.service.status()

    def report(self, owner_user_id: str):
        return self.service.report(owner_user_id)

    def list_contacts(self, owner_user_id: str, **filters):
        return self.service.list_contacts(owner_user_id, **filters)

    def create_contact(self, owner_user_id: str, actor_user_id: str, data: dict):
        return self.service.create_contact(owner_user_id, actor_user_id, data)

    def preview_import(self, owner_user_id: str, provider: str, records: list[dict], column_map=None):
        return self.service.preview_import(owner_user_id, provider, records, column_map)
