"""Catalog metadata for Healthcare Business, Insurance & Regulation."""
CATEGORY_ID = "healthcare_business_insurance_regulation"
CATEGORY_NAME = "Healthcare Business, Insurance & Regulation"
DESCRIPTION = "Health insurance, claims, medical billing, accreditation, licensing, compliance and healthcare enterprises."
STATUS = "taxonomy_scaffold"

def get_metadata():
    return {"id": CATEGORY_ID, "name": CATEGORY_NAME, "description": DESCRIPTION, "status": STATUS}
