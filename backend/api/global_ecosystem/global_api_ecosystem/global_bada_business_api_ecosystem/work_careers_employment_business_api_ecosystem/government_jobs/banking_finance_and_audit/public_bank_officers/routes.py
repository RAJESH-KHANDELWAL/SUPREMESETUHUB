"""Transport-neutral route handlers for Public sector bank officer posts."""
from .services import register_post

def create_government_post(payload):
    return register_post(payload)

def get_specialization_metadata():
    return {"job_family": "banking_finance_and_audit", "specialization": "public_bank_officers", "display_name": "Public sector bank officer posts"}
