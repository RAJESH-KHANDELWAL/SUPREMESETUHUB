"""Accessibility domain package and capability exports."""

from ..domain_registry import get_domain_profile
from .audit import audit_form_labels, audit_image_alternatives
from .catalog import list_features
from .models import AccessibilityFeature, AccessibilityNeed
from .policy import get_principles

_DOMAIN_ID = __name__.rsplit(".", 1)[-1]
DOMAIN_PROFILE = get_domain_profile(_DOMAIN_ID)


def get_profile() -> dict:
    """Return this package's detached domain profile."""
    if DOMAIN_PROFILE is None:
        raise RuntimeError(f"No registered domain profile for {_DOMAIN_ID}")
    return get_domain_profile(_DOMAIN_ID)


__all__ = [
    "DOMAIN_PROFILE",
    "AccessibilityFeature",
    "AccessibilityNeed",
    "audit_form_labels",
    "audit_image_alternatives",
    "get_principles",
    "get_profile",
    "list_features",
]
