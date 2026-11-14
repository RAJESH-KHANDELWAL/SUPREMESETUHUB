"""Integration declarations with explicit verification states."""
from .schemas import CatalogRecord

INTEGRATIONS = (
    CatalogRecord("hostinger_api", "Hostinger API", "provider_adapter", "Read-only inventory client exists; credentials and live connectivity must be verified.", "CATALOG_ONLY"),
    CatalogRecord("global_server_ecosystem", "Global Server Ecosystem", "internal_integration", "Canonical server ecosystem is maintained under backend.server; runtime registration is not a live provider connection.", "FOUNDATION_LINKED"),
    CatalogRecord("database_service", "Database Service", "internal_integration", "Infrastructure persistence delegates to backend.database; production database readiness is separately verified.", "FOUNDATION_LINKED"),
    CatalogRecord("ftp_healthcheck", "FTP Health Check", "internal_integration", "Read-only explicit-FTPS health-check path; no file mutation.", "READ_ONLY"),
    CatalogRecord("monitoring_probes", "Monitoring Probes", "internal_integration", "Read-only HTTP(S) endpoint probes.", "READ_ONLY"),
    CatalogRecord("storage_artifact_adapter", "Storage Artifact Adapter", "internal_integration", "Canonical backend.storage exists; no shared Global Infrastructure artifact adapter is enabled yet.", "NOT_IMPLEMENTED"),
)
