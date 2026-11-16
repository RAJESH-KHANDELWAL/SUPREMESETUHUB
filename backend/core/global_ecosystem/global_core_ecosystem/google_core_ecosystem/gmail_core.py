"""Backward-compatible import for the Gmail product Core service.

OAuth and message transport are implemented only in the Google Gmail API
adapter. This module now delegates to the shared Core metadata/policy service.
"""
from .google_gmail_core_ecosystem.service import GoogleGmailProductCoreService

GoogleGmailCoreService = GoogleGmailProductCoreService

__all__ = ["GoogleGmailCoreService", "GoogleGmailProductCoreService"]
