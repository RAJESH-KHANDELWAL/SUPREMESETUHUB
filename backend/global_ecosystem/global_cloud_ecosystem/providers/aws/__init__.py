"""AWS provider integration boundary."""
from .adapter import AWSAdapter
from .config import AWSConfig

__all__ = ["AWSAdapter", "AWSConfig"]
