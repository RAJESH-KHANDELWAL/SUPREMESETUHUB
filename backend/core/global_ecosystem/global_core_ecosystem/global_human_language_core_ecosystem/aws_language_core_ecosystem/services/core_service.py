"""Reusable Human Language CORE provider service for AWS LANGUAGE."""
from ...module_service import HumanLanguageProviderCoreService
from ..ecosystem_config import PROVIDER_ID

service = HumanLanguageProviderCoreService(PROVIDER_ID)
