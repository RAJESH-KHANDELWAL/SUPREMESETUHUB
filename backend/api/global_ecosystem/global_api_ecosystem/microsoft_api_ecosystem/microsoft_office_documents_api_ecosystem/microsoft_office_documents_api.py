"""Microsoft Office Documents service-family metadata; catalog scaffold, not a live connector."""
from __future__ import annotations

SERVICE_ECOSYSTEM = {
    "provider_id": "microsoft",
    "service_id": "microsoft_office_documents_api",
    "name": "MICROSOFT OFFICE DOCUMENTS API ECOSYSTEM",
    "scope": "Excel workbooks, Word documents, and Office file operations via Microsoft Graph.",
    "authentication_setup": "Graph Files.* and service-specific workbook permissions; supported file formats and drive access.",
    "documentation_required": True,
    "adapter_implemented": False,
    "live_connection_verified": False,
    "credential_persistence_implemented": False,
}

__all__ = ["SERVICE_ECOSYSTEM"]
