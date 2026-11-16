"""Provider-neutral infrastructure capability catalog."""
from .schemas import CatalogRecord

_CAPABILITIES = (
    ("compute", "Compute", "Servers, VPS, virtual machines and compute capacity."),
    ("cloud", "Cloud Platform", "Cloud resource discovery and lifecycle metadata."),
    ("datacenter", "Data Center", "Facility, rack, region and availability-zone metadata."),
    ("virtualization", "Virtualization", "Hypervisor and virtual machine management contracts."),
    ("containers", "Containers", "Container runtime and orchestration metadata."),
    ("network", "Networking", "Networks, subnets, routes and connectivity."),
    ("ipam", "IP Address Management", "IP address allocation and inventory."),
    ("dns", "DNS", "DNS zones and record inventory."),
    ("domains", "Domains", "Domain registration and renewal metadata."),
    ("load_balancing", "Load Balancing", "Traffic distribution and health-check contracts."),
    ("cdn", "CDN", "Content delivery and edge configuration metadata."),
    ("storage", "Storage", "Block, file and object storage metadata."),
    ("database", "Database", "Database instances, engines and connection metadata."),
    ("backup", "Backup", "Backup policy, retention and restore-point metadata."),
    ("security", "Security", "Security posture and policy metadata."),
    ("firewall", "Firewall", "Firewall rules and policy contracts."),
    ("ssl", "TLS / SSL", "Certificate inventory and expiry monitoring."),
    ("monitoring", "Monitoring", "Metrics, logs, probes and alert metadata."),
    ("disaster_recovery", "Disaster Recovery", "Recovery objectives and recovery-plan metadata."),
    ("billing", "Billing", "Usage and cost metadata; no payment execution."),
    ("deployment", "Deployment", "Deployment targets and release metadata."),
    ("secrets", "Secrets", "Secret references and rotation metadata; never secret values."),
    ("configuration", "Configuration Management", "Desired-state and configuration metadata."),
    ("api_gateway", "API Gateway", "Gateway and ingress configuration metadata."),
    ("email", "Email", "Mail service and delivery configuration metadata."),
    ("ftp_sftp", "FTP / SFTP", "File-transfer endpoint and profile metadata."),
    ("identity", "Identity and Access", "Identity, role and access-policy metadata."),
    ("high_availability", "High Availability", "Redundancy and failover metadata."),
    ("orchestration", "Resource Orchestration", "Cross-domain dependency and lifecycle planning."),
    ("audit", "Audit", "Change history and evidence metadata."),
)

CAPABILITIES = tuple(
    CatalogRecord(key, name, "infrastructure_capability", description)
    for key, name, description in _CAPABILITIES
)
