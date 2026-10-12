"""Digital-only SUPREME marketplace catalog on the existing SQLite foundation.

This module deliberately does not create physical fulfillment, payment, or
download delivery flows. Checkout stays disabled until provider approval,
server-side payment verification, and private file delivery are implemented.
"""
from __future__ import annotations

from backend.database.service import DatabaseService


class DigitalMarketplaceService:
    """Store and read published digital designs without exposing private files."""

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

    def catalog(self, market: str = "IN", limit: int = 24, offset: int = 0) -> dict:
        market = self.normalise_market(market)
        if not 1 <= int(limit) <= 100:
            raise ValueError("LIMIT_MUST_BE_BETWEEN_1_AND_100")
        if int(offset) < 0:
            raise ValueError("OFFSET_MUST_BE_NON_NEGATIVE")
        currency = "INR" if market == "IN" else "USD"
        rows = self.database.fetchall("""
            SELECT d.design_id, d.slug, d.title, d.description, d.category,
                   d.preview_url, d.license_label, d.published_at,
                   p.market_code, p.currency_code, p.price_minor
            FROM digital_designs AS d
            INNER JOIN digital_design_prices AS p
                ON p.design_id = d.design_id
               AND p.market_code = ?
               AND p.is_active = 1
            WHERE d.status = 'PUBLISHED'
            ORDER BY d.published_at DESC, d.design_id DESC
            LIMIT ? OFFSET ?
        """, (market, int(limit), int(offset)))
        designs = []
        for row in rows:
            item = dict(row)
            minor = int(item["price_minor"])
            item["price"] = f"{minor / 100:.2f}"
            item["price_minor"] = minor
            designs.append(item)
        return {
            "market": market,
            "currency": currency,
            "count": len(designs),
            "designs": designs,
            "checkout_status": "DISABLED_UNTIL_MERCHANT_APPROVAL_AND_PAYMENT_VERIFICATION",
            "delivery_status": "PRIVATE_DOWNLOAD_DELIVERY_NOT_YET_IMPLEMENTED",
            "tax_status": "TAX_CONFIGURATION_REQUIRES_VERIFICATION",
            "product_model": "DIGITAL_DOWNLOADS_ONLY",
        }
