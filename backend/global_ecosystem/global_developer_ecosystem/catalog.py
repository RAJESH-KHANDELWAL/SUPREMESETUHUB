"""Bharat-to-global software and developer ecosystem catalog."""
GEOGRAPHIC_SCOPES = ("bharat_india","india_state","india_district","south_asia","asia_pacific","middle_east","africa","europe","north_america","latin_america_caribbean","oceania","global_cross_border")
MATURITY_LEVELS = ("normal","standard","professional","advanced","expert","enterprise","research","frontier","supreme")
DEVELOPER_DOMAINS = {
"software_engineering":("application_development","system_software","desktop_software","mobile_software"),
"web_engineering":("websites","web_apps","frontend","backend","headless_cms","ecommerce"),
"api_and_integration":("rest_api","graphql","webhooks","sdk","identity_federation","integration_platforms"),
"ai_and_data":("ai_apps","machine_learning","llm_applications","data_engineering","analytics","vector_search"),
"platform_and_cloud":("cloud_native","containers","serverless","edge","hosting","platform_engineering"),
"devops_and_reliability":("ci_cd","infrastructure_as_code","observability","site_reliability","release_engineering"),
"security_and_privacy":("secure_development","application_security","privacy_engineering","threat_modeling","accessibility"),
"databases_and_storage":("relational","document","graph","vector","object_storage","distributed_storage"),
"developer_tools":("ide","cli","debugging","testing","documentation","code_generation"),
"open_source_and_community":("open_source_projects","package_ecosystems","maintainers","developer_communities"),
"enterprise_and_industry":("erp","crm","workflow_automation","industrial_software","government_technology"),
"gaming_and_interactive":("game_engines","multiplayer_services","xr","simulation"),
"adult_only_content_technology":("age_assurance","consent_and_model_release_records","adult_creator_platforms","lawful_adult_content_management","content_moderation","copyright_and_takedowns","privacy_preserving_subscriptions","payout_compliance"),
}
PROHIBITED_USE_CASES = ("sexual_content_involving_minors","non_consensual_intimate_imagery","coercion_exploitation_or_trafficking","doxxing_or_private_data_exposure","malware_or_unauthorized_access")
def get_catalog() -> dict:
    return {"geographic_scopes":list(GEOGRAPHIC_SCOPES),"maturity_levels":list(MATURITY_LEVELS),"domains":{k:list(v) for k,v in DEVELOPER_DOMAINS.items()},"prohibited_use_cases":list(PROHIBITED_USE_CASES),"implementation_status":"CATALOG_ONLY"}
