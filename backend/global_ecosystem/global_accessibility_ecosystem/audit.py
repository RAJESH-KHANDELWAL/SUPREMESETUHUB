"""Small, dependency-free checks for common web accessibility issues."""

from collections.abc import Mapping
from typing import Any


def audit_image_alternatives(images: list[Mapping[str, Any]]) -> list[dict[str, str]]:
    """Report images with missing alternative text.

    Each image mapping may contain: id, decorative, and alt.
    Decorative images should use an empty alt string.
    """
    findings: list[dict[str, str]] = []
    for index, image in enumerate(images):
        image_id = str(image.get("id", index))
        alt = image.get("alt")
        decorative = bool(image.get("decorative", False))
        if decorative:
            if alt != "":
                findings.append({
                    "id": image_id,
                    "severity": "warning",
                    "message": "Decorative images should have empty alternative text.",
                })
        elif not isinstance(alt, str) or not alt.strip():
            findings.append({
                "id": image_id,
                "severity": "error",
                "message": "Informative images need meaningful alternative text.",
            })
    return findings


def audit_form_labels(controls: list[Mapping[str, Any]]) -> list[dict[str, str]]:
    """Report form controls without an accessible name."""
    findings: list[dict[str, str]] = []
    for index, control in enumerate(controls):
        name = control.get("accessible_name")
        if not isinstance(name, str) or not name.strip():
            findings.append({
                "id": str(control.get("id", index)),
                "severity": "error",
                "message": "Form control is missing an accessible name.",
            })
    return findings
