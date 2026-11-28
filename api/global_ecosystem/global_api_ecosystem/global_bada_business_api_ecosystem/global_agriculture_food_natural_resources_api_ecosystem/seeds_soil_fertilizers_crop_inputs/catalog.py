"""Catalog metadata for Seeds, Soil & Crop Inputs."""
CATEGORY_ID = "seeds_soil_fertilizers_crop_inputs"
CATEGORY_NAME = "Seeds, Soil & Crop Inputs"
DESCRIPTION = "Seed systems, nurseries, soil health, fertilizers, bio-inputs and crop protection."
STATUS = "taxonomy_scaffold"


def get_metadata():
    return {"id": CATEGORY_ID, "name": CATEGORY_NAME, "description": DESCRIPTION, "status": STATUS}
