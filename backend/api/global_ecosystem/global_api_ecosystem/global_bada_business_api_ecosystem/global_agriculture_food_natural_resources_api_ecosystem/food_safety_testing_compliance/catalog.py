"""Catalog metadata for Food Safety & Compliance."""
CATEGORY_ID = "food_safety_testing_compliance"
CATEGORY_NAME = "Food Safety & Compliance"
DESCRIPTION = "Food testing, traceability, standards, licensing and regulatory workflows."
STATUS = "taxonomy_scaffold"

def get_metadata():
    return {"id": CATEGORY_ID, "name": CATEGORY_NAME, "description": DESCRIPTION, "status": STATUS}
