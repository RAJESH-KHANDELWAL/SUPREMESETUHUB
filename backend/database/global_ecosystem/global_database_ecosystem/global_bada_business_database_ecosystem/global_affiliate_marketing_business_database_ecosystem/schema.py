"""SQLite schema for the GLOBAL BADA BUSINESS affiliate-marketing domain.

This schema owns persistence only. Business rules remain in CORE and provider
execution remains in ENGINE.
"""
from __future__ import annotations

SCHEMA_VERSION = "2026_01"
PROGRAMS_TABLE = "global_affiliate_programs"
REFERRALS_TABLE = "global_affiliate_referrals"
EVENTS_TABLE = "global_affiliate_events"


def schema_statements() -> tuple[str, ...]:
    """Return idempotent DDL statements; existing data is never dropped."""
    return (
        f"""CREATE TABLE IF NOT EXISTS {PROGRAMS_TABLE} (
            program_id TEXT PRIMARY KEY,
            platform_id TEXT NOT NULL,
            program_name TEXT NOT NULL,
            region TEXT NOT NULL DEFAULT 'GLOBAL',
            commission_type TEXT NOT NULL DEFAULT 'UNSPECIFIED'
                CHECK (commission_type IN ('PERCENTAGE','FIXED','UNSPECIFIED')),
            commission_rate REAL NOT NULL DEFAULT 0 CHECK (commission_rate >= 0),
            currency TEXT NOT NULL DEFAULT 'USD'
                CHECK (length(currency) = 3),
            terms_url TEXT,
            verification_status TEXT NOT NULL DEFAULT 'UNVERIFIED'
                CHECK (verification_status IN ('UNVERIFIED','PENDING','VERIFIED','REJECTED')),
            program_status TEXT NOT NULL DEFAULT 'PENDING_VERIFICATION'
                CHECK (program_status IN ('PENDING_VERIFICATION','ACTIVE','PAUSED','ARCHIVED')),
            metadata_json TEXT NOT NULL DEFAULT '{{}}',
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        )""",
        f"""CREATE TABLE IF NOT EXISTS {REFERRALS_TABLE} (
            referral_id TEXT PRIMARY KEY,
            owner_user_id TEXT NOT NULL,
            program_id TEXT NOT NULL REFERENCES {PROGRAMS_TABLE}(program_id),
            referral_code TEXT NOT NULL,
            destination_url TEXT NOT NULL,
            disclosure_text TEXT NOT NULL,
            referral_status TEXT NOT NULL DEFAULT 'ACTIVE'
                CHECK (referral_status IN ('ACTIVE','PAUSED','REVOKED')),
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(owner_user_id, program_id, referral_code)
        )""",
        f"""CREATE TABLE IF NOT EXISTS {EVENTS_TABLE} (
            event_id TEXT PRIMARY KEY,
            referral_id TEXT NOT NULL REFERENCES {REFERRALS_TABLE}(referral_id),
            source_event_id TEXT NOT NULL,
            event_type TEXT NOT NULL
                CHECK (event_type IN ('CLICK','LEAD','CONVERSION')),
            amount_minor INTEGER NOT NULL DEFAULT 0 CHECK (amount_minor >= 0),
            commission_minor INTEGER NOT NULL DEFAULT 0 CHECK (commission_minor >= 0),
            currency TEXT NOT NULL CHECK (length(currency) = 3),
            event_status TEXT NOT NULL DEFAULT 'PENDING'
                CHECK (event_status IN ('PENDING','APPROVED','REJECTED','PAID')),
            occurred_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            metadata_json TEXT NOT NULL DEFAULT '{{}}',
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(referral_id, source_event_id)
        )""",
        f"CREATE INDEX IF NOT EXISTS idx_global_affiliate_referrals_owner ON {REFERRALS_TABLE}(owner_user_id, created_at)",
        f"CREATE INDEX IF NOT EXISTS idx_global_affiliate_events_referral ON {EVENTS_TABLE}(referral_id, occurred_at)",
    )


__all__ = [
    "SCHEMA_VERSION", "PROGRAMS_TABLE", "REFERRALS_TABLE",
    "EVENTS_TABLE", "schema_statements",
]
