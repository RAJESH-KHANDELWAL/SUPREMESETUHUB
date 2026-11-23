"""Global Hosting Core public interface."""
from .catalog import ROOT_ID,get_catalog,get_provider,list_providers
from .manager import GlobalHostingCoreManager,get_manager
from .models import HostingProviderRecord
from .contracts import CoreResult,Readiness,SecretReference,TenantContext
from .module_service import HostingProviderCoreService
__all__=["ROOT_ID","get_catalog","get_provider","list_providers","GlobalHostingCoreManager","get_manager","HostingProviderRecord","CoreResult","Readiness","SecretReference","TenantContext","HostingProviderCoreService"]
