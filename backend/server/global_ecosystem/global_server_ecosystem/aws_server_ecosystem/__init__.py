"""Amazon Web Services provider package in GLOBAL SERVER ECOSYSTEM."""
from ..aws_server import AWSServerEcosystem

PROVIDER_ID = "aws"
DISPLAY_NAME = "Amazon Web Services"
OWNING_DOMAIN = "SERVER"

__all__ = ["AWSServerEcosystem", "PROVIDER_ID", "DISPLAY_NAME", "OWNING_DOMAIN"]
