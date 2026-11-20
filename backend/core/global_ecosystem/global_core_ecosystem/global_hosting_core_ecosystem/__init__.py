"""Global Hosting Core Ecosystem public interface."""
from .catalog import ROOT_ID,get_catalog,get_provider,list_providers
from .manager import GlobalHostingCoreManager,get_manager
from .models import HostingProviderRecord
from .registry import HostingProviderRegistry
__all__=["ROOT_ID","get_catalog","get_provider","list_providers","GlobalHostingCoreManager","get_manager","HostingProviderRecord","HostingProviderRegistry"]
