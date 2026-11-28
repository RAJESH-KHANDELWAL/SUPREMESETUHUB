"""LINKSETU marketplace experience service."""


class LinkSetuMarketplaceService:
    """Manage marketplace experiences in LINKSETU."""

    platform_name = "LINKSETU"

    allowed_listing_types = (
        "product",
        "service",
        "digital_product",
    )

    def create_listing(
        self,
        seller_id: str,
        title: str,
        description: str = "",
        listing_type: str = "product",
        price: float = 0.0,
        currency: str = "INR",
    ) -> dict:

        if listing_type not in self.allowed_listing_types:
            raise ValueError(
                f"Unsupported listing type: {listing_type}"
            )

        return {
            "platform": self.platform_name,
            "seller_id": seller_id,
            "title": title,
            "description": description,
            "listing_type": listing_type,
            "price": price,
            "currency": currency,
            "status": "created",
        }

    def get_listing(
        self,
        listing_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "listing_id": listing_id,
        }

    def update_listing(
        self,
        listing_id: str,
        data: dict,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "listing_id": listing_id,
            "data": data,
            "status": "updated",
        }

    def search_listings(
        self,
        query: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "query": query,
            "listings": [],
        }

    def create_order(
        self,
        buyer_id: str,
        listing_id: str,
        quantity: int = 1,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "buyer_id": buyer_id,
            "listing_id": listing_id,
            "quantity": quantity,
            "status": "created",
        }
