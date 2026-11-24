"""Canonical infrastructure controller owned by the Global Infrastructure Ecosystem."""
from typing import Optional
from uuid import uuid4
from backend.infrastructure.model import InfrastructureCategory, InfrastructureResource, InfrastructureResourceStatus, InfrastructureResourceType
from .service import InfrastructureService

class InfrastructureController:
    def __init__(self, service: Optional[InfrastructureService] = None):
        self.service = service or InfrastructureService()

    @staticmethod
    def _resource_type(value: str) -> InfrastructureResourceType:
        aliases = {"server":"dedicated_server","cloud":"cloud_server","vm":"virtual_machine","ip":"ip_address"}
        normalized = aliases.get(value.strip().lower(), value.strip().lower())
        try:
            return InfrastructureResourceType(normalized)
        except ValueError as exc:
            raise ValueError(f"Unsupported infrastructure type: {value}") from exc

    @staticmethod
    def _category(resource_type: InfrastructureResourceType) -> InfrastructureCategory:
        mapping = {
            InfrastructureResourceType.DEDICATED_SERVER: InfrastructureCategory.SERVER,
            InfrastructureResourceType.VPS: InfrastructureCategory.SERVER,
            InfrastructureResourceType.CLOUD_SERVER: InfrastructureCategory.SERVER,
            InfrastructureResourceType.VIRTUAL_MACHINE: InfrastructureCategory.SERVER,
            InfrastructureResourceType.VPN: InfrastructureCategory.NETWORK,
            InfrastructureResourceType.NETWORK: InfrastructureCategory.NETWORK,
            InfrastructureResourceType.IP_ADDRESS: InfrastructureCategory.NETWORK,
            InfrastructureResourceType.DNS: InfrastructureCategory.NETWORK,
            InfrastructureResourceType.STORAGE: InfrastructureCategory.STORAGE,
            InfrastructureResourceType.OBJECT_STORAGE: InfrastructureCategory.STORAGE,
            InfrastructureResourceType.DATABASE: InfrastructureCategory.DATABASE,
            InfrastructureResourceType.DATABASE_SERVER: InfrastructureCategory.DATABASE,
            InfrastructureResourceType.HOSTING: InfrastructureCategory.HOSTING,
            InfrastructureResourceType.HOSTING_PLAN: InfrastructureCategory.HOSTING,
            InfrastructureResourceType.DOMAIN: InfrastructureCategory.DOMAIN,
            InfrastructureResourceType.WEBSITE: InfrastructureCategory.WEBSITE,
            InfrastructureResourceType.WORDPRESS: InfrastructureCategory.WEBSITE,
            InfrastructureResourceType.APPLICATION: InfrastructureCategory.APPLICATION,
            InfrastructureResourceType.CONTAINER: InfrastructureCategory.APPLICATION,
            InfrastructureResourceType.FIREWALL: InfrastructureCategory.SECURITY,
            InfrastructureResourceType.CDN: InfrastructureCategory.DELIVERY,
            InfrastructureResourceType.LOAD_BALANCER: InfrastructureCategory.DELIVERY,
            InfrastructureResourceType.BACKUP: InfrastructureCategory.BACKUP,
            InfrastructureResourceType.OTHER: InfrastructureCategory.OTHER,
        }
        return mapping[resource_type]

    def create(self, name: str, infrastructure_type: str, provider: str = "", region: str = "",
               public_ipv4: str = "", public_ipv6: str = "", description: str = "") -> dict:
        resource_type = self._resource_type(infrastructure_type)
        metadata = {}
        if public_ipv4: metadata["public_ipv4"] = public_ipv4
        if public_ipv6: metadata["public_ipv6"] = public_ipv6
        item = InfrastructureResource(
            resource_id=str(uuid4()), name=name, resource_type=resource_type,
            category=self._category(resource_type), status=InfrastructureResourceStatus.ACTIVE,
            provider=provider or None, region=region or None, description=description or None, metadata=metadata)
        return self.service.register_resource(item).to_dict()

    def get(self, infrastructure_id: str) -> Optional[dict]:
        item = self.service.get_resource(infrastructure_id)
        return item.to_dict() if item else None

    def list(self) -> list[dict]:
        return [item.to_dict() for item in self.service.list_resources()]

    def update_status(self, infrastructure_id: str, status: str) -> Optional[dict]:
        try:
            normalized = InfrastructureResourceStatus(status.strip().lower())
        except (AttributeError, ValueError) as exc:
            raise ValueError(f"Unsupported infrastructure status: {status}") from exc
        item = self.service.set_status(infrastructure_id, normalized)
        return item.to_dict() if item else None

    def delete(self, infrastructure_id: str) -> bool:
        return self.service.delete_resource(infrastructure_id)

__all__ = ["InfrastructureController"]
