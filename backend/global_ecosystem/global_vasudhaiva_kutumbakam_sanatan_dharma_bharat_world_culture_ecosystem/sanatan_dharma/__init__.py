"""Sanatan Dharma knowledge domain package."""
from .domain import (
    DOMAIN_ID, DOMAIN_NAME, DOMAIN_DESCRIPTION, SUBJECT_AREAS,
    KnowledgeRecord, search_records,
)

__all__ = [
    "DOMAIN_ID", "DOMAIN_NAME", "DOMAIN_DESCRIPTION", "SUBJECT_AREAS",
    "KnowledgeRecord", "search_records",
]

from .knowledge_index import catalogue, search as search_knowledge
from .texts import get_veda, list_vedas, get_upanishad, search_upanishads, get_itihasa, list_itihasa, chapter_map
from .philosophy import get_darshana, compare_darshanas, list_vedanta_schools
from .practice import get_samskara_framework, list_yoga_traditions
from .traditions import list_tradition_streams
from .places import list_pilgrimage_clusters
from .rituals import list_yajna_areas

__all__ += [
    "catalogue", "search_knowledge", "get_veda", "list_vedas",
    "get_upanishad", "search_upanishads", "get_itihasa", "list_itihasa",
    "chapter_map", "get_darshana", "compare_darshanas",
    "list_vedanta_schools", "get_samskara_framework",
    "list_yoga_traditions", "list_tradition_streams",
    "list_pilgrimage_clusters", "list_yajna_areas",
]
