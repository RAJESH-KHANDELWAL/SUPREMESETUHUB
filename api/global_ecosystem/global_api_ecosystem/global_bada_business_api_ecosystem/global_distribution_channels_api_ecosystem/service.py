from .catalog import get_channel, list_channels
from .business_profiles import get_business_profile

class DistributionChannelsService:
    DOMAIN_ID = "distribution_channels_api_ecosystem"

    def _enrich(self, item):
        record = dict(item)
        profile = get_business_profile(item["id"])
        if profile:
            record["business_profile"] = profile
        return record

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
        return [self._enrich(item) for item in items]

    def get_channel(self, channel_id):
        item = get_channel(channel_id)
        return self._enrich(item) if item else None

    def get_status(self):
        return {
            "success": True,
            "domain_id": self.DOMAIN_ID,
            "status": "taxonomy_and_business_profile_scaffold",
            "channel_count": len(list_channels()),
            "business_profile_count": 25,
            "coverage": ["india", "global"],
            "operating_modes": ["online", "offline", "hybrid"],
            "scope": "manufacturer dispatch through channel intermediaries to final customer handover",
            "note": "Profiles describe generic operating models and data fields. They are not legal advice, verified providers, live inventory, shipment tracking or transaction processing."
        }
