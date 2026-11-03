"""Application services for Judicial officer recruitment."""
from dataclasses import asdict
from .models import GovernmentPost
from .validators import validate_post

def register_post(post: GovernmentPost) -> dict:
    validate_post(post)
    record = asdict(post)
    record.update({"job_family": "judiciary_and_legal", "specialization": "judicial_officers", "work_function": "adjudication"})
    return record

def filter_by_authority(posts: list[GovernmentPost], authority: str) -> list[GovernmentPost]:
    query = authority.casefold()
    return [post for post in posts if query in post.recruiting_authority.casefold()]
