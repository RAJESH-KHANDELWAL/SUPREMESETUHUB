"""Writing systems catalog, including Indic and global scripts."""
SCRIPTS = {
 "indic": ("Devanagari", "Bengali-Assamese", "Gujarati", "Gurmukhi", "Kannada", "Malayalam", "Meitei Mayek", "Odia", "Ol Chiki", "Tamil", "Telugu", "Perso-Arabic"),
 "global": ("Latin", "Arabic", "Cyrillic", "Han", "Hiragana", "Katakana", "Hangul", "Greek", "Hebrew", "Thai", "Lao", "Armenian", "Georgian", "Ethiopic"),
 "historic_and_specialized": ("Brahmi", "Grantha", "Tibetan", "Syriac", "Coptic", "other historic and specialist scripts"),
}
def get_writing_system_catalog() -> dict[str, tuple[str, ...]]:
 return dict(SCRIPTS)
