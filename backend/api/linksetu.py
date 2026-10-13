from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field

from backend.security.dependencies import get_current_user
from backend.platform.linksetu.social.service import LinkSetuSocialService
from backend.platform.linksetu.notification.service import LinkSetuNotificationService

from backend.platform.linksetu.story import LinkSetuStoryService
from backend.platform.linksetu.live import LinkSetuLiveService
from backend.platform.linksetu.call import LinkSetuCallService
from backend.platform.linksetu.status import LinkSetuStatusService
from backend.platform.linksetu.broadcast import LinkSetuBroadcastService
from backend.platform.linksetu.contact import LinkSetuContactService
from backend.platform.linksetu.list import LinkSetuListService
from backend.platform.linksetu.topic import LinkSetuTopicService
from backend.platform.linksetu.job import LinkSetuJobService
from backend.platform.linksetu.professional import LinkSetuProfessionalService


router = APIRouter(
    prefix="/api/v1/linksetu",
    tags=["LINKSETU"],
)


story_service = LinkSetuStoryService()
live_service = LinkSetuLiveService()
call_service = LinkSetuCallService()
status_service = LinkSetuStatusService()
broadcast_service = LinkSetuBroadcastService()
contact_service = LinkSetuContactService()
list_service = LinkSetuListService()
topic_service = LinkSetuTopicService()
job_service = LinkSetuJobService()
professional_service = LinkSetuProfessionalService()
social_service = LinkSetuSocialService()
notification_service = social_service.notifications


class PostCreateRequest(BaseModel):
    content: str = Field(min_length=1, max_length=10000)


class CommentCreateRequest(BaseModel):
    content: str = Field(min_length=1, max_length=3000)


class ReactionRequest(BaseModel):
    reaction: str = Field(default="like", min_length=1, max_length=32)


def _actor(current_user: dict) -> str:
    user_id = str(current_user.get("user_id", "")).strip()
    if not user_id:
        raise HTTPException(status_code=401, detail="AUTHENTICATED_USER_ID_REQUIRED")
    return user_id


@router.post("/posts", status_code=201)
def create_social_post(payload: PostCreateRequest, current_user: dict = Depends(get_current_user)):
    try:
        return {"success": True, "data": social_service.create_post(_actor(current_user), payload.content)}
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


@router.get("/posts")
def list_social_posts(limit: int = 50, current_user: dict = Depends(get_current_user)):
    return {"success": True, "data": social_service.list_posts(limit)}


@router.get("/posts/{post_id}/comments")
def list_social_comments(post_id: str, current_user: dict = Depends(get_current_user)):
    try:
        return {"success": True, "data": social_service.get_comments(post_id)}
    except LookupError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.post("/posts/{post_id}/comments", status_code=201)
def create_social_comment(post_id: str, payload: CommentCreateRequest, current_user: dict = Depends(get_current_user)):
    try:
        return {"success": True, "data": social_service.add_comment(_actor(current_user), post_id, payload.content)}
    except LookupError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


@router.post("/posts/{post_id}/reactions")
def add_social_reaction(post_id: str, payload: ReactionRequest, current_user: dict = Depends(get_current_user)):
    try:
        return {"success": True, "data": social_service.react(_actor(current_user), post_id, payload.reaction)}
    except LookupError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


@router.delete("/posts/{post_id}/reactions")
def remove_social_reaction(post_id: str, current_user: dict = Depends(get_current_user)):
    try:
        return {"success": True, "data": social_service.remove_reaction(_actor(current_user), post_id)}
    except LookupError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.get("/posts/{post_id}/reactions")
def get_social_reactions(post_id: str, current_user: dict = Depends(get_current_user)):
    try:
        return {"success": True, "data": social_service.get_reactions(post_id)}
    except LookupError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.post("/users/{target_user_id}/follow")
def follow_social_user(target_user_id: str, current_user: dict = Depends(get_current_user)):
    try:
        return {"success": True, "data": social_service.follow(_actor(current_user), target_user_id)}
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


@router.delete("/users/{target_user_id}/follow")
def unfollow_social_user(target_user_id: str, current_user: dict = Depends(get_current_user)):
    return {"success": True, "data": social_service.unfollow(_actor(current_user), target_user_id)}


@router.get("/users/{target_user_id}/followers")
def list_social_followers(target_user_id: str, current_user: dict = Depends(get_current_user)):
    return {"success": True, "data": social_service.followers(target_user_id)}


@router.get("/users/{target_user_id}/following")
def list_social_following(target_user_id: str, current_user: dict = Depends(get_current_user)):
    return {"success": True, "data": social_service.following(target_user_id)}


@router.get("/notifications")
def list_social_notifications(limit: int = 50, current_user: dict = Depends(get_current_user)):
    return {"success": True, **notification_service.get_notifications(_actor(current_user), limit)}


@router.patch("/notifications/{notification_id}/read")
def read_social_notification(notification_id: str, current_user: dict = Depends(get_current_user)):
    return {"success": True, "data": notification_service.mark_as_read(notification_id, _actor(current_user))}


@router.post("/notifications/read-all")
def read_all_social_notifications(current_user: dict = Depends(get_current_user)):
    return {"success": True, "data": notification_service.mark_all_as_read(_actor(current_user))}


@router.get("/status")
def linksetu_status():
    return {
        "success": True,
        "platform": "LINKSETU",
        "status": "active",
        "backend": "connected",
        "modules": {
            "story": True,
            "live": True,
            "call": True,
            "status": True,
            "broadcast": True,
            "contact": True,
            "list": True,
            "topic": True,
            "job": True,
            "professional": True,
        },
    }


@router.get("/story/feed/{user_id}")
def story_feed(user_id: str):
    return story_service.get_story_feed(user_id)


@router.get("/live/feed/{user_id}")
def live_feed(user_id: str):
    return live_service.get_live_feed(user_id)


@router.get("/status/feed/{user_id}")
def status_feed(user_id: str):
    return status_service.get_status_feed(user_id)


@router.get("/broadcast/feed/{user_id}")
def broadcast_feed(user_id: str):
    return broadcast_service.get_broadcast_feed(user_id)


@router.get("/contact/list/{user_id}")
def contact_list(user_id: str):
    return contact_service.get_contacts(user_id)


@router.get("/list/user/{user_id}")
def user_lists(user_id: str):
    return list_service.get_user_lists(user_id)


@router.get("/topic/feed/{topic_id}")
def topic_feed(topic_id: str):
    return topic_service.get_topic_feed(topic_id)


@router.get("/job/search")
def search_jobs(query: str = ""):
    return job_service.search_jobs(query)


@router.get("/professional/{user_id}")
def professional_profile(user_id: str):
    return professional_service.get_profile(user_id)
