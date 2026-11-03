"""Transport-neutral route handlers for Scientific officer and scientist posts."""
from .services import register_post

def create_government_post(payload):
    return register_post(payload)

def get_specialization_metadata():
    return {"job_family": "science_research_and_statistics", "specialization": "scientific_officer_posts", "display_name": "Scientific officer and scientist posts"}
