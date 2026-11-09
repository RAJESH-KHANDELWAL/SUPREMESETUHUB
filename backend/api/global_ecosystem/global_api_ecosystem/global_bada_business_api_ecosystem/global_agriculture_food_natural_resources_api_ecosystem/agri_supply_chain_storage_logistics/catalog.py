"""Catalog metadata for Agri Supply Chain & Logistics."""
CATEGORY_ID = "agri_supply_chain_storage_logistics"
CATEGORY_NAME = "Agri Supply Chain & Logistics"
DESCRIPTION = "Warehousing, grading, aggregation, cold-chain, transport and market linkage."
STATUS = "taxonomy_scaffold"

def get_metadata():
    return {"id": CATEGORY_ID, "name": CATEGORY_NAME, "description": DESCRIPTION, "status": STATUS}
