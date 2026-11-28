"""Outlook Mail and Calendar service-family metadata; catalog scaffold, not a live connector."""
from __future__ import annotations

SERVICE_ECOSYSTEM = {
    "provider_id": "microsoft",
    "service_id": "microsoft_outlook_mail_calendar_api",
    "name": "OUTLOOK MAIL AND CALENDAR API ECOSYSTEM",
    "scope": "Exchange Online mail, messages, folders, events, calendars, and contacts through Microsoft Graph.",
    "authentication_setup": "Graph Mail.* and Calendars.* permissions; mailbox access policy and tenant consent.",
    "documentation_required": True,
    "adapter_implemented": False,
    "live_connection_verified": False,
    "credential_persistence_implemented": False,
}

__all__ = ["SERVICE_ECOSYSTEM"]
