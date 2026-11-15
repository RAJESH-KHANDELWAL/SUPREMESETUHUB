"""Unified discovery interface for the Sanatan Dharma knowledge subdomains."""
from __future__ import annotations
from typing import Any
from .texts.vedas import VEDAS, get_veda
from .texts.upanishads import UPANISHADS, get_upanishad, search_upanishads
from .texts.itihasa import ITIHASA_WORKS, get_itihasa
from .texts.puranas import PURANA_CATEGORIES
from .philosophy.darshana import DARSHANAS, get_darshana
from .philosophy.vedanta_schools import VEDANTA_SCHOOLS
from .practice.samskara import SAMSKARA_FRAMEWORK
from .practice.yoga_traditions import YOGA_TRADITIONS
from .history.chronology import CHRONOLOGY
from .sources.primary_source_catalog import PRIMARY_SOURCE_FAMILIES

def catalogue() -> dict[str, Any]:
    return {
      "domain_id":"SANATAN_DHARMA",
      "counts":{"vedas":len(VEDAS),"upanishads":len(UPANISHADS),"itihasa_works":len(ITIHASA_WORKS),
                "darshanas":len(DARSHANAS),"vedanta_schools":len(VEDANTA_SCHOOLS),
                "yoga_traditions":len(YOGA_TRADITIONS),"chronology_periods":len(CHRONOLOGY)},
      "sections":["texts.vedas","texts.upanishads","texts.itihasa","texts.puranas",
                  "philosophy.darshana","philosophy.vedanta_schools","practice.samskara",
                  "practice.yoga_traditions","history.chronology","sources.primary_source_catalog"]
    }

def search(query: str) -> list[dict[str, Any]]:
    needle=query.strip().casefold()
    if not needle: return []
    hits=[]
    catalogues=[
      ("veda",VEDAS),("upanishad",UPANISHADS),("itihasa",ITIHASA_WORKS),
      ("darshana",DARSHANAS),("vedanta_school",VEDANTA_SCHOOLS),
      ("yoga",YOGA_TRADITIONS)
    ]
    for kind,records in catalogues:
      for key,item in records.items():
        haystack=(key+" "+str(item)).casefold()
        if needle in haystack: hits.append({"kind":kind,"id":key,"record":item})
    return hits

__all__=["catalogue","search","get_veda","get_upanishad","search_upanishads","get_itihasa","get_darshana"]
