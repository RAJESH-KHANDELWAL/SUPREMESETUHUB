"""Catalog metadata for Research, Education & Extension."""
CATEGORY_ID = "agri_research_education_extension"
CATEGORY_NAME = "Research, Education & Extension"
DESCRIPTION = "Research institutions, training, extension services, skills and certifications."
STATUS = "taxonomy_scaffold"

def get_metadata():
    return {"id": CATEGORY_ID, "name": CATEGORY_NAME, "description": DESCRIPTION, "status": STATUS}
