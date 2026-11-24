"""Guardrails for independent work and business classification."""
CLASSIFICATION_DIMENSIONS=("work_status","contract_type","business_ownership","business_size","tax_status","licensing","jurisdiction")
def classification_notice():
    return ("Freelancer, contractor, gig worker, self-employed person and entrepreneur "
            "can overlap but are not identical. The catalogue does not determine worker "
            "classification, tax status, licensing or legal compliance.")
