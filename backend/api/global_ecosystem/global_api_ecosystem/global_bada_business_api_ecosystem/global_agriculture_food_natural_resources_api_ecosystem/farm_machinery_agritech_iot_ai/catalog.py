"""Catalog metadata for Farm Machinery & AgriTech."""
CATEGORY_ID = "farm_machinery_agritech_iot_ai"
CATEGORY_NAME = "Farm Machinery & AgriTech"
DESCRIPTION = "Mechanisation, precision agriculture, sensors, drones, farm software and AI."
STATUS = "taxonomy_scaffold"


def get_metadata():
    return {"id": CATEGORY_ID, "name": CATEGORY_NAME, "description": DESCRIPTION, "status": STATUS}
