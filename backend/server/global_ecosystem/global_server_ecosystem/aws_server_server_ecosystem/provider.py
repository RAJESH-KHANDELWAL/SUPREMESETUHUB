"""Amazon Web Services provider adapter binding for GLOBAL SERVER.

This namespace mirrors sibling layer package naming and reuses the
existing provider adapter. It does not claim live connectivity.
"""
from ..aws_server_ecosystem import AWSServerEcosystem

PROVIDER_ID = "aws"
DISPLAY_NAME = "Amazon Web Services"
OWNING_DOMAIN = "SERVER"
ADAPTER_CLASS = AWSServerEcosystem

__all__ = ["PROVIDER_ID", "DISPLAY_NAME", "OWNING_DOMAIN", "ADAPTER_CLASS"]
