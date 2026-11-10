"""Samskara lifecycle-study framework with regional and textual variation."""
SAMSKARA_FRAMEWORK = {
 "meaning":"Samskara refers to rites of passage and formative rites; lists and counts differ across Grihya Sutras, communities and later manuals.",
 "commonly_studied": {
  "garbhadhana":"Conception-related rite in some textual classifications.",
  "pumsavana":"Prenatal rite described in certain Grihya and Smriti traditions; contemporary practice varies.",
  "simantonnayana":"Prenatal rite associated with the expectant mother; regional forms differ.",
  "jatakarma":"Birth-related rite.",
  "namakarana":"Naming ceremony.",
  "nishkramana":"First outing or presentation of the child outside the home.",
  "annaprashana":"First feeding of solid food.",
  "chudakarana":"First hair-cutting or tonsure rite in traditions that observe it.",
  "karnavedha":"Ear-piercing rite in some communities.",
  "vidyarambha":"Beginning of formal learning; regional names and practices vary.",
  "upanayana":"Initiatory rite associated with Vedic learning in particular traditions; eligibility and practice are historically and socially varied.",
  "samavartana":"Completion of studentship in textual frameworks.",
  "vivaha":"Marriage rites with substantial regional, linguistic and community diversity.",
  "antyeshti":"Funeral and post-death rites; customs vary widely."
 },
 "research_fields":["textual source","Grihya Sutra or regional manual","community followed","life stage","ritual sequence","language and mantra","gender and eligibility history","contemporary practice","consent and personal choice"],
 "caution":"Never prescribe a rite as universally mandatory. Document community context, living practice, individual choice and local authority."
}

def get_samskara_framework():
    return SAMSKARA_FRAMEWORK.copy()
