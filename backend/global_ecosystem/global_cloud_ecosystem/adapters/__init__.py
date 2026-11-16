"""Provider-neutral cloud adapter protocol."""
from typing import Any,Protocol,runtime_checkable
from collections.abc import Mapping
@runtime_checkable
class CloudProviderAdapter(Protocol):
    provider:Mapping[str,Any]
    @property
    def configured(self)->bool:...
    def execute(self,operation:str,payload:Mapping[str,Any]|None=None)->Any:...
__all__=["CloudProviderAdapter"]
