"""Bhagavad Gita chapter map and study framework."""
GITA_CHAPTERS = [
("1","Arjuna Vishada Yoga","Arjuna's moral crisis on the battlefield"),
("2","Sankhya Yoga","Self, disciplined action, steadiness and wisdom"),
("3","Karma Yoga","Action, duty and non-attachment"),
("4","Jnana Karma Sannyasa Yoga","Knowledge, action, teaching lineage and avatara doctrine"),
("5","Karma Sannyasa Yoga","Renunciation and disciplined action"),
("6","Dhyana Yoga","Meditation, mind discipline and yogic practice"),
("7","Jnana Vijnana Yoga","Knowledge of the divine and its manifestations"),
("8","Akshara Brahma Yoga","Brahman, remembrance and the imperishable"),
("9","Raja Vidya Raja Guhya Yoga","The sovereign knowledge and divine presence"),
("10","Vibhuti Yoga","Divine manifestations and excellence"),
("11","Vishvarupa Darshana Yoga","The cosmic form"),
("12","Bhakti Yoga","Devotion and qualities of the devotee"),
("13","Kshetra Kshetrajna Vibhaga Yoga","Field, knower and discernment"),
("14","Gunatraya Vibhaga Yoga","Three gunas and transcendence"),
("15","Purushottama Yoga","Cosmic tree, self and supreme person"),
("16","Daivasura Sampad Vibhaga Yoga","Divine and destructive dispositions"),
("17","Shraddhatraya Vibhaga Yoga","Threefold faith and modes of conduct"),
("18","Moksha Sannyasa Yoga","Synthesis of duty, knowledge, devotion and liberation")
]
GITA_STUDY_FRAMEWORK = {
 "textual_location":"Bhishma Parva of the Mahabharata",
 "traditional_dialogue_speakers":["Krishna","Arjuna"],
 "chapter_count":18,
 "verse_count_note":"A commonly used received text has 700 verses; manuscript and edition details should be specified for critical work.",
 "interpretive_streams":["Advaita Vedanta","Vishishtadvaita Vedanta","Dvaita Vedanta","Bhakti traditions","modern reform and political readings","comparative philosophy"],
 "study_rules":["Read the whole chapter argument, not isolated quotations alone.","Identify the commentary tradition being used.","Separate Sanskrit wording, translation and interpreter's gloss.","Do not claim all schools interpret every verse identically."]
}
def chapter_map():
    return [{"chapter":int(n),"title":title,"focus":focus} for n,title,focus in GITA_CHAPTERS]
