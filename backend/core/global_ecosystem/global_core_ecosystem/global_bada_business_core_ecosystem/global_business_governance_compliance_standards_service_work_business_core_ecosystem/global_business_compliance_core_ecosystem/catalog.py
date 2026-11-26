"""Compliance obligation categories; taxonomy only, not legal advice."""
COMPLIANCE_CAPABILITIES = {
 "REGULATORY_OBLIGATIONS": ("obligation_registers","jurisdiction_and_effective_date_required"),
 "LICENSING_AND_PERMITS": ("licence_and_permit_metadata","issuing_authority_and_expiry_tracking"),
 "TAX_AND_STATUTORY_RECORDS": ("tax_registration_and_filing_metadata","professional_review_required"),
 "PRIVACY_AND_DATA_PROTECTION": ("privacy_and_processing_metadata","data_controller_context_required"),
 "LABOUR_AND_WORKPLACE": ("employment_obligation_metadata","jurisdiction_specific_review_required"),
 "AML_AND_FINANCIAL_CONTROLS": ("risk_and_control_metadata","regulated_entity_review_required"),
 "AUDIT_AND_DISCLOSURES": ("audit_and_disclosure_metadata","evidence_reference_required"),
 "CONSUMER_AND_MARKET_CONDUCT": ("consumer_protection_metadata","source_provenance_required")
}
