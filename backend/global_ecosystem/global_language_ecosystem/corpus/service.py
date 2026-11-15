"""Metadata checks for text and speech corpora."""
def validate_corpus_metadata(*, name: str, language_code: str, source_description: str,
                             rights_confirmed: bool, personal_data_reviewed: bool) -> tuple[str, ...]:
 issues=[]
 if not name.strip(): issues.append("name_required")
 if not language_code.strip(): issues.append("language_code_required")
 if not source_description.strip(): issues.append("source_description_required")
 if not rights_confirmed: issues.append("dataset_rights_unconfirmed")
 if not personal_data_reviewed: issues.append("personal_data_review_required")
 return tuple(issues)
