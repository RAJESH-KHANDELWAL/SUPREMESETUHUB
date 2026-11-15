"""Canonical ownership map for existing infrastructure domains."""
from .schemas import CatalogRecord

SERVICES = (
    CatalogRecord("backup", "Backup", "domain_service", "Canonical module: backend.infrastructure.backup."),
    CatalogRecord("billing", "Billing", "domain_service", "Canonical module: backend.infrastructure.billing."),
    CatalogRecord("cdn", "CDN", "domain_service", "Canonical module: backend.infrastructure.cdn."),
    CatalogRecord("containers", "Containers", "domain_service", "Canonical module: backend.infrastructure.containers."),
    CatalogRecord("database", "Database", "domain_service", "Infrastructure checks live here; database persistence is owned by backend.database."),
    CatalogRecord("dns", "DNS", "domain_service", "Canonical module: backend.infrastructure.dns."),
    CatalogRecord("domains", "Domains", "domain_service", "Canonical module: backend.infrastructure.domains."),
    CatalogRecord("email", "Email", "domain_service", "Canonical module: backend.infrastructure.email."),
    CatalogRecord("firewall", "Firewall", "domain_service", "Canonical module: backend.infrastructure.firewall."),
    CatalogRecord("ftp", "FTP", "domain_service", "Canonical module: backend.infrastructure.ftp."),
    CatalogRecord("hosting", "Hosting", "domain_service", "Canonical module: backend.infrastructure.hosting."),
    CatalogRecord("ipam", "IPAM", "domain_service", "Canonical module: backend.infrastructure.ipam."),
    CatalogRecord("load_balancer", "Load Balancer", "domain_service", "Canonical module: backend.infrastructure.load_balancer."),
    CatalogRecord("monitoring", "Monitoring", "domain_service", "Canonical module: backend.infrastructure.monitoring."),
    CatalogRecord("network", "Network", "domain_service", "Canonical module: backend.infrastructure.network."),
    CatalogRecord("object_storage", "Object Storage", "domain_service", "Canonical module: backend.infrastructure.object_storage."),
    CatalogRecord("security", "Security", "domain_service", "Canonical module: backend.infrastructure.security."),
    CatalogRecord("server", "Server", "domain_service", "Inventory module: backend.infrastructure.server; canonical ecosystem: backend.server."),
    CatalogRecord("ssl", "SSL", "domain_service", "Canonical module: backend.infrastructure.ssl."),
    CatalogRecord("storage", "Storage", "domain_service", "Canonical module: backend.infrastructure.storage; storage implementation remains backend.storage."),
)
