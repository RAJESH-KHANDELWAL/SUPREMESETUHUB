"""Evidence-aware knowledge base for Vasudhaiva Kutumbakam.

The module distinguishes textual evidence, traditional interpretation, modern
application and unresolved historical questions. It deliberately does not
invent an individual author, a precise composition date or a geographic
location for the Maha Upanishad.
"""
from typing import Any, Dict, Tuple

KNOWLEDGE_ID = "VASUDHAIVA_KUTUMBAKAM_PRIMARY_KNOWLEDGE"

CORE_IDEA: Dict[str, Any] = {
    "sanskrit": "वसुधैव कुटुम्बकम्",
    "transliteration": "vasudhaiva kuṭumbakam",
    "concise_translation": "The whole earth is one family.",
    "expanded_translation": (
        "For people of generous or noble character, the whole earth is one family; "
        "the narrow-minded divide people into 'one of ours' and 'not one of ours'."
    ),
    "word_etymology": {
        "vasudhā": "earth; the world",
        "eva": "indeed; emphatic particle, contracted in the compound as -aiva",
        "kuṭumbakam": "family or household",
    },
    "ethical_scope": (
        "A call to widen moral concern beyond narrow in-group boundaries, "
        "cultivate generosity, and treat human relationships with dignity."
    ),
}

PRIMARY_TEXT: Dict[str, Any] = {
    "work": "Mahā Upaniṣad (also written Mahopaniṣad)",
    "location_in_work": "Chapter 6; commonly cited as verse 6.72",
    "numbering_note": (
        "Verse numbering can vary between editions and citation traditions; "
        "some references discuss the surrounding passage as 6.71–73. "
        "Always identify the edition used when publishing a critical citation."
    ),
    "sanskrit_devanagari": (
        "अयं बन्धुरयं नेति गणना लघुचेतसाम् ।\n"
        "उदारचरितानां तु वसुधैव कुटुम्बकम् ॥"
    ),
    "iast": (
        "ayaṃ bandhur ayaṃ neti gaṇanā laghu-cetasām |\n"
        "udāra-caritānāṃ tu vasudhaiva kuṭumbakam ||"
    ),
    "plain_meaning": (
        "The calculation 'this person is a relative/friend, and that person is not' "
        "belongs to narrow-minded people; for those of generous character, "
        "the whole earth is one family."
    ),
    "textual_context": (
        "The verse occurs in a philosophical and spiritual discussion in the "
        "sixth chapter. It describes the expansive outlook associated with "
        "noble character and spiritual insight. It should not be detached from "
        "its textual setting when explaining its original meaning."
    ),
    "variant_reading": {
        "work": "Hitopadeśa",
        "common_opening": "अयं निजः परो वेति गणना लघुचेतसाम्",
        "iast_opening": "ayaṃ nijaḥ paro veti gaṇanā laghu-cetasām",
        "note": (
            "A related form circulates in the Hitopadeśa and later quotation "
            "traditions. Do not silently combine readings from different works "
            "and present them as one diplomatic transcription."
        ),
    },
}

