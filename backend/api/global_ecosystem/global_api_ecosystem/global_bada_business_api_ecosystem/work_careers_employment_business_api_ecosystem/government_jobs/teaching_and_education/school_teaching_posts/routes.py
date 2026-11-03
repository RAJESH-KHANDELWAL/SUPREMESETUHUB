"""Transport-neutral route handlers for School teaching posts."""
from .services import register_post

def create_government_post(payload):
    return register_post(payload)

def get_specialization_metadata():
    return {"job_family": "teaching_and_education", "specialization": "school_teaching_posts", "display_name": "School teaching posts"}
