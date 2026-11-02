"""Company-facing industry taxonomy; metadata only."""
INDUSTRY_ECOSYSTEMS=(
("agriculture-forestry-fishing","Agriculture, Forestry and Fishing"),("mining-quarrying","Mining and Quarrying"),
("manufacturing","Manufacturing"),("electricity-gas-utilities","Electricity, Gas and Utilities"),
("water-waste-environment","Water, Waste and Environmental Services"),("construction-infrastructure","Construction and Infrastructure"),
("wholesale-retail-trade","Wholesale and Retail Trade"),("transport-storage-logistics","Transport, Storage and Logistics"),
("accommodation-food-services","Accommodation and Food Services"),("information-communications","Information and Communications"),
("finance-insurance","Finance and Insurance"),("real-estate","Real Estate"),
("professional-scientific-technical","Professional, Scientific and Technical Services"),("administrative-support","Administrative and Support Services"),
("public-administration","Public Administration"),("education","Education"),("human-health-social-work","Human Health and Social Work"),
("arts-entertainment-recreation","Arts, Entertainment and Recreation"),("other-services","Other Services"),
("international-organizations","International Organizations"))
def list_industries():
 return [{"id":i,"industry_id":i,"name":n,"classification_status":"curated_taxonomy","profile_count":0,"live_data_connected":False} for i,n in INDUSTRY_ECOSYSTEMS]
def get_industry(industry_id): return next((x for x in list_industries() if x["industry_id"]==industry_id),None)
def search_industries(query):
 q=(query or "").strip().casefold()
 return [x for x in list_industries() if q and (q in x["industry_id"].casefold() or q in x["name"].casefold())]
def validate_industry_registry():
 ids=[x[0] for x in INDUSTRY_ECOSYSTEMS]
 return {"structurally_valid":bool(ids) and len(ids)==len(set(ids)),"industry_count":len(ids),"duplicate_ids":sorted({x for x in ids if ids.count(x)>1}),"registry_status":"curated_taxonomy","live_data_connected":False}
