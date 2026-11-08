"""Amazon Web Services provider adapter binding for GLOBAL SERVER.

This namespace follows the provider/layer package convention used by
API, CORE, ENGINE and DATABASE. It reuses the existing SERVER adapter and
does not claim a live connection or provider-specific service capability.
"""
from ..aws_server import AWSServerEcosystem

PROVIDER_ID = "aws"
DISPLAY_NAME = "Amazon Web Services"
OWNING_DOMAIN = "SERVER"
ADAPTER_CLASS = AWSServerEcosystem

__all__ = ["PROVIDER_ID", "DISPLAY_NAME", "OWNING_DOMAIN", "ADAPTER_CLASS"]
