"""Bharat-to-global application domain and lifecycle taxonomy.
This is discovery metadata, not proof that listed apps or integrations are live.
"""
from __future__ import annotations
from typing import Any
APP_MATURITY_LEVELS = (
 {"id":"catalogued","name":"Catalogued application","status":"CATALOG_ONLY"},
 {"id":"documented","name":"Documented integration requirements","status":"DOCUMENTATION"},
 {"id":"scaffolded","name":"Integration scaffold","status":"SCAFFOLD"},
 {"id":"configured","name":"Configured provider integration","status":"CONFIGURED"},
 {"id":"verified","name":"Verified live integration","status":"LIVE_VERIFIED"},
)
APP_CAPABILITY_LEVELS = (
 {"id":"normal_basic","name":"Normal / Basic","description":"Everyday single-purpose applications and foundational user workflows."},
 {"id":"standard","name":"Standard","description":"Reliable multi-feature apps with standard integrations and accessibility."},
 {"id":"professional","name":"Professional","description":"Advanced workflows, productivity, collaboration and business use."},
 {"id":"advanced","name":"Advanced","description":"Complex automation, interoperability, analytics and multi-platform delivery."},
 {"id":"expert","name":"Expert","description":"Specialist-grade applications with robust controls and domain workflows."},
 {"id":"enterprise_industrial","name":"Enterprise / Industrial","description":"Large-scale, mission-critical, governed and highly available applications."},
 {"id":"research_frontier","name":"Research / Frontier","description":"Experimental and emerging application paradigms under evaluation."},
 {"id":"supreme_long_horizon","name":"Supreme / Long-horizon","description":"Aspirational future-facing capability tier; not a claim of achieved superintelligence."},
)

