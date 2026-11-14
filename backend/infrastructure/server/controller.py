"""
MAIN BASE FOUNDATION
Infrastructure - Server Controller

Control-plane facade for server management, including the canonical SERVER
domain integration. Legacy infrastructure inventory methods remain intact.
"""

from typing import Any, Dict, List, Optional

from .service import ServerService
from .domain_integration import ServerDomainIntegration


class ServerController:
    """Controller for infrastructure inventory and SERVER domain operations."""

    def __init__(self, service=None, domain_integration=None):
        self.service = service or ServerService()
        self.domain = domain_integration or ServerDomainIntegration()

    def create(self, server_type: str, name: Optional[str] = None,
               provider: Optional[str] = None, location: Optional[str] = None,
               region: Optional[str] = None, datacenter: Optional[str] = None,
               ip_address_id: Optional[str] = None, operating_system: Optional[str] = None,
               control_panel: Optional[str] = None, cpu_cores: Optional[int] = None,
               memory_gb: Optional[float] = None, storage_gb: Optional[float] = None,
               bandwidth_gb: Optional[float] = None, virtualization: Optional[str] = None,
               root_access: bool = False, metadata: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        return self.service.create_server(
            server_type=server_type, name=name, provider=provider, location=location,
            region=region, datacenter=datacenter, ip_address_id=ip_address_id,
            operating_system=operating_system, control_panel=control_panel,
            cpu_cores=cpu_cores, memory_gb=memory_gb, storage_gb=storage_gb,
            bandwidth_gb=bandwidth_gb, virtualization=virtualization,
            root_access=root_access, metadata=metadata,
        )

    def get(self, server_id: str) -> Optional[Dict[str, Any]]:
        return self.service.get_server(server_id)

    def list(self) -> List[Dict[str, Any]]:
        return self.service.list_servers()

    def list_by_type(self, server_type: str) -> List[Dict[str, Any]]:
        return self.service.list_by_type(server_type)

    def update(self, server_id: str, **fields: Any) -> Optional[Dict[str, Any]]:
        return self.service.update_server(server_id, **fields)

    def delete(self, server_id: str) -> bool:
        return self.service.delete_server(server_id)

    def exists(self, server_id: str) -> bool:
        return self.service.exists(server_id)

    def attach_ip(self, server_id: str, ip_address_id: str) -> Optional[Dict[str, Any]]:
        return self.service.attach_ip(server_id, ip_address_id)

    def set_active(self, server_id: str) -> Optional[Dict[str, Any]]:
        return self.service.set_active(server_id)

    def set_maintenance(self, server_id: str) -> Optional[Dict[str, Any]]:
        return self.service.set_maintenance(server_id)

    def suspend(self, server_id: str) -> Optional[Dict[str, Any]]:
        return self.service.suspend(server_id)

    # Canonical backend.server domain: distinct from the legacy SQL inventory above.
    def domain_status(self):
        return self.domain.health()

    def domain_describe(self):
        return self.domain.describe()

    def register_domain_server(self, **kwargs):
        return self.domain.register(**kwargs)

    def get_domain_server(self, server_id):
        return self.domain.get(server_id)

    def list_domain_servers(self):
        return self.domain.list()

    def update_domain_server(self, server_id, **changes):
        return self.domain.update(server_id, **changes)

    def delete_domain_server(self, server_id):
        return self.domain.delete(server_id)

    def start_domain_server(self, server_id):
        return self.domain.start(server_id)

    def stop_domain_server(self, server_id):
        return self.domain.stop(server_id)

    def restart_domain_server(self, server_id):
        return self.domain.restart(server_id)

    def register_domain_provider(self, provider_id, adapter, *, replace=False):
        return self.domain.register_provider(provider_id, adapter, replace=replace)

    def describe_domain_provider(self, provider_id):
        return self.domain.describe_provider(provider_id)

    def domain_provider_health(self, provider_id):
        return self.domain.provider_health(provider_id)

    def execute_domain_provider_operation(self, provider_id, operation, payload=None):
        return self.domain.execute_provider_operation(provider_id, operation, payload)

    def register_domain_operation_adapter(self, capability, adapter, *, replace=False):
        return self.domain.register_operation_adapter(capability, adapter, replace=replace)

    def execute_domain_operation(self, capability, operation, payload=None):
        return self.domain.execute_operation(capability, operation, payload)
