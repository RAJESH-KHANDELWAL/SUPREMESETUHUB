"""Canonical service, work and business domain taxonomy."""
DOMAINS = (
 {"domain_id":"DIGITAL_INFRASTRUCTURE","name":"Digital infrastructure","capabilities":("compute","storage","networking","edge","platform infrastructure")},
 {"domain_id":"TELECOMMUNICATIONS_NETWORK_SERVICES","name":"Telecommunications and network services","capabilities":("connectivity","mobile networks","fixed networks","voice","network operations")},
 {"domain_id":"CLOUD_HOSTING_DATA_CENTRES","name":"Cloud, hosting and data centres","capabilities":("cloud platforms","hosting","data centres","backup","disaster recovery")},
 {"domain_id":"SOFTWARE_APPLICATION_ENGINEERING","name":"Software and application engineering","capabilities":("web applications","mobile applications","APIs","integration","quality engineering")},
 {"domain_id":"IT_OPERATIONS_MANAGED_SERVICES","name":"IT operations and managed services","capabilities":("service desk","monitoring","endpoint management","maintenance","incident management")},
 {"domain_id":"AI_DATA_AUTOMATION_SERVICES","name":"AI, data and automation services","capabilities":("AI solutions","analytics","data engineering","automation","model operations")},
 {"domain_id":"CYBERSECURITY_PRIVACY_TRUST","name":"Cybersecurity, privacy and trust services","capabilities":("security assessment","identity","access management","privacy operations","resilience")},
 {"domain_id":"PROFESSIONAL_TECHNICAL_WORK","name":"Professional and technical work","capabilities":("consulting","architecture","implementation","training","technical support")},
 {"domain_id":"BUSINESS_OPERATIONS_COMMERCIAL_SERVICES","name":"Business operations and commercial services","capabilities":("sales","procurement","vendor management","partnerships","billing operations")},
 {"domain_id":"SERVICE_DELIVERY_LIFECYCLE","name":"Service delivery and lifecycle management","capabilities":("discovery","design","delivery","support","renewal and exit")},
)
_INDEX = {item["domain_id"]: item for item in DOMAINS}
def list_domains() -> list[dict]:
    return [dict(x, capabilities=list(x["capabilities"])) for x in DOMAINS]
def get_domain(domain_id: str) -> dict | None:
    x = _INDEX.get(domain_id)
    return dict(x, capabilities=list(x["capabilities"])) if x else None
