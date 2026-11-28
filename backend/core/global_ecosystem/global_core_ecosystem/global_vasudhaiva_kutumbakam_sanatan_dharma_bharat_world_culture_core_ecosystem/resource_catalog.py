"""Evidence-aware access to existing cultural knowledge; no synthetic inventory."""
from backend.global_ecosystem.global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_ecosystem.service import CulturalKnowledgeDomainService
from .domain_catalog import list_domains
_SOURCE=CulturalKnowledgeDomainService()
def list_resource_families(): return list_domains()
def get_foundational_knowledge(): return _SOURCE.knowledge()
def search_knowledge(query: str):
    if not str(query or "").strip(): raise ValueError("CULTURAL_QUERY_REQUIRED")
    return _SOURCE.search(query)
def resource_inventory_summary(): return {"success":True,"domain_family_count":len(list_resource_families()),"resource_count":None,"resource_count_verified":False,"live_connections_verified":0,"note":"Source runtime does not expose a complete count of all cultural resources."}
