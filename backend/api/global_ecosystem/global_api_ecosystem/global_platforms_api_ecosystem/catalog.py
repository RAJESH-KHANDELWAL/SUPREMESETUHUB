"""Controlled taxonomy for platform discovery; not a live platform directory."""
PLATFORM_DOMAINS = [
 {"domain_id":"ai_data","name":"AI, Data and Automation","subdomains":["artificial_intelligence","machine_learning","data_analytics","automation","developer_ai"]},
 {"domain_id":"communication","name":"Communication and Communities","subdomains":["messaging","email","video_conferencing","social_networks","online_communities"]},
 {"domain_id":"content_media","name":"Content and Media","subdomains":["video","audio_music","publishing","streaming","creator_monetization"]},
 {"domain_id":"commerce","name":"Commerce and Marketplaces","subdomains":["ecommerce","marketplace","retail","classifieds","subscriptions"]},
 {"domain_id":"finance_payments","name":"Finance and Payments","subdomains":["payments","banking","fintech","accounting","insurance","investing"]},
 {"domain_id":"work_business","name":"Work and Business Operations","subdomains":["freelancing","recruitment","crm","erp","project_management","business_services"]},
 {"domain_id":"cloud_infrastructure","name":"Cloud and Infrastructure","subdomains":["cloud_compute","hosting","storage","cdn","identity_security"]},
 {"domain_id":"software_development","name":"Software Development and Distribution","subdomains":["code_hosting","ci_cd","api_marketplace","app_stores","no_code_low_code"]},
 {"domain_id":"education","name":"Education and Learning","subdomains":["online_learning","courses","tutoring","research","certification"]},
 {"domain_id":"health_wellness","name":"Health and Wellness","subdomains":["telehealth","fitness","wellness","health_records"]},
 {"domain_id":"travel_transport","name":"Travel and Transport","subdomains":["travel_booking","mobility","delivery","logistics"]},
 {"domain_id":"public_services","name":"Government and Public Services","subdomains":["government_portals","public_information","civic_services"]},
 {"domain_id":"adult_industry","name":"Lawful Adult Industry (18+)","subdomains":["adult_content_publishing","adult_creator_platforms","adult_entertainment_distribution","adult_subscription_services"],"adult_only":True,"minimum_age":18},
]
PLATFORM_TYPES = ["web_platform","mobile_platform","desktop_platform","cloud_platform","marketplace_platform","social_platform","messaging_platform","creator_platform","payment_platform","developer_platform","saas_platform","infrastructure_platform","content_distribution_platform","government_digital_platform","adult_industry_platform"]
OWNERSHIP_TYPES = ["private_company","public_company","government","nonprofit","cooperative","community_owned","individual_operator","unknown"]
BUSINESS_MODELS = ["free","freemium","subscription","transaction_fee","advertising","usage_based","licensing","donation","mixed","unknown"]
VERIFICATION_STATES = ["unverified","source_checked","identity_verified","operator_verified","suspended"]
