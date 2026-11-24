"""Catalog metadata for Medical Research, Clinical Trials & Education."""
CATEGORY_ID = "medical_research_trials_education_training"
CATEGORY_NAME = "Medical Research, Clinical Trials & Education"
DESCRIPTION = "Research ethics, clinical trials, medical colleges, professional training and certification."
STATUS = "taxonomy_scaffold"

def get_metadata():
    return {"id": CATEGORY_ID, "name": CATEGORY_NAME, "description": DESCRIPTION, "status": STATUS}
