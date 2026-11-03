"""Application services for Other-rank and defence technical trade posts."""
from dataclasses import asdict
from .models import GovernmentPost
from .validators import validate_post

def register_post(post: GovernmentPost) -> dict:
    validate_post(post)
    record = asdict(post)
    record.update({"job_family": "defence_and_uniformed_services", "specialization": "other_ranks_and_technical_trades", "work_function": "operational_and_technical_duties"})
    return record

def filter_by_authority(posts: list[GovernmentPost], authority: str) -> list[GovernmentPost]:
    query = authority.casefold()
    return [post for post in posts if query in post.recruiting_authority.casefold()]
