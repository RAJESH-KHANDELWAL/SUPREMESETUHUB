"""Google Ads SDK adapter; requires approved developer token and OAuth credentials."""
from __future__ import annotations
import os

def build_client():
    try:
        from google.ads.googleads.client import GoogleAdsClient
    except ImportError as exc:
        raise RuntimeError("Install the optional google-ads package to use Google Ads") from exc
    path = os.getenv("GOOGLE_ADS_CONFIGURATION_FILE", "").strip()
    if path:
        return GoogleAdsClient.load_from_storage(path)
    keys = ("GOOGLE_ADS_DEVELOPER_TOKEN", "GOOGLE_ADS_CLIENT_ID", "GOOGLE_ADS_CLIENT_SECRET", "GOOGLE_ADS_REFRESH_TOKEN")
    missing = [key for key in keys if not os.getenv(key)]
    if missing:
        raise RuntimeError("Missing Google Ads configuration: " + ", ".join(missing))
    return GoogleAdsClient.load_from_dict({
        "developer_token": os.environ["GOOGLE_ADS_DEVELOPER_TOKEN"],
        "client_id": os.environ["GOOGLE_ADS_CLIENT_ID"],
        "client_secret": os.environ["GOOGLE_ADS_CLIENT_SECRET"],
        "refresh_token": os.environ["GOOGLE_ADS_REFRESH_TOKEN"],
        "use_proto_plus": True,
    })
