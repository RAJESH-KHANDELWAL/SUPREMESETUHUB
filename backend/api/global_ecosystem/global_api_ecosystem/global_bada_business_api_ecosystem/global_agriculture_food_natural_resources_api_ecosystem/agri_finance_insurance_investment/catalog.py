"""Catalog metadata for Agri Finance & Insurance."""
CATEGORY_ID = "agri_finance_insurance_investment"
CATEGORY_NAME = "Agri Finance & Insurance"
DESCRIPTION = "Agricultural credit, insurance, risk products, investment and financial inclusion."
STATUS = "taxonomy_scaffold"

def get_metadata():
    return {"id": CATEGORY_ID, "name": CATEGORY_NAME, "description": DESCRIPTION, "status": STATUS}
