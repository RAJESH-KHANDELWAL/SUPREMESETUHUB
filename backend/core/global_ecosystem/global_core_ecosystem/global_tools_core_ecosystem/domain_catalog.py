"""Cross-provider responsibility taxonomy."""
from collections import Counter
from .product_catalog import list_products
DOMAIN_DEFINITIONS={
  "PROVIDER_GOVERNANCE": {
    "name": "Provider Governance"
  },
  "DEVELOPER_SOURCE_CONTROL": {
    "name": "Developer Tools and Source Control"
  },
  "CLOUD_INFRASTRUCTURE": {
    "name": "Cloud and Infrastructure Tools"
  },
  "PRODUCTIVITY_COLLABORATION": {
    "name": "Productivity and Collaboration"
  },
  "AI_DEVELOPER_TOOLS": {
    "name": "AI and Developer Intelligence"
  },
  "CRM_BUSINESS_APPLICATIONS": {
    "name": "CRM and Business Applications"
  },
  "ADVERTISING_MONETIZATION": {
    "name": "Advertising and Monetization"
  },
  "MARKETING_SEO": {
    "name": "Marketing and SEO"
  },
  "COMMUNICATION_CUSTOMER_ENGAGEMENT": {
    "name": "Communications and Customer Engagement"
  },
  "DATA_ANALYTICS": {
    "name": "Data and Analytics"
  },
  "OBSERVABILITY_ANALYTICS": {
    "name": "Observability and Monitoring"
  },
  "AUTOMATION_WORKFLOW": {
    "name": "Automation and Workflow"
  },
  "DESIGN_CREATIVE_MEDIA": {
    "name": "Design, Creative and Media"
  },
  "SECURITY_IDENTITY": {
    "name": "Security, Identity and Compliance"
  },
  "PAYMENTS_COMMERCE_BILLING": {
    "name": "Payments, Commerce and Billing"
  },
  "HOSTING_WEB_DEPLOYMENT": {
    "name": "Hosting, Web and Deployment"
  },
  "IT_SERVICE_MANAGEMENT": {
    "name": "IT Service Management and Support"
  },
  "TESTING_QUALITY": {
    "name": "Testing, Quality and Release"
  },
  "INTEGRATION_API": {
    "name": "Integration, API and iPaaS"
  },
  "DOCUMENTATION_KNOWLEDGE": {
    "name": "Documentation and Knowledge"
  }
}
CATEGORY_TO_DOMAIN={"PROJECT_MANAGEMENT":"PRODUCTIVITY_COLLABORATION","DOCUMENTATION_KNOWLEDGE":"DOCUMENTATION_KNOWLEDGE","DEVELOPER_SOURCE_CONTROL":"DEVELOPER_SOURCE_CONTROL","IT_SERVICE_MANAGEMENT":"IT_SERVICE_MANAGEMENT","COMMUNICATION_COLLABORATION":"COMMUNICATION_CUSTOMER_ENGAGEMENT","DEVELOPER_CLOUD_TOOLS":"CLOUD_INFRASTRUCTURE","INFRASTRUCTURE_AUTOMATION":"AUTOMATION_WORKFLOW","OBSERVABILITY_ANALYTICS":"OBSERVABILITY_ANALYTICS","CI_CD_RELEASE":"TESTING_QUALITY","SECURITY_IDENTITY":"SECURITY_IDENTITY","ADVERTISING_MONETIZATION":"ADVERTISING_MONETIZATION","DATA_ANALYTICS":"DATA_ANALYTICS","AUTOMATION_WORKFLOW":"AUTOMATION_WORKFLOW","AI_DEVELOPER_TOOLS":"AI_DEVELOPER_TOOLS","TESTING_QUALITY":"TESTING_QUALITY","CRM_BUSINESS_APPLICATIONS":"CRM_BUSINESS_APPLICATIONS","MARKETING_SEO":"MARKETING_SEO","INTEGRATION_API":"INTEGRATION_API"}
def list_domains():
 c=Counter(CATEGORY_TO_DOMAIN.get(x["category"],"PROVIDER_GOVERNANCE") for x in list_products())
 return [{"domain_id":k,**v,"offering_count":c.get(k,0)} for k,v in DOMAIN_DEFINITIONS.items()]
def domain_summary():
 d=list_domains(); return {"success":True,"domain_count":len(d),"offering_count":sum(x["offering_count"] for x in d),"domains":d}
