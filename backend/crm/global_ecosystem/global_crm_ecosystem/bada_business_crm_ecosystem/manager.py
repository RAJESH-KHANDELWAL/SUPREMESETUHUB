"""Public manager for BADA BUSINESS CRM ECOSYSTEM."""

from .service import BadaBusinessCRMService


class BadaBusinessCRMManager:
    def __init__(self, service=None):
        self.service = service or BadaBusinessCRMService()

    def status(self):
        return self.service.status()

    def list_business_leads(self, owner_user_id: str, *, limit: int = 100):
        return self.service.list_business_leads(owner_user_id, limit=limit)

    def create_business_lead(self, owner_user_id: str, actor_user_id: str, data: dict):
        return self.service.create_business_lead(owner_user_id, actor_user_id, data)

    def suggest_lead_category(self, record: dict):
        return self.service.suggest_lead_category(record)

    def prepare_follow_up(self, owner_user_id: str, contact_id: str):
        return self.service.prepare_follow_up(owner_user_id, contact_id)

    def draft_outreach(self, owner_user_id: str, contact_id: str, purpose: str, tone: str = "friendly"):
        return self.service.draft_outreach(owner_user_id, contact_id, purpose, tone)
