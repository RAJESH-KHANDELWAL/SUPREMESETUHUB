"""Classification and standards identifiers; consumers verify current versions."""
CLASSIFICATION_SYSTEMS = {
 "ISIC":"International industry activity classification",
 "NAICS":"North American industry classification",
 "NIC":"National industrial classification (India)",
 "NACE":"European economic activity classification",
 "UNSPSC":"Products and services classification",
 "CPC":"Central product classification",
 "HS":"Harmonized commodity description and coding system",
 "ISCO":"International standard classification of occupations"
}
STANDARD_FAMILIES = {
 "QUALITY":("ISO_9001_FAMILY","quality_management"),
 "INFORMATION_SECURITY":("ISO_27000_FAMILY","information_security_management"),
 "ENVIRONMENT":("ISO_14000_FAMILY","environmental_management"),
 "OCCUPATIONAL_HEALTH_SAFETY":("ISO_45001","occupational_health_and_safety"),
 "BUSINESS_CONTINUITY":("ISO_22301","business_continuity_management"),
 "ANTI_BRIBERY":("ISO_37001","anti_bribery_management")
}
