"""Transport-neutral route handlers for Public bank clerical and customer operations."""
from .services import register_post

def create_government_post(payload):
    return register_post(payload)

def get_specialization_metadata():
    return {"job_family": "banking_finance_and_audit", "specialization": "bank_clerical_and_customer_operations", "display_name": "Public bank clerical and customer operations"}
