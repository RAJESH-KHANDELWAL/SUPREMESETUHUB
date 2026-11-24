"""VPS capability-domain taxonomy."""
from typing import Any
DOMAIN_DEFINITIONS:dict[str,dict[str,str]]={
 "PROVIDER_GOVERNANCE":{"name":"Provider Governance","purpose":"Provider Governance metadata and governance boundary."},
 "COMPUTE_AND_INSTANCE_LIFECYCLE":{"name":"Compute and Instance Lifecycle","purpose":"Compute and Instance Lifecycle metadata and governance boundary."},
 "REGIONS_AND_AVAILABILITY":{"name":"Regions and Availability","purpose":"Regions and Availability metadata and governance boundary."},
 "IMAGES_AND_OPERATING_SYSTEMS":{"name":"Images and Operating Systems","purpose":"Images and Operating Systems metadata and governance boundary."},
 "COMPUTE_SIZING_AND_CAPACITY":{"name":"Compute Sizing and Capacity","purpose":"Compute Sizing and Capacity metadata and governance boundary."},
 "NETWORKING_AND_VIRTUAL_NETWORKS":{"name":"Networking and Virtual Networks","purpose":"Networking and Virtual Networks metadata and governance boundary."},
 "IP_ADDRESSING_AND_DNS":{"name":"IP Addressing and DNS","purpose":"IP Addressing and DNS metadata and governance boundary."},
 "FIREWALLS_AND_NETWORK_SECURITY":{"name":"Firewalls and Network Security","purpose":"Firewalls and Network Security metadata and governance boundary."},
 "IDENTITY_ACCESS_AND_SSH":{"name":"Identity, Access and SSH","purpose":"Identity, Access and SSH metadata and governance boundary."},
 "BLOCK_STORAGE_AND_VOLUMES":{"name":"Block Storage and Volumes","purpose":"Block Storage and Volumes metadata and governance boundary."},
 "SNAPSHOTS_BACKUPS_AND_RECOVERY":{"name":"Snapshots, Backups and Recovery","purpose":"Snapshots, Backups and Recovery metadata and governance boundary."},
 "LOAD_BALANCING_AND_TRAFFIC":{"name":"Load Balancing and Traffic","purpose":"Load Balancing and Traffic metadata and governance boundary."},
 "MONITORING_LOGGING_AND_OBSERVABILITY":{"name":"Monitoring, Logging and Observability","purpose":"Monitoring, Logging and Observability metadata and governance boundary."},
 "BILLING_PRICING_QUOTAS_AND_USAGE":{"name":"Billing, Pricing, Quotas and Usage","purpose":"Billing, Pricing, Quotas and Usage metadata and governance boundary."},
 "COMPLIANCE_RESILIENCE_AND_GOVERNANCE":{"name":"Compliance, Resilience and Governance","purpose":"Compliance, Resilience and Governance metadata and governance boundary."},
 "AUTOMATION_AND_DEPLOYMENT":{"name":"Automation and Deployment","purpose":"Automation and Deployment metadata and governance boundary."},
}
def list_domain_inventory()->list[dict[str,str]]: return [{"domain_id":k,**v} for k,v in DOMAIN_DEFINITIONS.items()]
def domain_summary()->dict[str,Any]: return {"success":True,"ecosystem_id":"GLOBAL-VPS-CORE-ECOSYSTEM","domain_count":len(DOMAIN_DEFINITIONS),"domains":list_domain_inventory()}
