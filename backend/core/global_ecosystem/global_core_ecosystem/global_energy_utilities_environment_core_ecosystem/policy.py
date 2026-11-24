ALLOWED=("LIST_DOMAINS","GET_DOMAIN","SEARCH_DOMAINS","LIST_REGIONS","GET_REGION","HEALTH")
PROHIBITED=("DISPATCH_GRID","CONTROL_POWER_PLANT","OPERATE_DAM","CONTROL_UTILITY_NETWORK","ISSUE_PERMIT","TRADE_ENERGY","STORE_SECRETS")
def is_allowed(operation): return operation.strip().upper() in ALLOWED
def policy_summary(): return {"allowed_operations":list(ALLOWED),"prohibited_operations":list(PROHIBITED),"mode":"READ_ONLY_METADATA"}
