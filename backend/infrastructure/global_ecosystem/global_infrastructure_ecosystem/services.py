"""Canonical ownership map for infrastructure domains migrated into this ecosystem."""
from .schemas import CatalogRecord

_BASE = "backend.infrastructure.global_ecosystem.global_infrastructure_ecosystem"

SERVICES = (
    CatalogRecord("backup", "Backup", "domain_service", f"Canonical module: {_BASE}.backup."),
    CatalogRecord("billing", "Billing", "domain_service", f"Canonical module: {_BASE}.billing."),
    CatalogRecord("cdn", "CDN", "domain_service", f"Canonical module: {_BASE}.cdn."),
    CatalogRecord("containers", "Containers", "domain_service", f"Canonical module: {_BASE}.containers."),
    CatalogRecord("database", "Database", "domain_service", f"Infrastructure adapters: {_BASE}.database; persistence remains backend.database."),
    CatalogRecord("dns", "DNS", "domain_service", f"Canonical module: {_BASE}.dns."),
    CatalogRecord("domains", "Domains", "domain_service", f"Canonical module: {_BASE}.domains."),
    CatalogRecord("email", "Email", "domain_service", f"Canonical module: {_BASE}.email."),
    CatalogRecord("firewall", "Firewall", "domain_service", f"Canonical module: {_BASE}.firewall."),
    CatalogRecord("ftp", "FTP", "domain_service", f"Canonical module: {_BASE}.ftp."),
    CatalogRecord("hosting", "Hosting", "domain_service", f"Canonical module: {_BASE}.hosting."),
    CatalogRecord("ipam", "IPAM", "domain_service", f"Canonical module: {_BASE}.ipam."),
    CatalogRecord("load_balancer", "Load Balancer", "domain_service", f"Canonical module: {_BASE}.load_balancer."),
    CatalogRecord("model", "Infrastructure Models", "domain_service", f"Canonical module: {_BASE}.model."),
    CatalogRecord("monitoring", "Monitoring", "domain_service", f"Canonical module: {_BASE}.monitoring."),
    CatalogRecord("network", "Network", "domain_service", f"Canonical module: {_BASE}.network."),
    CatalogRecord("object_storage", "Object Storage", "domain_service", f"Canonical module: {_BASE}.object_storage."),
    CatalogRecord("security", "Security", "domain_service", f"Canonical module: {_BASE}.security."),
    CatalogRecord("server", "Server", "domain_service", f"Inventory module: {_BASE}.server; canonical server ecosystem: backend.server."),
    CatalogRecord("ssl", "SSL", "domain_service", f"Canonical module: {_BASE}.ssl."),
    CatalogRecord("storage", "Storage", "domain_service", f"Inventory module: {_BASE}.storage; storage implementation remains backend.storage."),
    CatalogRecord("hostinger", "Hostinger Integration", "provider_adapter", "Existing adapters: backend.infrastructure.hostinger_api and backend.infrastructure.hostinger_catalog."),
    CatalogRecord("nsfwinfra", "NSFW Infrastructure", "domain_service", "Existing module: backend.infrastructure.nsfwinfra; subject to dedicated safety and policy governance."),
)
