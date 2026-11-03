"""Transport-neutral route handlers for College and university faculty posts."""
from .services import register_post

def create_government_post(payload):
    return register_post(payload)

def get_specialization_metadata():
    return {"job_family": "teaching_and_education", "specialization": "higher_education_faculty", "display_name": "College and university faculty posts"}
