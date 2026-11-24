"""Common cloud capability taxonomy; exact support varies by provider and region."""
CLOUD_CAPABILITIES={
"compute":("virtual_machines","containers","serverless","gpu_compute","bare_metal"),
"storage":("object_storage","block_storage","file_storage","archive","backup","sync_and_share"),
"data":("relational_database","document_database","cache","warehouse","streaming"),
"network":("vpc","load_balancing","cdn","dns","private_connectivity","edge"),
"platform":("kubernetes","container_registry","application_hosting","ci_cd"),
"security":("identity_and_access","key_management","secrets","audit_logs","threat_protection"),
"governance":("policy","compliance_evidence","cost_management","resource_inventory"),
}
__all__=["CLOUD_CAPABILITIES"]
