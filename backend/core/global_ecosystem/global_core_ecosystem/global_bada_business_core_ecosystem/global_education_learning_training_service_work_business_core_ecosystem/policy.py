ALLOWED=("LIST_BUSINESS_DOMAINS","GET_BUSINESS_DOMAIN","FILTER_CAPABILITIES","GET_CATALOG","HEALTH")
PROHIBITED=("PROCESS_PAYMENTS","ENROLL_STUDENTS","ISSUE_ACCREDITED_CREDENTIALS","CLAIM_GOVERNMENT_APPROVAL","STORE_SENSITIVE_STUDENT_RECORDS","GUARANTEE_JOBS_OR_ADMISSIONS","EXECUTE_TRAINING")
def is_allowed(operation): return operation.strip().upper() in ALLOWED
def policy_summary(): return {"allowed_operations":list(ALLOWED),"prohibited_operations":list(PROHIBITED),"mode":"CLASSIFICATION_AND_METADATA_ONLY","compliance_note":"Operators must independently verify licensing, accreditation, privacy and safeguarding duties."}
