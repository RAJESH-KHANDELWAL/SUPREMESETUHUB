"""SUPREME PRINT ON DEMAND catalog, pricing, and design-brief persistence.

Seed costs and design concepts are planning defaults, not live provider quotes or
live trend measurements. Verify provider costs before enabling paid checkout.
"""
from __future__ import annotations

import json
import math
from datetime import datetime, timezone
from uuid import uuid4

from backend.database.service import DatabaseService

PRODUCTS = {
    "POD-TEE": {
        "sku": "POD-TEE", "name": "Custom T-Shirt", "category": "Apparel",
        "description": "Everyday tee for typography, creator, culture and custom art designs.",
        "estimated_cost": {"IN": 320, "GLOBAL": 8},
        "price_cap": {"IN": 2499, "GLOBAL": 79},
    },
    "POD-HOODIE": {
        "sku": "POD-HOODIE", "name": "Premium Hoodie", "category": "Apparel",
        "description": "Premium-feel layer for limited-edition and personalised artwork.",
        "estimated_cost": {"IN": 700, "GLOBAL": 18},
        "price_cap": {"IN": 3999, "GLOBAL": 129},
    },
    "POD-MUG": {
        "sku": "POD-MUG", "name": "Custom Mug", "category": "Home & Gifts",
        "description": "Personalised gifts, illustrations, names and short-form typography.",
        "estimated_cost": {"IN": 180, "GLOBAL": 5},
        "price_cap": {"IN": 999, "GLOBAL": 39},
    },
    "POD-POSTER": {
        "sku": "POD-POSTER", "name": "Art Poster", "category": "Wall Art",
        "description": "Wall art for original illustrations, travel themes and motivational art.",
        "estimated_cost": {"IN": 150, "GLOBAL": 4},
        "price_cap": {"IN": 1299, "GLOBAL": 49},
    },
    "POD-TOTE": {
        "sku": "POD-TOTE", "name": "Printed Tote Bag", "category": "Accessories",
        "description": "Reusable tote for minimalist, cultural and creator-led designs.",
        "estimated_cost": {"IN": 220, "GLOBAL": 6},
        "price_cap": {"IN": 1499, "GLOBAL": 59},
    },
    "POD-CASE": {
        "sku": "POD-CASE", "name": "Custom Phone Case", "category": "Accessories",
        "description": "Personalised patterns, initials and original graphic artwork.",
        "estimated_cost": {"IN": 240, "GLOBAL": 7},
        "price_cap": {"IN": 1499, "GLOBAL": 59},
    },
}

DESIGN_STARTERS = [
    {"id": "heritage-minimal", "name": "Bharat Heritage Minimal", "tags": ["Bharat", "heritage", "minimal"], "note": "Original cultural-inspired geometry and typography; avoid protected emblems and copied artwork."},
    {"id": "creator-economy", "name": "Creator & Builder Mindset", "tags": ["creator", "startup", "digital"], "note": "Original creator, learning and entrepreneurship messages."},
    {"id": "cosmic-calm", "name": "Cosmic Calm", "tags": ["space", "abstract", "calm"], "note": "Abstract celestial forms and calm colour palettes."},
    {"id": "personal-gift", "name": "Personalised Gifts", "tags": ["name", "date", "gift"], "note": "Customer-supplied names, dates and original personalisation."},
    {"id": "bold-typography", "name": "Bold Typography", "tags": ["typography", "streetwear", "statement"], "note": "Short original phrases with high-contrast, print-friendly layouts."},
]

