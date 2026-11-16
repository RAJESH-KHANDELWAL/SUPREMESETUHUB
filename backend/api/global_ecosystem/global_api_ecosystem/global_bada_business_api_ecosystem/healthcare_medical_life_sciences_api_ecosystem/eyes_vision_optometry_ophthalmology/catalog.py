"""Catalog metadata for Eyes & Vision Health."""
CATEGORY_ID = "eyes_vision_optometry_ophthalmology"
CATEGORY_NAME = "Eyes & Vision Health"
DESCRIPTION = "Eye anatomy, vision, optometry, ophthalmology and eye surgery."
STATUS = "taxonomy_scaffold"

def get_metadata():
    return {"id": CATEGORY_ID, "name": CATEGORY_NAME, "description": DESCRIPTION, "status": STATUS}
