"""GOOGLE GMAIL CORE ECOSYSTEM package."""
from ..gmail_core import GoogleGmailCoreService
from .service import GoogleGmailProductCoreService

ECOSYSTEM_ID = "GOOGLE-GMAIL-CORE-ECOSYSTEM"
ECOSYSTEM_NAME = "GOOGLE GMAIL CORE ECOSYSTEM"
__all__ = ["GoogleGmailCoreService", "ECOSYSTEM_ID", "ECOSYSTEM_NAME", "GoogleGmailProductCoreService"]