HISTORICAL_QUESTIONS: Dict[str, Dict[str, Any]] = {
    "what_is_it": {
        "answer": (
            "A Sanskrit ethical-philosophical expression meaning that the earth "
            "or world is one family. In its verse context it contrasts narrow "
            "in-group thinking with generous, expansive character."
        ),
        "confidence": "high",
        "basis": "The wording and its placement in the Maha Upanishad passage.",
    },
    "who_created_or_authored_it": {
        "answer": (
            "No historically verified individual author or inventor is known. "
            "The Maha Upanishad is a traditional sacred text transmitted through "
            "a textual and oral tradition; assigning this line to a named modern "
            "individual would be unsupported."
        ),
        "confidence": "high_for_no_verified_individual; author_identity_unknown",
        "basis": "The cited textual tradition does not establish a verifiable named author.",
    },
    "when_was_it_composed": {
        "answer": (
            "The exact date of composition of the Maha Upanishad, and the date "
            "when this particular verse first took shape, are not securely known. "
            "Do not assign a specific year or century without edition-specific "
            "and scholarly evidence."
        ),
        "confidence": "high_that_exact_date_is_unsettled",
        "basis": "Textual dating is a scholarly question; manuscript and transmission histories matter.",
    },
    "where_was_it_composed": {
        "answer": (
            "A precise place of composition has not been established by reliable "
            "evidence. The text belongs to the Sanskrit Upanishadic literary "
            "tradition of India, but that broad cultural setting is not proof "
            "of a particular city, ashram, kingdom or geographic site."
        ),
        "confidence": "high_that_precise_location_is_unestablished",
        "basis": "No securely established colophon or historical record identifies a place of composition.",
    },
    "why_was_it_taught": {
        "answer": (
            "Within its philosophical setting, the verse teaches that spiritual "
            "maturity and noble conduct overcome narrow distinctions between "
            "one's own people and outsiders. It encourages a wider moral outlook "
            "and generosity of character."
        ),
        "confidence": "interpretation_grounded_in_textual_context",
        "basis": "The verse itself contrasts laghu-cetas (narrow-minded) with udāra-carita (noble/generous in conduct).",
    },
    "how_was_it_transmitted": {
        "answer": (
            "Through the preservation, recitation, copying, teaching and "
            "commentarial transmission of Sanskrit texts. The exact chain of "
            "transmission for this individual verse cannot be reconstructed "
            "from the phrase alone."
        ),
        "confidence": "general_transmission_context; verse_specific_chain_unknown",
        "basis": "Traditional textual transmission and surviving textual witnesses.",
    },
}

INTERPRETIVE_LAYERS: Dict[str, Any] = {
    "original_textual_layer": (
        "Read the verse in the Maha Upanishad passage and explain its contrast "
        "between narrow-minded classification and generous character."
    ),
    "ethical_layer": (
        "Extend fairness, empathy, hospitality, compassion and responsibility "
        "beyond one's immediate group."
    ),
    "social_layer": (
        "Support peaceful coexistence and dialogue while respecting differences "
        "in language, community, belief, history and identity."
    ),
    "global_contemporary_layer": (
        "The idea can inspire international cooperation and shared responsibility "
        "for humanity and the planet. This is a contemporary application, not "
        "a claim that the ancient verse prescribed today's institutions or policies."
    ),
    "limits_and_cautions": (
        "One-family language must not be used to erase cultural differences, "
        "override community consent, excuse injustice, or claim that every "
        "tradition has identical beliefs. Respect includes boundaries, rights "
        "and accountability."
    ),
}

COMMON_MISATTRIBUTIONS: Tuple[Dict[str, str], ...] = (
    {
        "claim": "The exact phrase is a Rigveda mantra.",
        "correction": (
            "The commonly cited textual source for this exact phrase is the "
            "Maha Upanishad; do not label it Rigvedic without a specific verified citation."
        ),
    },
    {
        "claim": "The exact phrase occurs in the Bhagavad Gita.",
        "correction": (
            "The phrase is commonly cited from the Maha Upanishad. The Gita has "
            "related teachings about seeing the self in all beings, but that is "
            "not the same as claiming this exact phrase appears there."
        ),
    },
    {
        "claim": "A known historical person invented it in a known year and city.",
        "correction": (
            "No reliable evidence establishes a single inventor, exact year or "
            "precise place of composition."
        ),
    },
    {
        "claim": "It means all cultures, religions and communities are identical.",
        "correction": (
            "It expresses expansive kinship and ethical regard; it does not "
            "erase plural identities, disagreements or community rights."
        ),
    },
)

APPLICATIONS: Dict[str, Tuple[str, ...]] = {
    "personal_life": (
        "Treat people with dignity regardless of background.",
        "Practise empathy, generosity, hospitality and responsible conduct.",
        "Resolve disagreement without dehumanising others.",
    ),
    "community": (
        "Build inclusive dialogue and mutual aid.",
        "Preserve local identity while learning respectfully from others.",
        "Seek consent and attribution when documenting community knowledge.",
    ),
    "education": (
        "Teach the original Sanskrit, translation, source and historical uncertainty.",
        "Compare textual evidence with later interpretations.",
        "Help learners distinguish primary sources from modern slogans.",
    ),
    "global_cooperation": (
        "Encourage cooperation on shared human and environmental challenges.",
        "Respect sovereignty, cultural diversity, rights and reciprocal responsibilities.",
        "Translate ideals into accountable actions rather than unsupported claims.",
    ),
}

