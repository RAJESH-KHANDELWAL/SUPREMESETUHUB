"""SUPREME ECOSYSTEM package and public connector interface."""
from .brand_identity import DR_RAJESH_KHANDELWAL_IBC_BRAND, DR_RAJESH_KHANDELWAL_IBC_OFFICIAL_BRAND
from .supreme_ecosystem import ACCESS_POLICY, CORE_MODULES, PARENT_SYSTEM, SYSTEM_NAME, SupremeEcosystem, supreme_ecosystem
from .connectors.base import ConnectorResult, ConnectorCapability, EcosystemProviderConnector
from .connectors.registry import ConnectorRegistry, registry
from .connectors.manager import ConnectorManager, connector_manager
from .supreme_business_ecosystem import status as supreme_business_ecosystem_status
from .supreme_ai_ecosystem import status as supreme_ai_ecosystem_status
__all__=["ACCESS_POLICY","CORE_MODULES","PARENT_SYSTEM","SYSTEM_NAME","SupremeEcosystem","supreme_ecosystem",
"ConnectorResult","ConnectorCapability","EcosystemProviderConnector","ConnectorRegistry","registry","ConnectorManager",
"connector_manager","supreme_business_ecosystem_status","supreme_ai_ecosystem_status",
"DR_RAJESH_KHANDELWAL_IBC_BRAND","DR_RAJESH_KHANDELWAL_IBC_OFFICIAL_BRAND"]
