"""Source-aware registry of classification standards; not a substitute for source datasets."""
from copy import deepcopy

CLASSIFICATIONS = (
    {"id": "india-nic-2025", "name": "National Industrial Classification 2025", "publisher": "Ministry of Statistics and Programme Implementation, Government of India", "jurisdiction": ["IN"], "version": "2025", "released": "2025-11-18", "status": "metadata_verified_dataset_not_yet_ingested", "hierarchy": ["section", "division", "group", "class", "subclass"], "code_depth": "6-digit subclass", "counts": {"sections": 22, "divisions": 87, "groups": 257, "classes": 463, "subclasses": 1887}, "aligned_with": "isic-rev-5", "source_url": "https://www.mospi.gov.in/classification", "workbook_url": "https://www.mospi.gov.in/uploads/publications_reports/publications_reports1763618655097_29a4a622-fa4c-47e9-abba-b549e27a1bbb_NIC_2025.xlsx", "publication_url": "https://www.mospi.gov.in/uploads/publications_reports/publications_reports1763457214315_c3e5d4f3-8e25-4775-85e3-ad42d571652f_NIC_2025_Final.pdf"},
    {"id": "isic-rev-5", "name": "International Standard Industrial Classification, Revision 5", "publisher": "United Nations Statistics Division", "jurisdiction": ["UN"], "version": "Revision 5", "status": "standard_registered_source_dataset_not_yet_ingested", "hierarchy": ["section", "division", "group", "class"], "source_url": "https://unstats.un.org/unsd/classifications/Econ"},
    {"id": "naics-2022", "name": "North American Industry Classification System 2022", "publisher": "Statistics Canada; Instituto Nacional de Estadística y Geografía; U.S. Office of Management and Budget", "jurisdiction": ["CA", "MX", "US"], "version": "2022", "status": "standard_registered_source_dataset_not_yet_ingested", "hierarchy": ["sector", "subsector", "industry_group", "industry", "national_industry"], "source_url": "https://www.census.gov/naics/"},
    {"id": "nace-rev-2-1", "name": "Statistical Classification of Economic Activities in the European Community", "publisher": "Eurostat", "jurisdiction": ["EU"], "version": "Rev. 2.1", "status": "standard_registered_source_dataset_not_yet_ingested", "hierarchy": ["section", "division", "group", "class"], "source_url": "https://ec.europa.eu/eurostat/web/nace"},
    {"id": "india-nco-2015", "name": "National Classification of Occupations 2015", "publisher": "Directorate General of Employment, Ministry of Labour and Employment, Government of India", "jurisdiction": ["IN"], "version": "2015", "status": "official_source_identified_dataset_not_yet_ingested", "hierarchy": ["division", "subdivision", "group", "family", "occupation"], "code_depth": "8-digit occupation code", "aligned_with": "isco-08", "source_url": "https://www.dge.gov.in/nco-2015"},
    {"id": "isco-08", "name": "International Standard Classification of Occupations 2008", "publisher": "International Labour Organization", "jurisdiction": ["UN"], "version": "2008", "status": "standard_registered_source_dataset_not_yet_ingested", "hierarchy": ["major_group", "sub_major_group", "minor_group", "unit_group"], "counts": {"major_groups": 10, "sub_major_groups": 43, "minor_groups": 130, "unit_groups": 436}, "source_url": "https://isco.ilo.org/en/isco-08/"},
    {"id": "esco-v1-2-1", "name": "European Skills, Competences, Qualifications and Occupations", "publisher": "European Commission", "jurisdiction": ["EU"], "version": "1.2.1", "status": "standard_registered_source_dataset_not_yet_ingested", "hierarchy": ["occupation", "skills_competences_knowledge"], "source_url": "https://esco.ec.europa.eu/en/classification/occupation-main"},
    {"id": "cpc-v3-0", "name": "Central Product Classification Version 3.0", "publisher": "United Nations Statistics Division", "jurisdiction": ["UN"], "version": "3.0", "status": "draft_structure_forthcoming_publication_source_registered", "hierarchy": ["section", "division", "group", "class", "subclass"], "source_url": "https://unstats.un.org/unsd/classifications/Econ/cpc"},
)

COUNTRY_SYSTEMS = (
    {"country_code": "IN", "country": "India", "classification_id": "india-nic-2025", "status": "registered"},
    {"country_code": "US", "country": "United States", "classification_id": "naics-2022", "status": "registered"},
    {"country_code": "CA", "country": "Canada", "classification_id": "naics-2022", "status": "registered"},
    {"country_code": "MX", "country": "Mexico", "classification_id": "naics-2022", "status": "registered"},
    {"country_code": "EU", "country": "European Union", "classification_id": "nace-rev-2-1", "status": "registered"},
    {"country_code": "GB", "country": "United Kingdom", "classification_id": None, "status": "source_dataset_required", "candidate_system": "UK SIC"},
    {"country_code": "AU", "country": "Australia", "classification_id": None, "status": "source_dataset_required", "candidate_system": "ANZSIC"},
    {"country_code": "NZ", "country": "New Zealand", "classification_id": None, "status": "source_dataset_required", "candidate_system": "ANZSIC"},
    {"country_code": "JP", "country": "Japan", "classification_id": None, "status": "source_dataset_required", "candidate_system": "Japan Standard Industrial Classification"},
    {"country_code": "KR", "country": "South Korea", "classification_id": None, "status": "source_dataset_required", "candidate_system": "Korean Standard Industrial Classification"},
)

def list_classifications():
    return deepcopy(list(CLASSIFICATIONS))

def get_classification(classification_id):
    return next((deepcopy(item) for item in CLASSIFICATIONS if item["id"] == classification_id), None)

def list_country_systems():
    return deepcopy(list(COUNTRY_SYSTEMS))

def validate_classification_registry():
    ids = [item["id"] for item in CLASSIFICATIONS]
    return {"registry_status": "metadata_registry", "classification_count": len(ids), "duplicate_ids": sorted({value for value in ids if ids.count(value) > 1}), "country_system_count": len(COUNTRY_SYSTEMS), "dataset_ingested_count": sum("dataset_not_yet_ingested" not in item["status"] for item in CLASSIFICATIONS), "nic_2025_dataset_ingested": False, "crosswalks_loaded": False, "structurally_valid": len(ids) == len(set(ids))}
