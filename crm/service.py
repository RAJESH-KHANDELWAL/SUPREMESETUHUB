"""CRM workflows: scoped records, duplicate hints, categories, follow-ups and drafts."""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Mapping

from .contact_service import ContactService
from .models import Contact
from .repository import CRMRepository
from .quality import assess_contact_quality


class CRMService:
    def __init__(self, repository: CRMRepository | None = None) -> None:
        self.repository = repository or CRMRepository()
        self.normalizer = ContactService()

    @staticmethod
    def _as_contact(record: Mapping[str, Any]) -> Contact:
        return Contact(
            contact_id=str(record["contact_id"]),
            full_name=str(record["full_name"]),
            email=str(record.get("email") or ""),
            phone=str(record.get("phone") or ""),
            whatsapp_phone=str(record.get("whatsapp_phone") or ""),
            organization=str(record.get("organization") or ""),
            address=str(record.get("address") or ""),
            city=str(record.get("city") or ""),
            pincode=str(record.get("pincode") or ""),
            designation=str(record.get("designation") or ""),
            verification_status=str(record.get("verification_status") or "UNVERIFIED"),
            source=str(record.get("source") or "MANUAL"),
            external_id=str(record.get("external_id") or ""),
            notes=str(record.get("notes") or ""),
            tags=tuple(record.get("tags") or ()),
            consent_to_contact=bool(record.get("consent_to_contact", False)),
            contact_status=str(record.get("contact_status") or "ACTIVE"),
            category=str(record.get("category") or "UNCATEGORIZED"),
            follow_up_at=record.get("follow_up_at"),
        )

    def create_contact(self, owner: str, actor: str, data: dict[str, Any]) -> dict[str, Any]:
        contact = Contact(
            contact_id="pending", full_name=data["full_name"].strip(),
            email=(data.get("email") or "").strip(),
            phone=(data.get("phone") or "").strip(),
            whatsapp_phone=(data.get("whatsapp_phone") or "").strip(),
            organization=(data.get("organization") or "").strip(),
            address=(data.get("address") or "").strip(),
            city=(data.get("city") or "").strip(),
            pincode=(data.get("pincode") or "").strip(),
            designation=(data.get("designation") or "").strip(),
            verification_status=data.get("verification_status", "UNVERIFIED"),
            source=data.get("source", "MANUAL"),
            external_id=data.get("external_id", ""),
            notes=data.get("notes", ""),
            tags=tuple(data.get("tags") or ()),
            consent_to_contact=bool(data.get("consent_to_contact", False)),
            contact_status=data.get("contact_status", "ACTIVE"),
            category=data.get("category", "UNCATEGORIZED"),
            follow_up_at=data.get("follow_up_at"),
        )
        contact.validate()
        saved = self.repository.create_contact(owner, contact.to_dict())
        self.repository.log_event(owner, actor, "CONTACT_CREATED", saved["contact_id"], {"source": saved["source"]})
        return saved

    def list_contacts(self, owner: str, **filters: Any) -> list[dict[str, Any]]:
        return self.repository.list_contacts(owner, **filters)

    def get_contact(self, owner: str, contact_id: str) -> dict[str, Any] | None:
        return self.repository.get_contact(owner, contact_id)

    def update_contact(self, owner: str, actor: str, contact_id: str, changes: dict[str, Any]) -> dict[str, Any] | None:
        existing = self.repository.get_contact(owner, contact_id)
        if existing is None:
            return None
        changes = {key: value for key, value in changes.items() if value is not None or key == "follow_up_at"}
        if "full_name" in changes and changes["full_name"] is not None:
            changes["full_name"] = changes["full_name"].strip()
        merged = dict(existing)
        merged.update({k: v for k, v in changes.items() if v is not None})
        self._as_contact(merged).validate()
        updated = self.repository.update_contact(owner, contact_id, changes)
        if updated is not None:
            self.repository.log_event(owner, actor, "CONTACT_UPDATED", contact_id, {"fields": sorted(changes)})
        return updated

    def delete_contact(self, owner: str, actor: str, contact_id: str) -> bool:
        existing = self.repository.get_contact(owner, contact_id)
        if existing is None:
            return False
        deleted = self.repository.delete_contact(owner, contact_id)
        if deleted:
            self.repository.log_event(owner, actor, "CONTACT_DELETED", contact_id, {"name": existing["full_name"]})
        return deleted

    def duplicate_candidates(self, owner: str) -> list[dict[str, Any]]:
        records = self.repository.list_contacts(owner, limit=500)
        candidates = []
        for i, left in enumerate(records):
            left_email = (left.get("email") or "").strip().casefold()
            left_phone = "".join(ch for ch in (left.get("phone") or "") if ch.isdigit())
            if not left_email and not left_phone:
                continue
            for right in records[i + 1:]:
                same_email = bool(left_email and left_email == (right.get("email") or "").strip().casefold())
                right_phone = "".join(ch for ch in (right.get("phone") or "") if ch.isdigit())
                same_phone = bool(left_phone and len(left_phone) >= 7 and left_phone == right_phone)
                if same_email or same_phone:
                    candidates.append({
                        "contact_ids": [left["contact_id"], right["contact_id"]],
                        "match_reason": "EMAIL_AND_PHONE" if same_email and same_phone else ("EMAIL" if same_email else "PHONE"),
                        "records": [
                            {"contact_id": left["contact_id"], "full_name": left["full_name"], "email": left.get("email", ""), "phone": left.get("phone", "")},
                            {"contact_id": right["contact_id"], "full_name": right["full_name"], "email": right.get("email", ""), "phone": right.get("phone", "")},
                        ],
                        "auto_merged": False,
                        "human_review_required": True,
                    })
        return candidates

    @staticmethod
    def suggest_category(record: Mapping[str, Any]) -> dict[str, Any]:
        text = " ".join([
            str(record.get("organization") or ""),
            str(record.get("notes") or ""),
            " ".join(str(tag) for tag in (record.get("tags") or [])),
        ]).casefold()
        rules = (
            ("CUSTOMER", ("customer", "client", "buyer")),
            ("LEAD", ("lead", "prospect", "inquiry", "enquiry")),
            ("PARTNER", ("partner", "affiliate", "collaborator")),
            ("SUPPLIER", ("supplier", "vendor", "provider")),
        )
        category = next((label for label, words in rules if any(word in text for word in words)), "UNCATEGORIZED")
        return {"contact_id": record["contact_id"], "current_category": record.get("category", "UNCATEGORIZED"),
                "suggested_category": category, "method": "TRANSPARENT_RULES",
                "requires_human_approval": True, "applied": False}

    def category_suggestions(self, owner: str) -> list[dict[str, Any]]:
        return [self.suggest_category(record) for record in self.repository.list_contacts(owner, limit=500)]

    @staticmethod
    def suggest_follow_up(record: Mapping[str, Any], now: datetime | None = None) -> dict[str, Any]:
        now = now or datetime.now(timezone.utc)
        raw = record.get("follow_up_at")
        overdue = False
        if raw:
            try:
                parsed = datetime.fromisoformat(str(raw).replace("Z", "+00:00"))
                if parsed.tzinfo is None:
                    parsed = parsed.replace(tzinfo=timezone.utc)
                overdue = parsed < now
            except ValueError:
                pass
        if record.get("contact_status") == "DO_NOT_CONTACT":
            action = "NO_CONTACT"
        elif not record.get("consent_to_contact"):
            action = "CHECK_CONSENT_BEFORE_OUTREACH"
        elif overdue:
            action = "REVIEW_OVERDUE_FOLLOW_UP"
        elif not raw:
            action = "HUMAN_DECIDE_IF_FOLLOW_UP_NEEDED"
        else:
            action = "FOLLOW_UP_SCHEDULED"
        return {"contact_id": record["contact_id"], "full_name": record["full_name"],
                "follow_up_at": raw, "overdue": overdue, "suggested_action": action,
                "automatic_message_sent": False}

    def follow_up_suggestions(self, owner: str) -> list[dict[str, Any]]:
        return [self.suggest_follow_up(record) for record in self.repository.list_contacts(owner, limit=500)
                if record.get("contact_status") != "ARCHIVED"]

    def draft_message(self, owner: str, contact_id: str, purpose: str, tone: str = "friendly") -> dict[str, Any] | None:
        record = self.repository.get_contact(owner, contact_id)
        if record is None:
            return None
        if record.get("contact_status") == "DO_NOT_CONTACT" or not record.get("consent_to_contact"):
            raise PermissionError("EXPLICIT_CONTACT_CONSENT_REQUIRED")
        purpose = purpose.strip()[:500]
        if not purpose:
            raise ValueError("purpose is required")
        greeting = f"Hi {record['full_name'].strip()},"
        if tone.casefold() == "formal":
            greeting = f"Hello {record['full_name'].strip()},"
        body = f"{greeting}\n\nI wanted to follow up regarding {purpose}. If this is relevant to you, please let me know what would be most helpful.\n\nBest regards"
        return {"contact_id": contact_id, "purpose": purpose, "tone": tone,
                "draft": body, "sent": False, "human_approval_required": True}

    def preview_import(
        self, owner: str, provider: str, records: list[dict[str, Any]],
        column_map: Mapping[str, str] | None = None,
    ) -> dict[str, Any]:
        provider = provider.strip().upper()
        if provider not in {"GOOGLE_SHEETS", "GOOGLE_CONTACTS"}:
            raise ValueError("Unsupported CRM import provider")
        if len(records) > 500:
            raise ValueError("A CRM import may contain at most 500 records")
        existing = self.repository.list_contacts(owner, limit=500)
        seen_emails = {(str(item.get("email") or "").strip().casefold(), item["contact_id"]) for item in existing if item.get("email")}
        seen_phones = {("".join(ch for ch in str(item.get("phone") or "") if ch.isdigit()), item["contact_id"]) for item in existing if item.get("phone")}
        incoming_emails: dict[str, int] = {}
        incoming_phones: dict[str, int] = {}
        items = []
        for index, raw in enumerate(records, start=1):
            try:
                if provider == "GOOGLE_SHEETS":
                    contact = self.normalizer.normalize_sheet_row(raw, f"PREVIEW-{index}", column_map)
                else:
                    contact = self.normalizer.normalize_google_contact(raw, f"PREVIEW-{index}")
                normalized = contact.to_dict()
                email = contact.email.strip().casefold()
                phone = "".join(ch for ch in contact.phone if ch.isdigit())
                reasons = []
                if email and any(value == email for value, _contact_id in seen_emails):
                    reasons.append("EXISTING_EMAIL")
                if phone and len(phone) >= 7 and any(value == phone for value, _contact_id in seen_phones):
                    reasons.append("EXISTING_PHONE")
                if email and email in incoming_emails:
                    reasons.append("DUPLICATE_EMAIL_IN_IMPORT")
                if phone and len(phone) >= 7 and phone in incoming_phones:
                    reasons.append("DUPLICATE_PHONE_IN_IMPORT")
                if email:
                    incoming_emails[email] = index
                if phone and len(phone) >= 7:
                    incoming_phones[phone] = index
                items.append({
                    "row_number": index, "status": "DUPLICATE_REVIEW" if reasons else "READY",
                    "duplicate_reasons": reasons, "contact": normalized,
                    "human_review_required": bool(reasons),
                })
            except (ValueError, TypeError, AttributeError) as exc:
                items.append({"row_number": index, "status": "INVALID", "error": str(exc)})
        return {
            "provider": provider, "status": "PREVIEW_ONLY", "records_received": len(records),
            "ready_count": sum(item["status"] == "READY" for item in items),
            "duplicate_review_count": sum(item["status"] == "DUPLICATE_REVIEW" for item in items),
            "invalid_count": sum(item["status"] == "INVALID" for item in items),
            "records_written": 0, "data": items,
            "human_approval_required": True, "no_data_written": True,
        }

    def commit_import(
        self, owner: str, actor: str, provider: str, records: list[dict[str, Any]],
        column_map: Mapping[str, str] | None = None, confirm_import: bool = False,
    ) -> dict[str, Any]:
        if not confirm_import:
            raise PermissionError("HUMAN_IMPORT_CONFIRMATION_REQUIRED")
        preview = self.preview_import(owner, provider, records, column_map)
        if preview["invalid_count"]:
            raise ValueError("Import contains invalid rows; fix them and preview again")
        if preview["duplicate_review_count"]:
            raise ValueError("Import contains duplicate candidates; resolve them before committing")
        created = []
        for item in preview["data"]:
            normalized = dict(item["contact"])
            normalized.pop("contact_id", None)
            normalized["source"] = provider
            created.append(self.create_contact(owner, actor, normalized))
        self.repository.log_event(owner, actor, "CRM_IMPORT_COMMITTED", None, {
            "provider": provider, "records_imported": len(created),
        })
        return {"success": True, "provider": provider, "records_imported": len(created), "data": created}

    def assess_contact(self, owner: str, contact_id: str) -> dict[str, Any] | None:
        record = self.repository.get_contact(owner, contact_id)
        if record is None:
            return None
        return {"contact_id": contact_id, "full_name": record["full_name"],
                **assess_contact_quality(record)}

    def quality_review_queue(self, owner: str, limit: int = 200) -> dict[str, Any]:
        records = self.repository.list_contacts(owner, limit=limit)
        assessed = [{"contact_id": item["contact_id"], "full_name": item["full_name"],
                     "phone": item.get("phone", ""), "email": item.get("email", ""),
                     **assess_contact_quality(item)} for item in records]
        flagged = [item for item in assessed if item["quality_label"] in {"REVIEW_REQUIRED", "INCOMPLETE"}]
        return {"success": True, "method": "RULE_BASED_FORMAT_AND_COMPLETENESS_CHECK",
                "scanned_count": len(assessed), "flagged_count": len(flagged),
                "unverified_count": sum(item["verification_status"] != "VERIFIED" for item in assessed),
                "data": flagged, "note": "Valid formats do not prove a real person owns the contact details."}

    def create_daily_item(self, owner: str, actor: str, data: dict[str, Any]) -> dict[str, Any]:
        if data.get("contact_id") and self.repository.get_contact(owner, data["contact_id"]) is None:
            raise ValueError("CRM_CONTACT_NOT_FOUND")
        title = str(data.get("title") or "").strip()
        if not title:
            raise ValueError("title is required")
        return self.repository.create_daily_item(owner, actor, {**data, "title": title[:200]})

    def update_daily_item(self, owner: str, actor: str, item_id: str, status: str) -> dict[str, Any] | None:
        return self.repository.update_daily_item(owner, actor, item_id, status)

    def daily_briefing(self, owner: str) -> dict[str, Any]:
        items = self.repository.list_daily_items(owner, limit=200)
        return {"success": True, "generated_by": "CRM_RULES_ENGINE",
                "external_ai_connected": False,
                "summary": {"open": sum(item["status"] == "OPEN" for item in items),
                            "in_progress": sum(item["status"] == "IN_PROGRESS" for item in items),
                            "done": sum(item["status"] == "DONE" for item in items)},
                "items": items, "suggested_routine": [
                    {"period": "MORNING", "action": "Review today's due tasks, overdue follow-ups and flagged contacts"},
                    {"period": "WORKDAY", "action": "Log calls, meetings, notes and agreed next steps"},
                    {"period": "EVENING", "action": "Mark completed work and schedule tomorrow's follow-ups"},
                ]}

    def report(self, owner: str) -> dict[str, Any]:
        return {"success": True, "report": self.repository.counts(owner),
                "duplicate_candidate_pairs": len(self.duplicate_candidates(owner)),
                "category_suggestions_pending": sum(
                    1 for item in self.category_suggestions(owner)
                    if item["suggested_category"] != item["current_category"]
                ),
                "generated_by": "CRM_RULES_ENGINE", "external_ai_connected": False}
