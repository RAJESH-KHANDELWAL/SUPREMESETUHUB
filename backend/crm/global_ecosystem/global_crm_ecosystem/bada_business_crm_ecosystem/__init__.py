"""Bada Business CRM domain facade."""

from .catalog import get_bada_business_crm_catalog
from .service import BadaBusinessCRMService
from .manager import BadaBusinessCRMManager

__all__ = ["get_bada_business_crm_catalog", "BadaBusinessCRMService", "BadaBusinessCRMManager"]
