"""Distinct AI provider and adjacent integration inventories."""
from .catalog import list_ai_providers,list_adjacent_integrations,get_ai_provider
def list_ai_offerings(): return list_ai_providers()
def list_partner_integrations(): return list_adjacent_integrations()
def get_ai_offering(provider_id): return get_ai_provider(provider_id)
