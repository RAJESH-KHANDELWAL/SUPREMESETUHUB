from .catalog import get_channel, list_channels

class DistributionChannelsService:
    DOMAIN_ID = "distribution_channels_api_ecosystem"

    def list_channels(self, query=None):
        items = list_channels()
        if query:
            q = query.strip().casefold()
            items = [
                item for item in items
                if q in item["id"].casefold()
                or q in item["name"].casefold()
                or q in item["stage"].casefold()
                or any(q in participant.replace("_", " ").casefold() for participant in item["participants"])
            ]
        return items

    def get_channel(self, channel_id):
        return get_channel(channel_id)

    def get_status(self):
        return {
            "success": True,
            "domain_id": self.DOMAIN_ID,
            "status": "taxonomy_scaffold",
            "channel_count": len(list_channels()),
            "coverage": ["india", "global"],
            "operating_modes": ["online", "offline", "hybrid"],
            "scope": "manufacturer dispatch through channel intermediaries to final customer handover",
            "note": "A channel taxonomy only; it does not imply verified providers, live inventory, shipment tracking or transaction processing."
        }
