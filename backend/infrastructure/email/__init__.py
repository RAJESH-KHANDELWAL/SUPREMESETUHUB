"""Email infrastructure for MAIN BASE FOUNDATION."""

from .model import (
    EmailAccountInfo,
    EmailServiceInfo,
)
from .service import EmailService
from .controller import EmailController

__all__ = [
    "EmailAccountInfo",
    "EmailServiceInfo",
    "EmailService",
    "EmailController",
]
