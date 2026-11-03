"""Transport-neutral route handlers for Statistics, economics and survey posts."""
from .services import register_post

def create_government_post(payload):
    return register_post(payload)

def get_specialization_metadata():
    return {"job_family": "science_research_and_statistics", "specialization": "statistics_economics_and_surveys", "display_name": "Statistics, economics and survey posts"}