SOURCES: Tuple[Dict[str, str], ...] = (
    {
        "title": "Government of India, Press Information Bureau: address explaining Vasudhaiva Kutumbakam",
        "url": "https://www.pib.gov.in/PressReleaseIframePage.aspx?PRID=1591742&lang=2&reg=48",
        "use": "Official explanation of the phrase, word components and Maha Upanishad VI.72 reference.",
        "source_type": "official_government",
    },
    {
        "title": "University of Calicut, School of Distance Education: Indian Heritage and Plurality of Cultures",
        "url": "https://sde.uoc.ac.in/sites/default/files/sde_videos/SLM-His-INDIAN%20HERITAGE%20AND%20PLURALITY%20OF%20CULTURES.pdf",
        "use": "Educational discussion of the phrase and its Maha Upanishad textual reference.",
        "source_type": "university_educational_material",
    },
    {
        "title": "Signe Cohen, The Classical Upanishads: A Guide, chapter 'Dating and Authorship' (Oxford University Press, 2024)",
        "url": "https://doi.org/10.1093/oso/9780197654156.003.0003",
        "use": "Scholarly method and caution for dating and authorship of Upanishadic texts generally; not a precise date for the Maha Upanishad.",
        "source_type": "academic_book",
    },
    {
        "title": "Vivekananda International Foundation, Vasudhaiva Kutumbakam conference proceedings",
        "url": "https://www.vifindia.org/sites/default/files/Vasudhaiva-Kutumbakam-Conference-Proceedings.pdf",
        "use": "Contextual discussion of the verse in relation to spiritual philosophy and contemporary interpretation.",
        "source_type": "research_conference_proceedings",
    },
)

EVIDENCE_RULES: Tuple[str, ...] = (
    "Never invent a named author, exact composition year or exact composition location.",
    "Keep Sanskrit text, transliteration and translation as separate fields.",
    "Record the edition and verse numbering used; numbering may vary.",
    "Label modern applications as interpretations or applications, not as literal ancient prescriptions.",
    "Distinguish primary text, scholarly interpretation, traditional belief and contemporary opinion.",
    "A URL in SOURCES is a research lead; verify the page and edition before making a critical scholarly claim.",
)

def get_core_idea() -> Dict[str, Any]:
    """Return the canonical meaning, wording and word-level explanation."""
    return CORE_IDEA.copy()

def get_primary_text() -> Dict[str, Any]:
    """Return the cited Sanskrit passage, translation and textual context."""
    return PRIMARY_TEXT.copy()

def answer_historical_question(question_key: str) -> Dict[str, Any]:
    """Answer one of the documented historical questions without filling gaps by guesswork."""
    try:
        return HISTORICAL_QUESTIONS[question_key].copy()
    except KeyError as exc:
        raise KeyError(
            f"Unknown question '{question_key}'. Available: {', '.join(HISTORICAL_QUESTIONS)}"
        ) from exc

def get_complete_knowledge() -> Dict[str, Any]:
    """Return the complete structured knowledge record for learning interfaces and APIs."""
    return {
        "knowledge_id": KNOWLEDGE_ID,
        "core_idea": CORE_IDEA,
        "primary_text": PRIMARY_TEXT,
        "historical_questions": HISTORICAL_QUESTIONS,
        "interpretive_layers": INTERPRETIVE_LAYERS,
        "common_misattributions": COMMON_MISATTRIBUTIONS,
        "applications": APPLICATIONS,
        "sources": SOURCES,
        "evidence_rules": EVIDENCE_RULES,
    }

def search_knowledge(keyword: str) -> Tuple[Dict[str, Any], ...]:
    """Simple deterministic keyword discovery over question keys and answers."""
    needle = keyword.strip().casefold()
    if not needle:
        return ()
    matches = []
    for key, item in HISTORICAL_QUESTIONS.items():
        haystack = f"{key} {item['answer']} {item['basis']}".casefold()
        if needle in haystack:
            matches.append({"topic": key, **item})
    return tuple(matches)
