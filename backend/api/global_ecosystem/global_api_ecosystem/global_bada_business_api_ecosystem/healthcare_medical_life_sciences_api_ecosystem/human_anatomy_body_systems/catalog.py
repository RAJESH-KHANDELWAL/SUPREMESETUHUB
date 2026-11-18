"""Catalog metadata for Human Anatomy & Body Systems."""
CATEGORY_ID = "human_anatomy_body_systems"
CATEGORY_NAME = "Human Anatomy & Body Systems"
DESCRIPTION = "Whole-body anatomy and physiology: cells, tissues, organs, organ systems, body regions and specialist clinical anatomy."
STATUS = "taxonomy_scaffold"

def get_metadata():
    return {"id": CATEGORY_ID, "name": CATEGORY_NAME, "description": DESCRIPTION, "status": STATUS}
