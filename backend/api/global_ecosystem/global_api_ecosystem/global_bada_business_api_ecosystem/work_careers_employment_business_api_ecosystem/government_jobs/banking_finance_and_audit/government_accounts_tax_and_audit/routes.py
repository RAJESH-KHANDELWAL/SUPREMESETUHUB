"""Transport-neutral route handlers for Government accounts, taxation and audit posts."""
from .services import register_post

def create_government_post(payload):
    return register_post(payload)

def get_specialization_metadata():
    return {"job_family": "banking_finance_and_audit", "specialization": "government_accounts_tax_and_audit", "display_name": "Government accounts, taxation and audit posts"}
