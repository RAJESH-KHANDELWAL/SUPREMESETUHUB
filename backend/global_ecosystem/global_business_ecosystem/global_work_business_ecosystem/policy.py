"""Guardrails for interpreting work and workforce labels."""
CLASSIFICATION_DIMENSIONS=("occupation","employment_status","work_arrangement","business_role","ownership_role","legal_entity")
def classification_notice():
    return ("Occupation, employment status, work arrangement, business role, ownership "
            "and legal entity are separate dimensions. A catalogue label does not determine "
            "employee status, tax treatment, licensing or legal form.")
