"""Language-family discovery for South Asia and the wider world."""
LANGUAGE_FAMILIES = {
 "indo_aryan":{"family":"Indo-Aryan","macro_family":"Indo-European","examples":["Hindi","Bengali","Punjabi","Marathi","Gujarati","Assamese","Odia","Sinhala","Nepali"],"caution":"Language, script, religion and ethnic identity are not interchangeable."},
 "dravidian":{"family":"Dravidian","examples":["Tamil","Telugu","Kannada","Malayalam","Tulu","Gondi","Kurukh","Brahui"],"caution":"Dravidian languages are internally diverse and extend beyond the four major literary languages."},
 "austroasiatic":{"family":"Austroasiatic","examples":["Santali","Mundari","Ho","Khasi","Nicobarese languages"],"caution":"Record community language names and dialect variation with speakers' guidance."},
 "sino_tibetan":{"family":"Sino-Tibetan / Trans-Himalayan (classification terminology varies)","examples":["Bodo","Meitei","many languages of Arunachal Pradesh and Himalayan regions"],"caution":"Classification of several languages is debated; do not force uncertain assignments."},
 "isolate_and_unclassified":{"family":"Language isolates and languages with disputed classification","examples":["Burushaski (often treated as an isolate)","other locally documented cases"],"caution":"Use current specialist linguistic sources for each classification."}
}
def list_language_families():
    return [{"id":key, **value} for key,value in LANGUAGE_FAMILIES.items()]
