
    # API hierarchy
    {
        "ecosystem_id": "GLOBAL-API-ECOSYSTEM",
        "name": "GLOBAL API ECOSYSTEM",
        "ecosystem_type": "PLATFORM",
        "capabilities": ["API_CATALOG", "API_ROUTING", "INTEGRATIONS"],
    },
    {
        "ecosystem_id": "GLOBAL-BUSINESS-API-ECOSYSTEM",
        "name": "GLOBAL BUSINESS API ECOSYSTEM",
        "ecosystem_type": "API_DOMAIN",
        "capabilities": ["BUSINESS_APIS", "BUSINESS_INTEGRATIONS"],
        "parent_id": "GLOBAL-API-ECOSYSTEM",
    },
    {
        "ecosystem_id": "GLOBAL-NETWORK-MARKETING-DIRECT-SELLING-API-ECOSYSTEM",
        "name": "GLOBAL NETWORK MARKETING & DIRECT SELLING API ECOSYSTEM",
        "ecosystem_type": "API_DOMAIN",
        "capabilities": ["NETWORK_MARKETING", "DIRECT_SELLING"],
        "parent_id": "GLOBAL-BUSINESS-API-ECOSYSTEM",
    },
    {
        "ecosystem_id": "GLOBAL-AFFILIATE-MARKETING-API-ECOSYSTEM",
        "name": "GLOBAL AFFILIATE MARKETING API ECOSYSTEM",
        "ecosystem_type": "API_DOMAIN",
        "capabilities": ["AFFILIATE_TRACKING", "REFERRALS", "COMMISSIONS"],
        "parent_id": "GLOBAL-BUSINESS-API-ECOSYSTEM",
    },
    {
        "ecosystem_id": "GLOBAL-E-COMMERCE-API-ECOSYSTEM",
        "name": "GLOBAL E-COMMERCE API ECOSYSTEM",
        "ecosystem_type": "API_DOMAIN",
        "capabilities": ["PRODUCTS", "ORDERS", "CATALOGS"],
        "parent_id": "GLOBAL-BUSINESS-API-ECOSYSTEM",
    },
    {
        "ecosystem_id": "GLOBAL-CRM-LEAD-GENERATION-API-ECOSYSTEM",
        "name": "GLOBAL CRM & LEAD GENERATION API ECOSYSTEM",
        "ecosystem_type": "API_DOMAIN",
        "capabilities": ["CRM", "LEADS", "CONTACTS"],
        "parent_id": "GLOBAL-BUSINESS-API-ECOSYSTEM",
    },

    # Global language and translation
    {
        "ecosystem_id": "GLOBAL-LANGUAGE-ECOSYSTEM",
        "name": "GLOBAL LANGUAGE ECOSYSTEM",
        "ecosystem_type": "FUNCTIONAL",
        "capabilities": [
            "LANGUAGE_PREFERENCES",
            "LANGUAGE_DETECTION",
            "LOCALIZATION",
        ],
    },
    {
        "ecosystem_id": "GLOBAL-LANGUAGE-TRANSLATION-ECOSYSTEM",
        "name": "GLOBAL LANGUAGE TRANSLATION ECOSYSTEM",
        "ecosystem_type": "FUNCTIONAL",
        "capabilities": [
            "TEXT_TRANSLATION",
            "TRANSLATION_METADATA",
            "QUALITY_SIGNALS",
        ],
        "parent_id": "GLOBAL-LANGUAGE-ECOSYSTEM",
    },
    {
        "ecosystem_id": "GLOBAL-SPEECH-ECOSYSTEM",
        "name": "GLOBAL SPEECH ECOSYSTEM",
        "ecosystem_type": "FUNCTIONAL",
        "capabilities": ["SPEECH_RECOGNITION", "SPEECH_SYNTHESIS"],
        "parent_id": "GLOBAL-LANGUAGE-ECOSYSTEM",
    },
    {
        "ecosystem_id": "GLOBAL-SPEECH-TO-TEXT-ECOSYSTEM",
        "name": "GLOBAL SPEECH TO TEXT ECOSYSTEM",
        "ecosystem_type": "FUNCTIONAL",
        "capabilities": ["AUDIO_TRANSCRIPTION", "LANGUAGE_IDENTIFICATION"],
        "parent_id": "GLOBAL-SPEECH-ECOSYSTEM",
    },
    {
        "ecosystem_id": "GLOBAL-TEXT-TO-SPEECH-ECOSYSTEM",
        "name": "GLOBAL TEXT TO SPEECH ECOSYSTEM",
        "ecosystem_type": "FUNCTIONAL",
        "capabilities": ["SYNTHETIC_SPEECH", "VOICE_OUTPUT"],
        "parent_id": "GLOBAL-SPEECH-ECOSYSTEM",
    },
    {
        "ecosystem_id": "GLOBAL-SUBTITLE-ECOSYSTEM",
        "name": "GLOBAL SUBTITLE ECOSYSTEM",
        "ecosystem_type": "FUNCTIONAL",
        "capabilities": ["CAPTIONS", "MULTILINGUAL_SUBTITLES", "TIMECODES"],
        "parent_id": "GLOBAL-LANGUAGE-ECOSYSTEM",
    },

    # Global video and media
    {
        "ecosystem_id": "GLOBAL-VIDEO-ECOSYSTEM",
        "name": "GLOBAL VIDEO ECOSYSTEM",
        "ecosystem_type": "FUNCTIONAL",
        "capabilities": ["VIDEO_METADATA", "PLAYBACK", "MEDIA_WORKFLOWS"],
    },
    {
        "ecosystem_id": "GLOBAL-VIDEO-LANGUAGE-ECOSYSTEM",
        "name": "GLOBAL VIDEO LANGUAGE ECOSYSTEM",
        "ecosystem_type": "FUNCTIONAL",
        "capabilities": [
            "VIDEO_TRANSCRIPTION",
            "TRANSLATED_CAPTIONS",
            "AUDIO_TRACKS",
        ],
        "parent_id": "GLOBAL-VIDEO-ECOSYSTEM",
    },
    {
        "ecosystem_id": "GLOBAL-MEDIA-INGESTION-ECOSYSTEM",
        "name": "GLOBAL MEDIA INGESTION ECOSYSTEM",
        "ecosystem_type": "FUNCTIONAL",
        "capabilities": ["AUTHORIZED_UPLOAD", "IMPORT", "MEDIA_VALIDATION"],
        "parent_id": "GLOBAL-VIDEO-ECOSYSTEM",
    },
    {
        "ecosystem_id": "GLOBAL-VIDEO-ACCESSIBILITY-ECOSYSTEM",
        "name": "GLOBAL VIDEO ACCESSIBILITY ECOSYSTEM",
        "ecosystem_type": "FUNCTIONAL",
        "capabilities": [
            "CAPTIONS",
            "AUDIO_DESCRIPTION",
            "ACCESSIBILITY_PREFERENCES",
        ],
        "parent_id": "GLOBAL-VIDEO-ECOSYSTEM",
    },
