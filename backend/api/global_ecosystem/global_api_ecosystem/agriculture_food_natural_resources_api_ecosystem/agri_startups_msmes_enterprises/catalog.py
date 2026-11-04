"""Catalog metadata for Agri Startups & Enterprises."""
CATEGORY_ID = "agri_startups_msmes_enterprises"
CATEGORY_NAME = "Agri Startups & Enterprises"
DESCRIPTION = "Agri startups, MSMEs, cooperatives, FPOs, enterprise operations and consulting."
STATUS = "taxonomy_scaffold"

def get_metadata():
    return {"id": CATEGORY_ID, "name": CATEGORY_NAME, "description": DESCRIPTION, "status": STATUS}
