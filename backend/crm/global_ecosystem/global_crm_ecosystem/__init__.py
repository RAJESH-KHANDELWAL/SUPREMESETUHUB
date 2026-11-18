"""Global CRM domain facade."""

from .catalog import get_global_crm_catalog
from .service import GlobalCRMService
from .manager import GlobalCRMManager

__all__ = ["get_global_crm_catalog", "GlobalCRMService", "GlobalCRMManager"]
