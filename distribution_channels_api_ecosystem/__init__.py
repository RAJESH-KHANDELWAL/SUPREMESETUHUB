"""Independent distribution-channel taxonomy API ecosystem."""

from .catalog import CHANNELS, get_channel, list_channels
from .service import DistributionChannelsService

__all__ = ["CHANNELS", "get_channel", "list_channels", "DistributionChannelsService"]
