"""Capability domain catalog."""
DOMAINS=[
  {
    "id": "IDENTITY_AUTH",
    "name": "Identity and Authorization",
    "products": [
      "identity_oauth"
    ]
  },
  {
    "id": "API",
    "name": "API Interfaces and Composition",
    "products": [
      "rest",
      "soap",
      "composite"
    ]
  },
  {
    "id": "DATA_OPERATIONS",
    "name": "Data Operations",
    "products": [
      "bulk",
      "data_cloud"
    ]
  },
  {
    "id": "DEVELOPER_PLATFORM",
    "name": "Developer and Metadata Platform",
    "products": [
      "apex",
      "metadata_tooling"
    ]
  },
  {
    "id": "ANALYTICS_REPORTING",
    "name": "Analytics and Reporting",
    "products": [
      "analytics"
    ]
  },
  {
    "id": "CONTENT",
    "name": "Files and Content",
    "products": [
      "files_content"
    ]
  },
  {
    "id": "MARKETING",
    "name": "Marketing",
    "products": [
      "marketing_cloud"
    ]
  },
  {
    "id": "SERVICE",
    "name": "Customer Service",
    "products": [
      "service_cloud"
    ]
  },
  {
    "id": "EVENTS",
    "name": "Event Streaming",
    "products": [
      "platform_events_pubsub",
      "streaming"
    ]
  }
]
def list_domains(): return [dict(d,products=list(d["products"])) for d in DOMAINS]
def get_domain(domain_id):
    target=str(domain_id).strip().upper()
    return next((dict(d,products=list(d["products"])) for d in DOMAINS if d["id"]==target),None)
