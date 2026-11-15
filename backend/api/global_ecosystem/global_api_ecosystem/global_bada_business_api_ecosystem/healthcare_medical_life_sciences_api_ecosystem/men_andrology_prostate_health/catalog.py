"""Catalog metadata for Men, Andrology & Prostate Health."""
CATEGORY_ID = "men_andrology_prostate_health"
CATEGORY_NAME = "Men, Andrology & Prostate Health"
DESCRIPTION = "Men's health, andrology, prostate, testicular and male reproductive medicine."
STATUS = "taxonomy_scaffold"

def get_metadata():
    return {"id": CATEGORY_ID, "name": CATEGORY_NAME, "description": DESCRIPTION, "status": STATUS}
