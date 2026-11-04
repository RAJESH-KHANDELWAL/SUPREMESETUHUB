"""Provider-neutral contact normalization for the CRM module."""
from __future__ import annotations

from typing import Any, Mapping

from .models import Contact


class ContactService:
    """Normalize imported contacts without performing external API calls."""

    @staticmethod
    def _first(mapping: Mapping[str, Any], key: str, value_key: str = "value") -> str:
        values = mapping.get(key) or []
        if not isinstance(values, list) or not values or not isinstance(values[0], Mapping):
            return ""
        value = values[0].get(value_key, "")
        return str(value).strip() if value is not None else ""

    def normalize_google_contact(self, record: Mapping[str, Any], contact_id: str) -> Contact:
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
        return Contact(
            contact_id=contact_id,
            full_name=full_name,
            email=self._first(record, "emailAddresses"),
            phone=self._first(record, "phoneNumbers"),
            organization=self._first(record, "organizations", "name"),
            source="GOOGLE_CONTACTS",
            external_id=external_id,
        ).validate()

    def normalize_sheet_row(
        self, row: Mapping[str, Any], contact_id: str,
        column_map: Mapping[str, str] | None = None,
    ) -> Contact:
        columns = dict(column_map or {
            "full_name": "Name", "email": "Email", "phone": "Mobile",
            "whatsapp_phone": "WhatsApp", "organization": "Company",
            "address": "Address", "city": "City", "pincode": "Pincode",
            "designation": "Designation",
        })

        def value(field_name: str) -> str:
            raw = row.get(columns.get(field_name, ""), "")
            return str(raw).strip() if raw is not None else ""

        return Contact(
            contact_id=contact_id,
            full_name=value("full_name"),
            email=value("email"),
            phone=value("phone"),
            whatsapp_phone=value("whatsapp_phone"),
            organization=value("organization"),
            address=value("address"),
            city=value("city"),
            pincode=value("pincode"),
            designation=value("designation"),
            source="GOOGLE_SHEETS",
        ).validate()
