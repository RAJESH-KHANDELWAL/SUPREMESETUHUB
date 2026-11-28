from fastapi import APIRouter

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
