"""Transport-neutral route handlers for Education leadership and specialist support posts."""
from .services import register_post

def create_government_post(payload):
    return register_post(payload)

def get_specialization_metadata():
    return {"job_family": "teaching_and_education", "specialization": "education_support_and_leadership", "display_name": "Education leadership and specialist support posts"}
