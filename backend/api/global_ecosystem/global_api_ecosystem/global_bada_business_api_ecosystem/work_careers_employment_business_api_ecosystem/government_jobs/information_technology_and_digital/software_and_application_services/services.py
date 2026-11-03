"""Application services for Software and application development posts."""
from dataclasses import asdict
from .models import GovernmentPost
from .validators import validate_post

def register_post(post: GovernmentPost) -> dict:
    validate_post(post)
    record = asdict(post)
    record.update({"job_family": "information_technology_and_digital", "specialization": "software_and_application_services", "work_function": "public_digital_service_development"})
    return record

def filter_by_authority(posts: list[GovernmentPost], authority: str) -> list[GovernmentPost]:
    query = authority.casefold()
    return [post for post in posts if query in post.recruiting_authority.casefold()]
