"""Catalog metadata for Heart, Blood Vessels & Circulation."""
CATEGORY_ID = "heart_blood_vessels_circulation"
CATEGORY_NAME = "Heart, Blood Vessels & Circulation"
DESCRIPTION = "Cardiology, vascular medicine, circulation, blood pressure and cardiovascular surgery."
STATUS = "taxonomy_scaffold"

def get_metadata():
    return {"id": CATEGORY_ID, "name": CATEGORY_NAME, "description": DESCRIPTION, "status": STATUS}