class PrintOnDemandService:
    """Persist customer design briefs and calculate market-aware draft quotes."""

    def __init__(self, database: DatabaseService | None = None):
        self.database = database or DatabaseService()
        self.database.initialize()
        self.database.execute("""
            CREATE TABLE IF NOT EXISTS pod_design_briefs (
                brief_id TEXT PRIMARY KEY,
                user_id TEXT NOT NULL,
                product_sku TEXT NOT NULL,
                market TEXT NOT NULL,
                tier TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                design_prompt TEXT NOT NULL,
                notes TEXT NOT NULL DEFAULT '',
                quote_json TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'DRAFT',
                created_at TEXT NOT NULL
            )
        """)
        self.database.execute("CREATE INDEX IF NOT EXISTS idx_pod_briefs_user ON pod_design_briefs(user_id, created_at)")

    @staticmethod
    def _normalise_market(market: str) -> str:
        value = market.strip().upper()
        if value not in {"IN", "GLOBAL"}:
            raise ValueError("MARKET_MUST_BE_IN_OR_GLOBAL")
        return value

    def catalog(self, market: str = "IN") -> dict:
        market = self._normalise_market(market)
        currency = "INR" if market == "IN" else "USD"
        products = []
        for item in PRODUCTS.values():
            standard = self.quote(item["sku"], market, "STANDARD", 3, 1)
            premium = self.quote(item["sku"], market, "PREMIUM", 3, 1)
            products.append({
                "sku": item["sku"], "name": item["name"], "category": item["category"],
                "description": item["description"], "currency": currency,
                "standard_from": standard["unit_price"], "premium_from": premium["unit_price"],
                "cost_is_estimate": True,
            })
        return {
            "market": market, "currency": currency, "products": products,
            "design_starters": DESIGN_STARTERS,
            "trend_data_status": "EDITORIAL_STARTERS_NOT_LIVE_TREND_DATA",
            "pricing_notice": "Draft estimates only. Confirm current printing, shipping, taxes, payment fees and supplier availability before checkout.",
        }

    def quote(self, product_sku: str, market: str, tier: str = "STANDARD", demand_score: int = 3, quantity: int = 1) -> dict:
        market = self._normalise_market(market)
        tier = tier.strip().upper()
        if tier not in {"STANDARD", "PREMIUM"}:
            raise ValueError("TIER_MUST_BE_STANDARD_OR_PREMIUM")
        if product_sku not in PRODUCTS:
            raise ValueError("UNKNOWN_PRODUCT_SKU")
        if not 1 <= int(demand_score) <= 5:
            raise ValueError("DEMAND_SCORE_MUST_BE_BETWEEN_1_AND_5")
        if not 1 <= int(quantity) <= 100:
            raise ValueError("QUANTITY_MUST_BE_BETWEEN_1_AND_100")

        product = PRODUCTS[product_sku]
        cost = product["estimated_cost"][market]
        demand_multiplier = 0.85 + (int(demand_score) - 1) * 0.125
        tier_cost_multiplier = 1.0 if tier == "STANDARD" else 1.35
        target_margin = 0.32 if tier == "STANDARD" else 0.45
        raw = (cost * tier_cost_multiplier * demand_multiplier) / (1 - target_margin)
        step = 10 if market == "IN" else 1
        unit_price = int(math.ceil(raw / step) * step)
        unit_price = min(unit_price, product["price_cap"][market])
        if unit_price <= cost * tier_cost_multiplier:
            raise ValueError("PRICE_CAP_WOULD_CREATE_A_LOSS_REVIEW_COSTS")
        total = unit_price * int(quantity)
        estimated_unit_cost = round(cost * tier_cost_multiplier, 2)
        estimated_margin = round((unit_price - estimated_unit_cost) / unit_price, 4)
        return {
            "product_sku": product_sku, "product_name": product["name"],
            "market": market, "currency": "INR" if market == "IN" else "USD",
            "tier": tier, "quantity": int(quantity), "demand_score": int(demand_score),
            "demand_multiplier": round(demand_multiplier, 3),
            "unit_price": unit_price, "total_price": total,
            "estimated_unit_cost": estimated_unit_cost,
            "estimated_gross_margin": estimated_margin,
            "cost_is_estimate": True,
            "excluded_costs": ["shipping", "taxes", "payment fees", "returns", "provider-specific premium options"],
            "notice": "Planning quote only; not a live supplier quote or payment request.",
        }

    def create_brief(self, user_id: str, product_sku: str, market: str, tier: str, quantity: int, demand_score: int, design_prompt: str, notes: str = "") -> dict:
        user_id = str(user_id or "").strip()
        design_prompt = design_prompt.strip()
        if not user_id:
            raise ValueError("AUTHENTICATED_USER_ID_REQUIRED")
        if not design_prompt or len(design_prompt) > 600:
            raise ValueError("DESIGN_PROMPT_REQUIRED_MAX_600_CHARACTERS")
        if len(notes) > 1000:
            raise ValueError("NOTES_MAX_1000_CHARACTERS")
        quote = self.quote(product_sku, market, tier, demand_score, quantity)
        brief_id = f"POD-{uuid4().hex.upper()}"
        created_at = datetime.now(timezone.utc).isoformat()
        self.database.execute("""
            INSERT INTO pod_design_briefs
            (brief_id, user_id, product_sku, market, tier, quantity, design_prompt, notes, quote_json, status, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (brief_id, user_id, product_sku, quote["market"], quote["tier"], int(quantity), design_prompt, notes.strip(), json.dumps(quote), "DRAFT", created_at))
        return {"brief_id": brief_id, "status": "DRAFT", "created_at": created_at, "quote": quote,
                "message": "Design brief saved. No payment or print-provider order has been placed."}

    def list_briefs(self, user_id: str) -> list[dict]:
        rows = self.database.fetchall("""
            SELECT brief_id, product_sku, market, tier, quantity, design_prompt, notes, quote_json, status, created_at
            FROM pod_design_briefs WHERE user_id = ? ORDER BY created_at DESC
        """, (str(user_id),))
        return [{
            "brief_id": row["brief_id"], "product_sku": row["product_sku"],
            "market": row["market"], "tier": row["tier"], "quantity": row["quantity"],
            "design_prompt": row["design_prompt"], "notes": row["notes"],
            "quote": json.loads(row["quote_json"]), "status": row["status"],
            "created_at": row["created_at"],
        } for row in rows]
