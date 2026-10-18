"""Canonical shared CRM module; ecosystem orchestration lives under SUPREME ECOSYSTEM."""
from .models import Contact
from .contact_service import ContactService
from .repository import CRMRepository
from .service import CRMService

__all__ = ["Contact", "ContactService", "CRMRepository", "CRMService"]
