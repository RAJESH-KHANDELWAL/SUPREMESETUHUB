"""Flexible digital-only marketplace catalog on the shared SQLite foundation.

The catalog supports arbitrary digital asset categories and format metadata.
Payment and download delivery remain disabled until a payment provider, verified
webhooks, and private file storage are configured and tested.
"""
from __future__ import annotations

import json
import re
import uuid
from backend.database.service import DatabaseService


class DigitalMarketplaceService:
    """Manage digital asset listings without exposing private storage keys."""

    def __init__(self, database: DatabaseService | None = None):
        self.database = database or DatabaseService()
        self.database.initialize()
        self.database.execute("""
            CREATE TABLE IF NOT EXISTS digital_designs (
                design_id TEXT PRIMARY KEY,
                slug TEXT NOT NULL UNIQUE,
                title TEXT NOT NULL,
                description TEXT NOT NULL DEFAULT '',
                category TEXT NOT NULL,
                preview_url TEXT NOT NULL DEFAULT '',
                private_storage_key TEXT NOT NULL,
                license_label TEXT NOT NULL DEFAULT 'Personal digital use',
                status TEXT NOT NULL DEFAULT 'DRAFT'
                    CHECK (status IN ('DRAFT', 'IN_REVIEW', 'PUBLISHED', 'ARCHIVED')),
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                published_at TEXT
            )
        """)
        # Additive migrations preserve older catalog rows.
        for name, definition in (
            ("asset_type", "TEXT NOT NULL DEFAULT 'IMAGE'"),
            ("file_format", "TEXT NOT NULL DEFAULT 'PNG'"),
            ("tags_json", "TEXT NOT NULL DEFAULT '[]'"),
            ("prompt_notes", "TEXT NOT NULL DEFAULT ''"),
        ):
            self.database.add_column_if_missing("digital_designs", name, definition)
        self.database.execute("""
            CREATE TABLE IF NOT EXISTS digital_design_prices (
                price_id TEXT PRIMARY KEY,
                design_id TEXT NOT NULL,
                market_code TEXT NOT NULL CHECK (market_code IN ('IN', 'GLOBAL')),
                currency_code TEXT NOT NULL CHECK (
                    (market_code = 'IN' AND currency_code = 'INR') OR
                    (market_code = 'GLOBAL' AND currency_code = 'USD')
                ),
                price_minor INTEGER NOT NULL CHECK (price_minor > 0),
                is_active INTEGER NOT NULL DEFAULT 1 CHECK (is_active IN (0, 1)),
                FOREIGN KEY (design_id) REFERENCES digital_designs(design_id) ON DELETE CASCADE,
                UNIQUE (design_id, market_code)
            )
        """)
        self.database.execute("""
            CREATE INDEX IF NOT EXISTS idx_digital_designs_publication
            ON digital_designs(status, published_at)
        """)
        self.database.execute("""
            CREATE INDEX IF NOT EXISTS idx_digital_prices_market
            ON digital_design_prices(market_code, is_active)
        """)

    @staticmethod
    def normalise_market(market: str) -> str:
        value = str(market).strip().upper()
        if value not in {"IN", "GLOBAL"}:
            raise ValueError("MARKET_MUST_BE_IN_OR_GLOBAL")
        return value

    @staticmethod
    def _slug(value: str) -> str:
        slug = re.sub(r"[^a-z0-9]+", "-", value.casefold()).strip("-")
        if not slug:
            raise ValueError("TITLE_MUST_CREATE_A_VALID_SLUG")
        return slug[:120]

    def save_design(self, payload: dict) -> dict:
        """Create/update a draft listing; publishing is a separate explicit action."""
        title = str(payload.get("title", "")).strip()
        category = str(payload.get("category", "uncategorized")).strip().lower()
        storage_key = str(payload.get("private_storage_key", "")).strip()
        if not title or len(title) > 180:
            raise ValueError("TITLE_MUST_BE_1_TO_180_CHARACTERS")
        if not category or len(category) > 80:
            raise ValueError("CATEGORY_MUST_BE_1_TO_80_CHARACTERS")
        if not storage_key or len(storage_key) > 500:
            raise ValueError("PRIVATE_STORAGE_KEY_REQUIRED")
        design_id = str(payload.get("design_id") or uuid.uuid4().hex)
        slug = self._slug(str(payload.get("slug") or title))
        asset_type = str(payload.get("asset_type", "IMAGE")).strip().upper()
        file_format = str(payload.get("file_format", "PNG")).strip().upper()
        if not re.fullmatch(r"[A-Z0-9_-]{1,32}", asset_type):
            raise ValueError("INVALID_ASSET_TYPE")
        if not re.fullmatch(r"[A-Z0-9.+_-]{1,20}", file_format):
            raise ValueError("INVALID_FILE_FORMAT")
        tags = payload.get("tags", [])
        if not isinstance(tags, list) or len(tags) > 40:
            raise ValueError("TAGS_MUST_BE_A_LIST_OF_UP_TO_40_ITEMS")
        clean_tags = [str(tag).strip()[:40] for tag in tags if str(tag).strip()]
        preview_url = str(payload.get("preview_url", "")).strip()
        if preview_url and not preview_url.startswith("https://"):
            raise ValueError("PREVIEW_URL_MUST_USE_HTTPS")
        status = str(payload.get("status", "DRAFT")).upper()
        if status not in {"DRAFT", "IN_REVIEW", "PUBLISHED", "ARCHIVED"}:
            raise ValueError("INVALID_DESIGN_STATUS")
        license_label = str(payload.get("license_label", "Personal digital use")).strip()[:120]
        description = str(payload.get("description", "")).strip()[:4000]
        prompt_notes = str(payload.get("prompt_notes", "")).strip()[:2000]
        prices = payload.get("prices", {})
        if not isinstance(prices, dict):
            raise ValueError("PRICES_MUST_BE_AN_OBJECT")
        normalized_prices = []
        for market, currency in (("IN", "INR"), ("GLOBAL", "USD")):
            if market in prices and prices[market] is not None:
                amount = prices[market]
                if isinstance(amount, bool) or not isinstance(amount, int) or amount <= 0:
                    raise ValueError(f"{market}_PRICE_MUST_BE_POSITIVE_MINOR_UNITS")
                normalized_prices.append((market, currency, amount))
        if not normalized_prices:
            raise ValueError("AT_LEAST_ONE_MARKET_PRICE_REQUIRED")
        if status == "PUBLISHED" and not preview_url:
            raise ValueError("PUBLISHED_DESIGN_REQUIRES_HTTPS_PREVIEW_URL")
        if storage_key.startswith(("http://", "https://")):
            raise ValueError("PRIVATE_STORAGE_KEY_MUST_NOT_BE_A_PUBLIC_URL")
        self.database.execute("""
            INSERT INTO digital_designs
                (design_id, slug, title, description, category, preview_url,
                 private_storage_key, license_label, status, published_at,
                 asset_type, file_format, tags_json, prompt_notes)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, CASE WHEN ? = 'PUBLISHED' THEN CURRENT_TIMESTAMP ELSE NULL END, ?, ?, ?, ?)
            ON CONFLICT(design_id) DO UPDATE SET
                slug=excluded.slug, title=excluded.title, description=excluded.description,
                category=excluded.category, preview_url=excluded.preview_url,
                private_storage_key=excluded.private_storage_key,
                license_label=excluded.license_label, status=excluded.status,
                published_at=CASE WHEN excluded.status='PUBLISHED'
                    THEN COALESCE(digital_designs.published_at, CURRENT_TIMESTAMP) ELSE NULL END,
                asset_type=excluded.asset_type, file_format=excluded.file_format,
                tags_json=excluded.tags_json, prompt_notes=excluded.prompt_notes
        """, (design_id, slug, title, description, category, preview_url, storage_key,
              license_label, status, status, asset_type, file_format,
              json.dumps(clean_tags), prompt_notes))
        for market, currency, amount in normalized_prices:
            self.database.execute("""
                INSERT INTO digital_design_prices
                    (price_id, design_id, market_code, currency_code, price_minor, is_active)
                VALUES (?, ?, ?, ?, ?, 1)
                ON CONFLICT(design_id, market_code) DO UPDATE SET
                    currency_code=excluded.currency_code,
                    price_minor=excluded.price_minor, is_active=1
            """, (uuid.uuid4().hex, design_id, market, currency, amount))
        return {"design_id": design_id, "slug": slug, "status": status,
                "markets": [item[0] for item in normalized_prices]}

    def catalog(self, market: str = "IN", limit: int = 24, offset: int = 0,
                category: str | None = None, search: str | None = None) -> dict:
        market = self.normalise_market(market)
        if not 1 <= int(limit) <= 100:
            raise ValueError("LIMIT_MUST_BE_BETWEEN_1_AND_100")
        if int(offset) < 0:
            raise ValueError("OFFSET_MUST_BE_NON_NEGATIVE")
        currency = "INR" if market == "IN" else "USD"
        clauses = ["d.status = 'PUBLISHED'", "p.market_code = ?", "p.is_active = 1"]
        params: list = [market]
        if category:
            clauses.append("LOWER(d.category) = ?")
            params.append(str(category).strip().lower())
        if search:
            clauses.append("(LOWER(d.title) LIKE ? OR LOWER(d.description) LIKE ? OR LOWER(d.tags_json) LIKE ?)")
            term = f"%{str(search).strip().lower()[:100]}%"
            params.extend([term, term, term])
        params.extend([int(limit), int(offset)])
        rows = self.database.fetchall(f"""
            SELECT d.design_id, d.slug, d.title, d.description, d.category,
                   d.preview_url, d.license_label, d.published_at,
                   d.asset_type, d.file_format, d.tags_json,
                   p.market_code, p.currency_code, p.price_minor
            FROM digital_designs AS d
            INNER JOIN digital_design_prices AS p ON p.design_id = d.design_id
            WHERE {' AND '.join(clauses)}
            ORDER BY d.published_at DESC, d.design_id DESC
            LIMIT ? OFFSET ?
        """, tuple(params))
        designs = []
        for row in rows:
            item = dict(row)
            item["tags"] = json.loads(item.pop("tags_json") or "[]")
            minor = int(item["price_minor"])
            item["price"] = f"{minor / 100:.2f}"
            item["price_minor"] = minor
            designs.append(item)
        return {
            "market": market, "currency": currency, "count": len(designs),
            "designs": designs,
            "checkout_status": "DISABLED_UNTIL_PAYMENT_PROVIDER_AND_SIGNED_WEBHOOKS_ARE_CONFIGURED",
            "delivery_status": "PRIVATE_PAID_DOWNLOAD_FLOW_NOT_YET_ENABLED",
            "tax_status": "TAX_CONFIGURATION_REQUIRES_VERIFICATION",
            "product_model": "FLEXIBLE_DIGITAL_ASSETS_ONLY",
            "supported_asset_types": ["IMAGE", "ILLUSTRATION", "WALLPAPER", "TEMPLATE", "ICON_PACK", "CLIPART", "PATTERN", "3D_ASSET", "DOCUMENT", "FONT", "AUDIO", "VIDEO", "BUNDLE", "OTHER"],
        }
