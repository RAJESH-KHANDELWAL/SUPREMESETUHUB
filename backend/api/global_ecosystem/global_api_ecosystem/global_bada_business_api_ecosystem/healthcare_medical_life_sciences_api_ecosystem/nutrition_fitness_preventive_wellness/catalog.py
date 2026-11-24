"""Catalog metadata for Nutrition, Fitness & Preventive Wellness."""
CATEGORY_ID = "nutrition_fitness_preventive_wellness"
CATEGORY_NAME = "Nutrition, Fitness & Preventive Wellness"
DESCRIPTION = "Clinical nutrition, dietetics, fitness, preventive health and lifestyle medicine."
STATUS = "taxonomy_scaffold"

def get_metadata():
    return {"id": CATEGORY_ID, "name": CATEGORY_NAME, "description": DESCRIPTION, "status": STATUS}
