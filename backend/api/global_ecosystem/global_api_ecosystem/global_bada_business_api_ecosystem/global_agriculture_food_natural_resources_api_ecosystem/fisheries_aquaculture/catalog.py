"""Catalog metadata for Fisheries & Aquaculture."""
CATEGORY_ID = "fisheries_aquaculture"
CATEGORY_NAME = "Fisheries & Aquaculture"
DESCRIPTION = "Inland and marine fisheries, aquaculture, hatcheries, feed and cold-chain."
STATUS = "taxonomy_scaffold"

def get_metadata():
    return {"id": CATEGORY_ID, "name": CATEGORY_NAME, "description": DESCRIPTION, "status": STATUS}
