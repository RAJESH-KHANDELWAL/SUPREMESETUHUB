"""Comparative Vedanta school records; avoid sectarian ranking."""
VEDANTA_SCHOOLS = {
 "advaita":{"name":"Advaita Vedanta","key_teacher":"Adi Shankaracharya (major historical systematiser)","core_position":"Non-dual interpretation of the relation between Atman and Brahman","study_topics":["adhyasa","avidya","mahavakya interpretation","jnana and moksha"],"primary_texts":["Upanishads","Bhagavad Gita","Brahma Sutra"],"caution":"Historical Advaita includes pre-Shankara sources and later subtraditions."},
 "vishishtadvaita":{"name":"Vishishtadvaita Vedanta","key_teacher":"Ramanuja","core_position":"Qualified non-dualism; Brahman with auspicious attributes and real dependent selves and world","study_topics":["sharira-shariri relation","bhakti","prapatti","Sri Vaishnava theology"],"primary_texts":["Upanishads","Bhagavad Gita","Brahma Sutra","Sri Vaishnava works"]},
 "dvaita":{"name":"Dvaita Vedanta","key_teacher":"Madhva","core_position":"Real distinction between God, individual souls and matter","study_topics":["fivefold difference","Vishnu theology","bhakti","scriptural exegesis"],"primary_texts":["Upanishads","Bhagavad Gita","Brahma Sutra","Madhva's works"]},
 "achintya_bhedabheda":{"name":"Achintya Bhedabheda","key_teacher":"Chaitanya and Gaudiya Vaishnava acharyas","core_position":"Inconceivable simultaneous oneness and difference between the divine and dependent realities","study_topics":["bhakti","nama-sankirtana","rasa theology","Gaudiya commentarial tradition"],"primary_texts":["Bhagavata Purana","Bhagavad Gita","Gaudiya works"]}
}

def list_vedanta_schools():
    return [{"id":key, **value} for key,value in VEDANTA_SCHOOLS.items()]
