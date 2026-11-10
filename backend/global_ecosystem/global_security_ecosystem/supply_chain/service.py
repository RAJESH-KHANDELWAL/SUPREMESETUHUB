"""Third-party and software supply-chain security review."""
def assess_supplier_security(*, security_questionnaire, incident_contact, data_access_scoped, subprocessors_disclosed, exit_plan):
    checks={"security_review_missing":security_questionnaire,"incident_contact_missing":incident_contact,"data_access_scope_missing":data_access_scoped,"subprocessor_disclosure_missing":subprocessors_disclosed,"supplier_exit_plan_missing":exit_plan}
    return tuple(name for name, ok in checks.items() if not ok)
