"""Catalog metadata for ENT, Dental & Oral Health."""
CATEGORY_ID = "ear_nose_throat_dental_oral_health"
CATEGORY_NAME = "ENT, Dental & Oral Health"
DESCRIPTION = "Ear, nose, throat, hearing, speech, teeth, gums, jaw and oral-maxillofacial care."
STATUS = "taxonomy_scaffold"

def get_metadata():
    return {"id": CATEGORY_ID, "name": CATEGORY_NAME, "description": DESCRIPTION, "status": STATUS}
