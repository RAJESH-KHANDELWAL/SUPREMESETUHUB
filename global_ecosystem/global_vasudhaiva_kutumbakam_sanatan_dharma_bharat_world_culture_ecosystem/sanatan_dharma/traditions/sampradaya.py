"""Tradition and lineage directory schema for living Hindu traditions."""
SAMPRADAYA_RECORD_FIELDS = (
 "tradition_id","tradition_name","self_description","foundational_texts",
 "teachers_and_lineage","regional_centres","languages","worship_and_practice",
 "historical_period","living_community_sources","source_references",
 "consent_and_publication_status"
)
TRADITIONAL_STREAMS = {
 "vaishnava":{"name":"Vaishnava traditions","broad_focus":"Devotion to Vishnu and/or his avatars; multiple philosophical schools and regional lineages.","examples":["Sri Vaishnava","Madhva","Gaudiya","Vallabha","Ramanandi"],"caution":"Examples are not exhaustive and differ in theology, ritual and history."},
 "shaiva":{"name":"Shaiva traditions","broad_focus":"Traditions centred on Shiva, including philosophical, devotional, ascetic and tantric streams.","examples":["Shaiva Siddhanta","Kashmir Shaivism","Pashupata","Lingayat/Veerashaiva traditions"],"caution":"Community self-identification and historical scholarship should be recorded separately."},
 "shakta":{"name":"Shakta traditions","broad_focus":"Traditions centred on Devi/Shakti in diverse theological and ritual forms.","examples":["Sri Vidya","Kali traditions","regional Devi traditions"],"caution":"Some ritual materials are restricted; do not publish community-controlled or initiatory content without permission."},
 "smarta":{"name":"Smarta traditions","broad_focus":"A broad Brahmanical tradition associated with Smriti, Vedanta and multi-deity worship in some lineages.","examples":["Panchayatana worship traditions","Advaita-associated Smarta lineages"],"caution":"The label's use varies by region and historical context."}
}
def list_tradition_streams():
    return [{"id":key, **value} for key,value in TRADITIONAL_STREAMS.items()]
