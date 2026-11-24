"""Canonical shared CRM module; ecosystem orchestration lives under SUPREME ECOSYSTEM."""
from .models import Contact
from .contact_service import ContactService
from .repository import CRMRepository
from .service import CRMService
from .global_ecosystem.global_crm_ecosystem import GlobalCRMManager, GlobalCRMService
from .global_ecosystem.global_crm_ecosystem.bada_business_crm_ecosystem import (
    BadaBusinessCRMManager,
    BadaBusinessCRMService,
)

__all__ = [
    "Contact", "ContactService", "CRMRepository", "CRMService",
    "GlobalCRMManager", "GlobalCRMService",
    "BadaBusinessCRMManager", "BadaBusinessCRMService",
]
