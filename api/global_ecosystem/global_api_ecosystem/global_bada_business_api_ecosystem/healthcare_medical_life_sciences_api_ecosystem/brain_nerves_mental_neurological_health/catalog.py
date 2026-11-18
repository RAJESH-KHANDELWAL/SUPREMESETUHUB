"""Catalog metadata for Brain, Nervous System & Mental Health."""
CATEGORY_ID = "brain_nerves_mental_neurological_health"
CATEGORY_NAME = "Brain, Nervous System & Mental Health"
DESCRIPTION = "Brain, spinal cord, nerves, cognition, neurology, psychiatry and mental healthcare."
STATUS = "taxonomy_scaffold"

def get_metadata():
    return {"id": CATEGORY_ID, "name": CATEGORY_NAME, "description": DESCRIPTION, "status": STATUS}
