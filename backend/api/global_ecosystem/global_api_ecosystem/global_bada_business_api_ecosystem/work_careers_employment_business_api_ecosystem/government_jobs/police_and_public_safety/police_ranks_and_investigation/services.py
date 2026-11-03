"""Application services for Police rank and investigation posts."""
from dataclasses import asdict
from .models import GovernmentPost
from .validators import validate_post

def register_post(post: GovernmentPost) -> dict:
    validate_post(post)
    record = asdict(post)
    record.update({"job_family": "police_and_public_safety", "specialization": "police_ranks_and_investigation", "work_function": "law_enforcement_and_investigation"})
    return record

def filter_by_authority(posts: list[GovernmentPost], authority: str) -> list[GovernmentPost]:
    query = authority.casefold()
    return [post for post in posts if query in post.recruiting_authority.casefold()]
