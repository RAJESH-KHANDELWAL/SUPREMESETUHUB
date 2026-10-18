"""Canonical shared CRM domain module; ecosystem orchestration lives under SUPREME ECOSYSTEM."""
from .models import Contact
from .contact_service import ContactService

__all__ = ["Contact", "ContactService"]
