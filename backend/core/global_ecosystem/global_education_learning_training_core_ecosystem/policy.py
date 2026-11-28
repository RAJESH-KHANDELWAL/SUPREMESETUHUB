ALLOWED=("LIST_DOMAINS","GET_DOMAIN","SEARCH_DOMAINS","GET_CATALOG","HEALTH")
PROHIBITED=("ENROLL_LEARNERS","ISSUE_CREDENTIALS","COLLECT_FEES","RUN_EXAMS","STORE_STUDENT_RECORDS","DELIVER_PAID_TRAINING")
def is_allowed(operation): return operation.strip().upper() in ALLOWED
def policy_summary(): return {"allowed_operations":list(ALLOWED),"prohibited_operations":list(PROHIBITED),"mode":"METADATA_ONLY"}
