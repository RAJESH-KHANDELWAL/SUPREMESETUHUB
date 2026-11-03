"""Transport-neutral route handlers for Civil engineering government posts."""
from .services import register_post

def create_government_post(payload):
    return register_post(payload)

def get_specialization_metadata():
    return {"job_family": "engineering_and_technical", "specialization": "civil_engineering_posts", "display_name": "Civil engineering government posts"}
