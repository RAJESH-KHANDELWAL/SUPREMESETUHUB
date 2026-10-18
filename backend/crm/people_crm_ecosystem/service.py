"""Provider-neutral foundation for the people-facing CRM ecosystem.

This layer normalizes contact records and reports connector readiness. It does not
perform network calls or claim Google data is connected/synchronized.
"""
from __future__ import annotations

from typing import Any, Mapping

from .models import PeopleContact


class PeopleCRMEcosystem:
    NAME = "PEOPLE_CRM_ECOSYSTEM"
    PROVIDERS = ("GOOGLE_CONTACTS", "GOOGLE_SHEETS")

    def status(self) -> dict[str, Any]:
        """Report honest readiness states; provider connectivity is not implied."""
        return {
            "success": True,
            "ecosystem": self.NAME,
            "purpose": "PEOPLE_DATA_AND_RELATIONSHIP_MANAGEMENT",
            "private_owner_crm": "SEPARATE_MODULE_AND_DATA_BOUNDARY",
            "providers": {
                provider: {
                    "status": "NOT_CONNECTED",
                    "sync_enabled": False,
                    "live_api_implemented": False,
                }
                for provider in self.PROVIDERS
            },
        }

    @staticmethod
    def _first(mapping: Mapping[str, Any], key: str, value_key: str = "value") -> str:
        values = mapping.get(key) or []
        if not isinstance(values, list) or not values or not isinstance(values[0], Mapping):
            return ""
        value = values[0].get(value_key, "")
        return str(value).strip() if value is not None else ""

    def normalize_google_contact(self, record: Mapping[str, Any], contact_id: str) -> PeopleContact:
        """Normalize a Google People API-style contact resource without API access."""
        names = record.get("names") or []
        full_name = ""
        if isinstance(names, list) and names and isinstance(names[0], Mapping):
            full_name = str(names[0].get("displayName", "") or "").strip()
        if not full_name:
            full_name = str(record.get("displayName", "") or "").strip()
        external_id = ""
        metadata = record.get("metadata")
        if isinstance(metadata, Mapping):
            sources = metadata.get("sources") or []
            if isinstance(sources, list) and sources and isinstance(sources[0], Mapping):
                external_id = str(sources[0].get("id", "") or "").strip()
        contact = PeopleContact(
            contact_id=contact_id,
            full_name=full_name,
            email=self._first(record, "emailAddresses"),
            phone=self._first(record, "phoneNumbers"),
            organization=self._first(record, "organizations", "name"),
            source="GOOGLE_CONTACTS",
            external_id=external_id,
        )
        return contact.validate()

    def normalize_sheet_row(
        self, row: Mapping[str, Any], contact_id: str, column_map: Mapping[str, str] | None = None
    ) -> PeopleContact:
        """Normalize a Sheets row using explicit canonical-field-to-column mapping.

        Example: {"full_name": "Name", "email": "Email Address"}.
        The mapping is explicit to avoid guessing from arbitrary spreadsheet columns.
        """
        columns = dict(column_map or {
            "full_name": "Name",
            "email": "Email",
            "phone": "Phone",
            "organization": "Organization",
        })
        def value(field_name: str) -> str:
            raw = row.get(columns.get(field_name, ""), "")
            return str(raw).strip() if raw is not None else ""
        contact = PeopleContact(
            contact_id=contact_id,
            full_name=value("full_name"),
            email=value("email"),
            phone=value("phone"),
            organization=value("organization"),
            source="GOOGLE_SHEETS",
        )
        return contact.validate()
