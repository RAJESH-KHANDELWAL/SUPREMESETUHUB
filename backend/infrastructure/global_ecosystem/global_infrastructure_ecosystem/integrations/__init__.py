"""Cross-layer integration declarations with explicit verification states.

FOUNDATION_LINKED means canonical packages and adapter entry points are mapped; it
does not claim provider connectivity, credentials or enabled provider operations.
"""
from ..schemas import CatalogRecord
from ..structure import INTEGRATION_PATHS

INTEGRATIONS = (
    CatalogRecord("global_infrastructure_ecosystem", "Global Infrastructure Ecosystem", "internal_integration", "Central domain adapter, catalog, ownership and governance hub.", "FOUNDATION_LINKED"),
    CatalogRecord("core_foundation", "CORE Foundation", "internal_integration", f"CORE adapter: {INTEGRATION_PATHS['core']}; canonical source: backend.core.", "FOUNDATION_LINKED"),
    CatalogRecord("global_core_ecosystem", "GLOBAL CORE ECOSYSTEM", "internal_integration", f"GLOBAL CORE adapter: {INTEGRATION_PATHS['global_core_ecosystem']}; canonical hierarchy remains under backend.core.", "FOUNDATION_LINKED"),
    CatalogRecord("global_infrastructure_core_ecosystem", "GLOBAL INFRASTRUCTURE CORE ECOSYSTEM", "internal_integration", f"Dedicated CORE validation contract: {INTEGRATION_PATHS['global_infrastructure_core_ecosystem']}.", "FOUNDATION_LINKED"),
    CatalogRecord("core_ecosystem_facade", "CORE Ecosystem Facade", "internal_integration", "Compatibility entry points remain in backend.core.global_ecosystem.", "FOUNDATION_LINKED"),
    CatalogRecord("global_ecosystem_root", "GLOBAL ECOSYSTEM", "internal_integration", "Master cross-domain and vendor ecosystem directory remains in backend.global_ecosystem.", "FOUNDATION_LINKED"),
    CatalogRecord("global_server_ecosystem", "Global Server Ecosystem", "internal_integration", "Canonical server ecosystem is maintained under backend.server; no provider connection is implied.", "FOUNDATION_LINKED"),
    CatalogRecord("database_service", "Database Service", "internal_integration", "Infrastructure persistence delegates to backend.database; production readiness is separately verified.", "FOUNDATION_LINKED"),
    CatalogRecord("storage_runtime", "Storage Runtime", "internal_integration", "Storage implementation remains canonical in backend.storage; no duplicate runtime is created.", "FOUNDATION_LINKED"),
    CatalogRecord("engine_execution_boundary", "ENGINE Execution Boundary", "internal_integration", "Executable operations remain owned by backend.engine and require explicit authorization.", "FOUNDATION_LINKED"),
    CatalogRecord("api_orchestration_boundary", "API Orchestration Boundary", "internal_integration", "HTTP orchestration remains owned by backend.api.", "FOUNDATION_LINKED"),
    CatalogRecord("hostinger_api", "Hostinger API", "provider_adapter", "Read-only inventory client exists; credentials and live connectivity must be verified.", "CATALOG_ONLY"),
    CatalogRecord("ftp_healthcheck", "FTP Health Check", "internal_integration", "Read-only explicit-FTPS health-check path; no file mutation.", "READ_ONLY"),
    CatalogRecord("monitoring_probes", "Monitoring Probes", "internal_integration", "Read-only HTTP(S) endpoint probes.", "READ_ONLY"),
)
