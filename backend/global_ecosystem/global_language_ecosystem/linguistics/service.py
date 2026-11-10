"""Core linguistics research areas."""
AREAS = {
    "phonetics_and_phonology": ("speech sounds", "prosody", "phonemes"),
    "morphology": ("word formation", "inflection", "derivation"),
    "syntax": ("sentence structure", "grammar"),
    "semantics_and_pragmatics": ("meaning", "context", "discourse"),
    "sociolinguistics": ("language variation", "multilingual communities"),
    "corpus_linguistics": ("corpora", "annotation", "frequency analysis"),
    "computational_linguistics": ("tokenization", "parsing", "evaluation datasets"),
}


def get_linguistics_areas() -> dict[str, tuple[str, ...]]:
    return dict(AREAS)
