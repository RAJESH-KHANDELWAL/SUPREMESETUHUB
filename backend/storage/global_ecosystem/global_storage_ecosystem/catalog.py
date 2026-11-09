"""STORAGE-owned canonical provider and category taxonomy."""
from copy import deepcopy
ROOT_ID = "GLOBAL-STORAGE-ECOSYSTEM"
PROVIDERS = [
    {
        "provider_id": "adobe",
        "name": "Adobe",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "anthropic",
        "name": "Anthropic",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "apple",
        "name": "Apple",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "atlassian",
        "name": "Atlassian",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "aws",
        "name": "Aws",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "bada_business",
        "name": "Bada Business",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "cohere",
        "name": "Cohere",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "deepseek",
        "name": "Deepseek",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "digitalocean",
        "name": "Digitalocean",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "github",
        "name": "Github",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "global_ai",
        "name": "Global Ai",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "global_app",
        "name": "Global App",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "global_cloud",
        "name": "Global Cloud",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "global_cloudflare",
        "name": "Global Cloudflare",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "global_communication",
        "name": "Global Communication",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "global_company_companies",
        "name": "Global Company Companies",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "global_database",
        "name": "Global Database",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "global_developer",
        "name": "Global Developer",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "global_domain",
        "name": "Global Domain",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "global_entity_relationships",
        "name": "Global Entity Relationships",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "global_hosting",
        "name": "Global Hosting",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "global_individual",
        "name": "Global Individual",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "global_integrations",
        "name": "Global Integrations",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "global_kamasutra_intimacy_relationship_sex_chudai_porn_adult_health_wellness",
        "name": "Global Kamasutra Intimacy Relationship Sex Chudai Porn Adult Health Wellness",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "global_language",
        "name": "Global Language",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "global_organizations",
        "name": "Global Organizations",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "global_payment",
        "name": "Global Payment",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "global_people_life",
        "name": "Global People Life",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "global_platforms",
        "name": "Global Platforms",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "global_programming_language",
        "name": "Global Programming Language",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "global_security",
        "name": "Global Security",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "global_server",
        "name": "Global Server",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "global_social_media",
        "name": "Global Social Media",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "global_software",
        "name": "Global Software",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "global_storage",
        "name": "Global Storage",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "global_system",
        "name": "Global System",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "global_tools",
        "name": "Global Tools",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "global_video",
        "name": "Global Video",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "global_vps",
        "name": "Global Vps",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "global_web",
        "name": "Global Web",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "global_website",
        "name": "Global Website",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "google",
        "name": "Google",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "huggingface",
        "name": "Huggingface",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "ibm",
        "name": "Ibm",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "mega",
        "name": "Mega",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "meta",
        "name": "Meta",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "microsoft",
        "name": "Microsoft",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "mistral",
        "name": "Mistral",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "nsfwinfra",
        "name": "Nsfwinfra",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "nvidia",
        "name": "Nvidia",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "openai",
        "name": "Openai",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "oracle",
        "name": "Oracle",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "paypal",
        "name": "Paypal",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "proton",
        "name": "Proton",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "salesforce",
        "name": "Salesforce",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "shopify",
        "name": "Shopify",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "slack",
        "name": "Slack",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "stripe",
        "name": "Stripe",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    },
    {
        "provider_id": "twilio",
        "name": "Twilio",
        "capabilities": [
            "STORAGE_DISCOVERY",
            "PROVIDER_ADAPTER_CONTRACT"
        ],
        "status": "NOT_CONFIGURED",
        "implementation_state": "CATALOG_ONLY"
    }
]
CATEGORIES = [
    {
        "category_id": "ai",
        "name": "AI",
        "ecosystem_id": "GLOBAL-AI-STORAGE-ECOSYSTEM",
        "status": "CATALOG_ONLY"
    },
    {
        "category_id": "app",
        "name": "APP",
        "ecosystem_id": "GLOBAL-APP-STORAGE-ECOSYSTEM",
        "status": "CATALOG_ONLY"
    },
    {
        "category_id": "bada_business",
        "name": "BADA BUSINESS",
        "ecosystem_id": "GLOBAL-BADA-BUSINESS-STORAGE-ECOSYSTEM",
        "status": "CATALOG_ONLY"
    },
    {
        "category_id": "cloud",
        "name": "CLOUD",
        "ecosystem_id": "GLOBAL-CLOUD-STORAGE-ECOSYSTEM",
        "status": "CATALOG_ONLY"
    },
    {
        "category_id": "cloudflare",
        "name": "CLOUDFLARE",
        "ecosystem_id": "GLOBAL-CLOUDFLARE-STORAGE-ECOSYSTEM",
        "status": "CATALOG_ONLY"
    },
    {
        "category_id": "communication",
        "name": "COMMUNICATION",
        "ecosystem_id": "GLOBAL-COMMUNICATION-STORAGE-ECOSYSTEM",
        "status": "CATALOG_ONLY"
    },
    {
        "category_id": "company_companies",
        "name": "COMPANY COMPANIES",
        "ecosystem_id": "GLOBAL-COMPANY-COMPANIES-STORAGE-ECOSYSTEM",
        "status": "CATALOG_ONLY"
    },
    {
        "category_id": "database",
        "name": "DATABASE",
        "ecosystem_id": "GLOBAL-DATABASE-STORAGE-ECOSYSTEM",
        "status": "CATALOG_ONLY"
    },
    {
        "category_id": "developer",
        "name": "DEVELOPER",
        "ecosystem_id": "GLOBAL-DEVELOPER-STORAGE-ECOSYSTEM",
        "status": "CATALOG_ONLY"
    },
    {
        "category_id": "domain",
        "name": "DOMAIN",
        "ecosystem_id": "GLOBAL-DOMAIN-STORAGE-ECOSYSTEM",
        "status": "CATALOG_ONLY"
    },
    {
        "category_id": "entity_relationships",
        "name": "ENTITY RELATIONSHIPS",
        "ecosystem_id": "GLOBAL-ENTITY-RELATIONSHIPS-STORAGE-ECOSYSTEM",
        "status": "CATALOG_ONLY"
    },
    {
        "category_id": "hosting",
        "name": "HOSTING",
        "ecosystem_id": "GLOBAL-HOSTING-STORAGE-ECOSYSTEM",
        "status": "CATALOG_ONLY"
    },
    {
        "category_id": "individual",
        "name": "INDIVIDUAL",
        "ecosystem_id": "GLOBAL-INDIVIDUAL-STORAGE-ECOSYSTEM",
        "status": "CATALOG_ONLY"
    },
    {
        "category_id": "integrations",
        "name": "INTEGRATIONS",
        "ecosystem_id": "GLOBAL-INTEGRATIONS-STORAGE-ECOSYSTEM",
        "status": "CATALOG_ONLY"
    },
    {
        "category_id": "kamasutra_intimacy_relationship_sex_chudai_porn_adult_health_wellness",
        "name": "KAMASUTRA INTIMACY RELATIONSHIP SEX CHUDAI PORN ADULT HEALTH WELLNESS",
        "ecosystem_id": "GLOBAL-KAMASUTRA-INTIMACY-RELATIONSHIP-SEX-CHUDAI-PORN-ADULT-HEALTH-WELLNESS-STORAGE-ECOSYSTEM",
        "status": "CATALOG_ONLY"
    },
    {
        "category_id": "language",
        "name": "LANGUAGE",
        "ecosystem_id": "GLOBAL-LANGUAGE-STORAGE-ECOSYSTEM",
        "status": "CATALOG_ONLY"
    },
    {
        "category_id": "organizations",
        "name": "ORGANIZATIONS",
        "ecosystem_id": "GLOBAL-ORGANIZATIONS-STORAGE-ECOSYSTEM",
        "status": "CATALOG_ONLY"
    },
    {
        "category_id": "payment",
        "name": "PAYMENT",
        "ecosystem_id": "GLOBAL-PAYMENT-STORAGE-ECOSYSTEM",
        "status": "CATALOG_ONLY"
    },
    {
        "category_id": "people_life",
        "name": "PEOPLE LIFE",
        "ecosystem_id": "GLOBAL-PEOPLE-LIFE-STORAGE-ECOSYSTEM",
        "status": "CATALOG_ONLY"
    },
    {
        "category_id": "platforms",
        "name": "PLATFORMS",
        "ecosystem_id": "GLOBAL-PLATFORMS-STORAGE-ECOSYSTEM",
        "status": "CATALOG_ONLY"
    },
    {
        "category_id": "programming_language",
        "name": "PROGRAMMING LANGUAGE",
        "ecosystem_id": "GLOBAL-PROGRAMMING-LANGUAGE-STORAGE-ECOSYSTEM",
        "status": "CATALOG_ONLY"
    },
    {
        "category_id": "security",
        "name": "SECURITY",
        "ecosystem_id": "GLOBAL-SECURITY-STORAGE-ECOSYSTEM",
        "status": "CATALOG_ONLY"
    },
    {
        "category_id": "server",
        "name": "SERVER",
        "ecosystem_id": "GLOBAL-SERVER-STORAGE-ECOSYSTEM",
        "status": "CATALOG_ONLY"
    },
    {
        "category_id": "social_media",
        "name": "SOCIAL MEDIA",
        "ecosystem_id": "GLOBAL-SOCIAL-MEDIA-STORAGE-ECOSYSTEM",
        "status": "CATALOG_ONLY"
    },
    {
        "category_id": "software",
        "name": "SOFTWARE",
        "ecosystem_id": "GLOBAL-SOFTWARE-STORAGE-ECOSYSTEM",
        "status": "CATALOG_ONLY"
    },
    {
        "category_id": "storage",
        "name": "STORAGE",
        "ecosystem_id": "GLOBAL-STORAGE-STORAGE-ECOSYSTEM",
        "status": "CATALOG_ONLY"
    },
    {
        "category_id": "system",
        "name": "SYSTEM",
        "ecosystem_id": "GLOBAL-SYSTEM-STORAGE-ECOSYSTEM",
        "status": "CATALOG_ONLY"
    },
    {
        "category_id": "tools",
        "name": "TOOLS",
        "ecosystem_id": "GLOBAL-TOOLS-STORAGE-ECOSYSTEM",
        "status": "CATALOG_ONLY"
    },
    {
        "category_id": "video",
        "name": "VIDEO",
        "ecosystem_id": "GLOBAL-VIDEO-STORAGE-ECOSYSTEM",
        "status": "CATALOG_ONLY"
    },
    {
        "category_id": "vps",
        "name": "VPS",
        "ecosystem_id": "GLOBAL-VPS-STORAGE-ECOSYSTEM",
        "status": "CATALOG_ONLY"
    },
    {
        "category_id": "web",
        "name": "WEB",
        "ecosystem_id": "GLOBAL-WEB-STORAGE-ECOSYSTEM",
        "status": "CATALOG_ONLY"
    },
    {
        "category_id": "website",
        "name": "WEBSITE",
        "ecosystem_id": "GLOBAL-WEBSITE-STORAGE-ECOSYSTEM",
        "status": "CATALOG_ONLY"
    }
]
def get_provider_catalog(): return deepcopy(PROVIDERS)
def get_category_catalog(): return deepcopy(CATEGORIES)
def get_catalog():
    records=[{"ecosystem_id":ROOT_ID,"name":"GLOBAL STORAGE ECOSYSTEM","ecosystem_type":"STORAGE_ROOT","parent_id":None,"capabilities":["OBJECT_STORAGE","FILE_STORAGE","STORAGE_DISCOVERY","OBJECT_METADATA","STORAGE_LIFECYCLE"],"metadata":{"layer":"STORAGE","independent":True}}]
    for c in CATEGORIES:
        records.append({"ecosystem_id":c["ecosystem_id"],"name":"GLOBAL "+c["name"]+" STORAGE ECOSYSTEM","ecosystem_type":"STORAGE_CATEGORY","parent_id":ROOT_ID,"capabilities":["STORAGE_NAMESPACE"],"metadata":{"category_id":c["category_id"],"implementation_state":"CATALOG_ONLY"}})
    for p in PROVIDERS:
        pid=p["provider_id"]
        records.append({"ecosystem_id":"GLOBAL-"+pid.upper().replace("_","-")+"-STORAGE-ECOSYSTEM","name":"GLOBAL "+p["name"].upper()+" STORAGE ECOSYSTEM","ecosystem_type":"STORAGE_PROVIDER","parent_id":ROOT_ID,"capabilities":list(p["capabilities"]),"status":"NOT_CONFIGURED","metadata":{"provider_id":pid,"implementation_state":"CATALOG_ONLY","connection_state":"NOT_CONFIGURED"}})
    return records
