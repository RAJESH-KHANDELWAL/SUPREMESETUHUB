ALLOWED_OPERATIONS=("LIST_DOMAINS","GET_DOMAIN","SEARCH_DOMAINS","GET_CATALOG","GET_REGION","HEALTH")
RESTRICTED_OPERATIONS=("CREATE_JOB_CONTRACT","PROCESS_PAYMENTS","HOLD_ESCROW","VERIFY_IDENTITY","STORE_PERSONAL_DATA","ISSUE_LEGAL_OR_TAX_ADVICE","GUARANTEE_EMPLOYMENT","EXECUTE_MARKETPLACE_TRANSACTIONS")
WORK_MODES=("independent","freelance","gig","remote","hybrid","work_from_home","part_time","full_time","on_site","project_based","contract","temporary","seasonal","microtask")
def is_allowed(operation): return operation.strip().upper() in ALLOWED_OPERATIONS
def policy_summary(): return {"mode":"METADATA_AND_DISCOVERY_ONLY","allowed_operations":list(ALLOWED_OPERATIONS),"restricted_operations":list(RESTRICTED_OPERATIONS),"work_modes":list(WORK_MODES)}
