"""Company-specific classification standards directory."""
DOMAIN_ID="company_classification_standards"
DOMAIN_NAME="Company Classification Standards"
ADULT_RESTRICTED=False
DEFAULT_DISCOVERY_ENABLED=True
SUBCATEGORY_IDS=("legal_entity_classification","ownership_classification","control_relationship_classification","corporate_group_classification","enterprise_size_classification","company_status_classification","jurisdictional_legal_form_mapping","cross_border_entity_mapping","identifier_and_registration_mapping","source_and_verification_levels")
def list_subcategories(): return [{"id":x,"name":x.replace("_"," ").title(),"domain_id":DOMAIN_ID} for x in SUBCATEGORY_IDS]
