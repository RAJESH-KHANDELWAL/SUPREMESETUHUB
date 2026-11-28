"""Shared metadata contracts."""
from typing import TypedDict
class ProductContract(TypedDict, total=False):
    product_id:str; slug:str; name:str; purpose:str; domain_id:str; package_name:str; enabled:bool; implementation_mode:str
class StatusContract(TypedDict, total=False):
    provider_id:str; ecosystem_id:str; product_count:int; domain_count:int; live_connections_verified:bool; api_transport_in_core:bool
