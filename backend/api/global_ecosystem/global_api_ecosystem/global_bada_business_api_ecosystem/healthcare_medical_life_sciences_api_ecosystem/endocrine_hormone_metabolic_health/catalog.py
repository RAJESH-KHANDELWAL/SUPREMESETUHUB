"""Catalog metadata for Hormones, Endocrine & Metabolic Health."""
CATEGORY_ID = "endocrine_hormone_metabolic_health"
CATEGORY_NAME = "Hormones, Endocrine & Metabolic Health"
DESCRIPTION = "Endocrine glands, hormones, thyroid, diabetes, metabolism and related disorders."
STATUS = "taxonomy_scaffold"

def get_metadata():
    return {"id": CATEGORY_ID, "name": CATEGORY_NAME, "description": DESCRIPTION, "status": STATUS}
