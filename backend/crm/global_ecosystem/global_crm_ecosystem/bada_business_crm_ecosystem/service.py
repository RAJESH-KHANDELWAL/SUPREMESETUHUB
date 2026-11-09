"""Bada Business CRM domain service over the canonical shared CRM service."""

from backend.crm.service import CRMService
from .catalog import get_bada_business_crm_catalog


class BadaBusinessCRMService:
    """Add Bada Business lead classification without copying CRM persistence."""

    def __init__(self, crm_service=None):
        self.crm_service = crm_service or CRMService()

    @staticmethod
    def _require_identity(owner_user_id: str, actor_user_id: str | None = None):
        if not str(owner_user_id).strip():
            raise ValueError("owner_user_id is required")
        if actor_user_id is not None and not str(actor_user_id).strip():
            raise ValueError("actor_user_id is required")

    def status(self):
        return {"success": True, **get_bada_business_crm_catalog()}

    def list_business_leads(self, owner_user_id: str, *, limit: int = 100):
        self._require_identity(owner_user_id)
        contacts = self.crm_service.list_contacts(owner_user_id, category="LEAD", limit=limit)
        return {"success": True, "count": len(contacts), "data": contacts}

    def create_business_lead(self, owner_user_id: str, actor_user_id: str, data: dict):
        self._require_identity(owner_user_id, actor_user_id)
        payload = dict(data)
        payload["category"] = "LEAD"
        payload.setdefault("source", "BADA_BUSINESS")
        payload.setdefault("consent_to_contact", False)
        return self.crm_service.create_contact(owner_user_id, actor_user_id, payload)

    def suggest_lead_category(self, record: dict):
        if not isinstance(record, dict):
            raise ValueError("record must be a mapping")
        result = self.crm_service.suggest_category(record)
        return {
            **result,
            "domain": "BADA_BUSINESS",
            "requires_human_approval": True,
            "applied": False,
        }

    def prepare_follow_up(self, owner_user_id: str, contact_id: str):
        self._require_identity(owner_user_id)
        record = self.crm_service.get_contact(owner_user_id, contact_id)
        if record is None:
            return {"success": False, "error": "CONTACT_NOT_FOUND"}
        return {
            "success": True,
            "follow_up": self.crm_service.suggest_follow_up(record),
            "message_sent": False,
            "human_approval_required": True,
        }

    def draft_outreach(self, owner_user_id: str, contact_id: str, purpose: str, tone: str = "friendly"):
        self._require_identity(owner_user_id)
        # Canonical service enforces contact consent and DO_NOT_CONTACT status.
        return self.crm_service.draft_message(owner_user_id, contact_id, purpose, tone)
