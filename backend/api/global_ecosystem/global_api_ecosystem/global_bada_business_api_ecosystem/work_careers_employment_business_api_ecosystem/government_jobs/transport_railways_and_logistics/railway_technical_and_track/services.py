"""Application services for Railway technical, signalling and track posts."""
from dataclasses import asdict
from .models import GovernmentPost
from .validators import validate_post

def register_post(post: GovernmentPost) -> dict:
    validate_post(post)
    record = asdict(post)
    record.update({"job_family": "transport_railways_and_logistics", "specialization": "railway_technical_and_track", "work_function": "railway_asset_maintenance"})
    return record

def filter_by_authority(posts: list[GovernmentPost], authority: str) -> list[GovernmentPost]:
    query = authority.casefold()
    return [post for post in posts if query in post.recruiting_authority.casefold()]
