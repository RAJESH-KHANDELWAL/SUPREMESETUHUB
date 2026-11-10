"""Oral-history collection and stewardship protocol."""
ORAL_HISTORY_PROTOCOL = {
 "before_interview":["Explain purpose, audience, storage, risks and future uses.","Obtain informed consent in a language the narrator understands.","Allow the narrator to set access restrictions and withdrawal terms.","Discuss names, sensitive events, sacred knowledge and third-party privacy."],
 "during_interview":["Use open questions and avoid leading prompts.","Record date, place, interviewer, language and recording conditions.","Distinguish direct memory, family transmission, hearsay and later interpretation.","Permit pauses, corrections and refusal to answer."],
 "after_interview":["Return transcript or summary for review where agreed.","Store consent record separately from public media.","Apply access controls and retention periods.","Preserve original recording and documented edits securely.","Credit or anonymise according to the narrator's wishes."],
 "required_metadata":["interview_id","narrator_consent_id","interviewer","date","location_precision","language","topics","access_level","embargo_until","reuse_permissions","transcript_status"],
 "non_negotiable":"No public release of restricted testimony or sacred/community-controlled knowledge without explicit authorisation."
}
def get_oral_history_protocol():
    return {key:list(value) if isinstance(value,list) else value for key,value in ORAL_HISTORY_PROTOCOL.items()}
