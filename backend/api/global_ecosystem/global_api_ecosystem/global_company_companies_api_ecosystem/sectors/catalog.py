"""Company sector catalogue, independent of legal-entity classification."""
from .models import SectorRecord
SECTORS=(
SectorRecord("primary","Primary Industries","Production based on natural resources.",("agriculture-forestry-fishing","mining-quarrying")),
SectorRecord("secondary","Secondary Industries","Manufacturing, utilities and construction.",("manufacturing","electricity-gas-utilities","water-waste-environment","construction-infrastructure")),
SectorRecord("trade","Trade and Consumer Markets","Wholesale, retail and consumer-facing trade.",("wholesale-retail-trade",)),
SectorRecord("transport-logistics","Transport and Logistics","Movement, storage and supply-chain services.",("transport-storage-logistics",)),
SectorRecord("hospitality","Hospitality and Tourism","Accommodation, food and visitor services.",("accommodation-food-services",)),
SectorRecord("digital-technology","Digital and Communications","Information, software and communications.",("information-communications",)),
SectorRecord("financial-services","Financial Services","Finance, insurance and related services.",("finance-insurance",)),
SectorRecord("property","Property and Real Estate","Real-estate ownership, leasing and services.",("real-estate",)),
SectorRecord("professional-services","Professional Services","Scientific, technical and administrative services.",("professional-scientific-technical","administrative-support")),
SectorRecord("public-social-services","Public and Social Services","Public administration, education, health and social work.",("public-administration","education","human-health-social-work")),
SectorRecord("creative-recreation","Creative and Recreation","Arts, entertainment and recreation.",("arts-entertainment-recreation",)),
SectorRecord("other-services","Other Services","Other service activities and international organizations.",("other-services","international-organizations")))
def _dict(x): return {"sector_id":x.sector_id,"name":x.name,"description":x.description,"industry_ids":list(x.industry_ids),"status":x.status}
def list_sectors(): return [_dict(x) for x in SECTORS]
def get_sector(sector_id):
 x=next((x for x in SECTORS if x.sector_id==(sector_id or "").strip().casefold()),None)
 return _dict(x) if x else None
def search_sectors(query):
 q=(query or "").strip().casefold()
 return [x for x in list_sectors() if q and (q in x["sector_id"].casefold() or q in x["name"].casefold() or q in x["description"].casefold())]
def validate_sector_catalog():
 ids=[x.sector_id for x in SECTORS]
 return {"structurally_valid":bool(ids) and len(ids)==len(set(ids)),"sector_count":len(ids),"duplicate_ids":sorted({x for x in ids if ids.count(x)>1}),"registry_status":"curated_taxonomy","live_data_connected":False}
