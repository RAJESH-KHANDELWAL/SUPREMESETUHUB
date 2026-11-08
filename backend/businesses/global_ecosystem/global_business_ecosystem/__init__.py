"""Public Global Business Ecosystem package.

The domain model, controller and service remain in the established
backend.businesses modules. This package provides the canonical ecosystem
import surface without duplicating those implementations.
"""

from backend.businesses.controller import BusinessController
from backend.businesses.model import Business
from backend.businesses.service import BusinessService

__all__ = ["Business", "BusinessController", "BusinessService"]
