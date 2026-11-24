"""Corporate group taxonomy package."""
DOMAIN_ID="corporate_groups"
DOMAIN_NAME="Corporate Groups"
ADULT_RESTRICTED=False
DEFAULT_DISCOVERY_ENABLED=True
SUBCATEGORY_IDS=("corporate_group","parent_company_group","holding_group","subsidiary_group","wholly_owned_subsidiary","partially_owned_subsidiary","associate_company","joint_venture_group","multinational_group","conglomerate_group","cross_border_corporate_group","family_owned_group","state_owned_group","listed_group","privately_held_group","group_headquarters","group_structure","group_ownership","group_governance","group_reorganization")
def list_subcategories(): return [{"id":x,"name":x.replace("_"," ").title(),"domain_id":DOMAIN_ID} for x in SUBCATEGORY_IDS]
