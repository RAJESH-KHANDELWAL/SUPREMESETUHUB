"""Festival calendar schema; dates must be computed from verified local calendars."""
FESTIVAL_RECORD_FIELDS = (
 "festival_id","local_name","alternate_names","region","community",
 "calendar_system","tithi_or_date_rule","observance_window","rituals",
 "historical_sources","living_practice_sources","regional_variants",
 "accessibility_notes","publication_consent","last_verified"
)
CALENDAR_RULES = {
 "lunar":{"description":"Date may depend on lunar tithi, paksha, month and local sunrise rules.","must_record":["amanta_or_purnimanta convention where relevant","regional panchanga","sunrise rule","adhika masa effects"]},
 "solar":{"description":"Date may follow solar ingress or a regional solar calendar.","must_record":["calendar tradition","astronomical convention","regional observance"]},
 "fixed_civil":{"description":"Date is fixed on the civil calendar or institutional schedule.","must_record":["calendar authority","local timezone","official notification where relevant"]}
}
def get_calendar_rules():
    return {key:dict(value) for key,value in CALENDAR_RULES.items()}
