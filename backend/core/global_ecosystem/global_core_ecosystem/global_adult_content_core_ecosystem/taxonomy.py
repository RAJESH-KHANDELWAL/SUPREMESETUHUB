"""Canonical orientation and scene descriptors."""

from __future__ import annotations

from .contracts import Orientation, ParticipantConfiguration

ORIENTATION_CATALOG = (
    {
        "id": "STRAIGHT",
        "label": "Straight",
        "definition": "Heterosexual orientation label.",
        "assignment_rule": "SELF_DECLARED_OR_AUTHORISED_SOURCE_ONLY",
    },
    {
        "id": "GAY",
        "label": "Gay",
        "definition": "Homosexual orientation label.",
        "assignment_rule": "SELF_DECLARED_OR_AUTHORISED_SOURCE_ONLY",
    },
    {
        "id": "BISEXUAL",
        "label": "Bisexual",
        "definition": "Orientation involving attraction to more than one gender.",
        "assignment_rule": "SELF_DECLARED_OR_AUTHORISED_SOURCE_ONLY",
    },
    {
        "id": "OTHER",
        "label": "Other",
        "definition": "A voluntary, self-described orientation not represented above.",
        "assignment_rule": "SELF_DECLARED_OR_AUTHORISED_SOURCE_ONLY",
    },
    {
        "id": "UNSPECIFIED",
        "label": "Unspecified",
        "definition": "No orientation label supplied.",
        "assignment_rule": "DEFAULT_NO_INFERENCE",
    },
)

PARTICIPANT_CONFIGURATION_CATALOG = tuple(
    {"id": item.value, "label": item.value.replace("_", " ").title()}
    for item in ParticipantConfiguration
)


def get_orientation(value: str) -> dict[str, str] | None:
    key = str(value).strip().upper()
    return next((dict(item) for item in ORIENTATION_CATALOG if item["id"] == key), None)
