"""Yoga traditions map: distinguish classical, tantric, devotional and modern forms."""
YOGA_TRADITIONS = {
 "classical_ashtanga":{"name":"Patanjali's eight-limbed Yoga","source_context":"Yoga Sutra tradition","limbs":["yama","niyama","asana","pranayama","pratyahara","dharana","dhyana","samadhi"],"goal_context":"A disciplined path directed toward liberation/kaivalya in its classical philosophical setting."},
 "hatha":{"name":"Hatha Yoga","source_context":"Medieval yoga texts and living lineages","study_topics":["asana","pranayama","mudra","bandha","nada","subtle-body models"],"caution":"Hatha is not simply a synonym for modern fitness-oriented yoga."},
 "bhakti_yoga":{"name":"Bhakti Yoga","source_context":"Epic, Purana, devotional and sectarian traditions","study_topics":["devotion","remembrance","worship","chanting","service","surrender"]},
 "jnana_yoga":{"name":"Jnana Yoga","source_context":"Upanishadic and Vedanta traditions","study_topics":["inquiry","discrimination","self-knowledge","liberating insight"]},
 "karma_yoga":{"name":"Karma Yoga","source_context":"Especially influential through Bhagavad Gita interpretation","study_topics":["action","duty","non-attachment","offering","ethical responsibility"]},
 "modern_postural":{"name":"Modern postural yoga","source_context":"Modern global developments, with multiple Indian and international teachers and institutions","study_topics":["asana systems","physical culture","health discourse","global transmission"],"caution":"Study its modern history rather than projecting every contemporary class format into antiquity."}
}

def list_yoga_traditions():
    return [{"id":key, **value} for key,value in YOGA_TRADITIONS.items()]