APP_SCOPE_DOMAINS: tuple[dict[str, Any], ...] = (
 {"id":"bharat_india_apps","name":"Bharat and India apps","examples":["Indic-language apps","DigiLocker","UMANG","BHIM","UPI apps","Indian public-service apps"]},
 {"id":"global_world_regional_apps","name":"Global, world and regional apps","examples":["country-specific apps","regional app markets","cross-border consumer apps"]},
 {"id":"mobile_android_ios_apps","name":"Mobile apps","examples":["Android apps","iOS apps","wearable companion apps"]},
 {"id":"desktop_system_apps","name":"Desktop and system apps","examples":["Windows apps","macOS apps","Linux apps","system utilities"]},
 {"id":"web_pwa_browser_apps","name":"Web, PWA and browser apps","examples":["web applications","progressive web apps","browser extensions"]},
 {"id":"business_enterprise_saas_apps","name":"Business, enterprise and SaaS apps","examples":["ERP","CRM","HRMS","accounting","workflow automation"]},
 {"id":"productivity_collaboration_apps","name":"Productivity and collaboration apps","examples":["documents","spreadsheets","notes","project management","team collaboration"]},
 {"id":"communication_messaging_apps","name":"Communication and messaging apps","examples":["email","chat","voice","video meetings","community messaging"]},
 {"id":"social_networking_creator_apps","name":"Social networking and creator apps","examples":["social networks","creator platforms","publishing","communities"]},
 {"id":"commerce_marketplace_retail_apps","name":"Commerce, marketplace and retail apps","examples":["ecommerce","marketplaces","POS","inventory","D2C storefronts"]},
 {"id":"banking_finance_payment_apps","name":"Banking, finance and payment apps","examples":["banking","UPI","wallets","investing","insurance","accounting"]},
 {"id":"education_learning_research_apps","name":"Education, learning and research apps","examples":["LMS","tutoring","language learning","research tools","digital libraries"]},
 {"id":"healthcare_wellness_fitness_apps","name":"Healthcare, wellness and fitness apps","examples":["telehealth","health records","fitness","wellness","care navigation"],"safeguards":["privacy","clinical_scope_limits","qualified_professional_oversight"]},
 {"id":"travel_transport_mobility_apps","name":"Travel, transport and mobility apps","examples":["booking","maps","navigation","ride-hailing","logistics","public transport"]},
 {"id":"food_grocery_delivery_apps","name":"Food, grocery and delivery apps","examples":["food ordering","restaurant platforms","grocery","last-mile delivery"]},
 {"id":"media_entertainment_streaming_apps","name":"Media, entertainment and streaming apps","examples":["video streaming","music","podcasts","gaming","digital publishing"]},
 {"id":"design_creative_content_apps","name":"Design and creative apps","examples":["graphic design","video editing","photo editing","3D","animation","publishing"]},
 {"id":"developer_software_engineering_apps","name":"Developer and software engineering apps","examples":["IDEs","source control","CI/CD","API clients","testing","observability"]},
 {"id":"cloud_storage_backup_apps","name":"Cloud, storage and backup apps","examples":["cloud consoles","file sync","backup","object storage clients"]},
 {"id":"cybersecurity_privacy_identity_apps","name":"Cybersecurity, privacy and identity apps","examples":["password managers","MFA","endpoint security","VPN","identity wallets"],"safeguards":["secure_by_design","least_privilege","privacy"]},
 {"id":"government_civic_public_service_apps","name":"Government, civic and public-service apps","examples":["citizen services","tax","identity","public records","municipal services"],"safeguards":["accessibility","transparency","privacy","non_discrimination"]},
 {"id":"real_estate_home_lifestyle_apps","name":"Real estate, home and lifestyle apps","examples":["property search","property management","smart home","home services"]},
 {"id":"agriculture_environment_industry_apps","name":"Agriculture, environment and industrial apps","examples":["farm management","IoT dashboards","manufacturing","supply chain","climate tools"]},
 {"id":"adult_age_restricted_platform_apps","name":"Lawful age-restricted adult platform apps","examples":["age assurance","creator account tools","content rights management","moderation and safety"],"safeguards":["adults_only","verified_consent","content_rights","no_minors","no_nonconsensual_intimate_content","applicable_law"]},
 {"id":"accessibility_assistive_apps","name":"Accessibility and assistive apps","examples":["screen readers","captioning","communication aids","assistive input"]},
 {"id":"app_distribution_store_ecosystems","name":"App stores and distribution ecosystems","examples":["Google Play","Apple App Store","Microsoft Store","enterprise app distribution","F-Droid"]},
 {"id":"app_development_delivery_platforms","name":"App development, testing and delivery platforms","examples":["no-code builders","low-code platforms","app frameworks","device labs","release management"]},

 {"id":"adult_dating_relationship_apps","name":"Adult dating and relationship apps","examples":["adult dating","matchmaking","relationship communication","consent and boundary education"],"safeguards":["adults_only_where_required","age_assurance","consent","privacy","anti_harassment","no_exploitation","applicable_law"]},
 {"id":"adult_creator_subscription_apps","name":"Adult creator and subscription platform apps","examples":["adult creator account management","subscription billing","creator payouts","rights and takedown workflows"],"safeguards":["adults_only","verified_creator_identity_where_lawful","informed_consent","content_rights","privacy","no_minors","no_nonconsensual_intimate_content","applicable_law"]},
 {"id":"adult_entertainment_streaming_apps","name":"Lawful adult entertainment and streaming apps","examples":["age-restricted adult video platforms","lawful adult streaming catalogs","content labeling and access controls"],"safeguards":["adults_only","age_assurance","verified_consent_and_rights","privacy","no_minors","no_nonconsensual_intimate_content","no_trafficking_or_exploitation","applicable_law"]},
 {"id":"sexual_wellness_education_apps","name":"Sexual wellness and education apps","examples":["sexual health education","intimacy education","reproductive health information","consent education"],"safeguards":["age_appropriate_access","privacy","medical_scope_limits","qualified_professional_oversight_where_needed","applicable_law"]},
 {"id":"adult_content_safety_rights_apps","name":"Adult content safety, rights and compliance apps","examples":["age assurance","consent and release records","content rights management","moderation","reporting and takedowns","privacy controls"],"safeguards":["adults_only","informed_consent","verified_rights","no_minors","no_nonconsensual_intimate_content","no_exploitation","auditability","applicable_law"]},
)
def get_scope_catalog() -> dict[str, list[dict[str, Any]]]:
 return {"maturity_levels":[dict(x) for x in APP_MATURITY_LEVELS],"domains":[{**x,"examples":list(x.get("examples",[])),"safeguards":list(x.get("safeguards",[]))} for x in APP_SCOPE_DOMAINS]}
def get_domain(domain_id: str) -> dict[str, Any] | None:
 for item in APP_SCOPE_DOMAINS:
  if item["id"]==domain_id:return {**item,"examples":list(item.get("examples",[])),"safeguards":list(item.get("safeguards",[]))}
 return None
def list_domain_ids() -> tuple[str,...]: return tuple(x["id"] for x in APP_SCOPE_DOMAINS)
__all__=["APP_MATURITY_LEVELS","APP_CAPABILITY_LEVELS","APP_SCOPE_DOMAINS","get_scope_catalog","get_domain","list_domain_ids"]
