"""Direct-child category registry."""
from pathlib import Path
ROOT = Path(__file__).parent
CATEGORY_PACKAGES = [
    "global_communication_email_storage_ecosystem",
    "global_communication_messaging_storage_ecosystem",
    "global_communication_chat_storage_ecosystem",
    "global_communication_voice_storage_ecosystem",
    "global_communication_video_conferencing_storage_ecosystem",
    "global_communication_sms_storage_ecosystem",
    "global_communication_mms_storage_ecosystem",
    "global_communication_instant_messaging_storage_ecosystem",
    "global_communication_team_collaboration_storage_ecosystem",
    "global_communication_social_messaging_storage_ecosystem",
    "global_communication_contact_storage_ecosystem",
    "global_communication_calendar_storage_ecosystem",
    "global_communication_mailbox_storage_ecosystem",
    "global_communication_email_attachment_storage_ecosystem",
    "global_communication_message_archive_storage_ecosystem",
    "global_communication_call_recording_storage_ecosystem",
    "global_communication_voicemail_storage_ecosystem",
    "global_communication_meeting_recording_storage_ecosystem",
    "global_communication_transcription_storage_ecosystem",
    "global_communication_notification_storage_ecosystem",
    "global_communication_push_notification_storage_ecosystem",
    "global_communication_webhook_storage_ecosystem",
    "global_communication_fax_storage_ecosystem",
    "global_communication_rtc_storage_ecosystem",
    "global_communication_signal_data_storage_ecosystem",
    "global_communication_presence_status_storage_ecosystem",
    "global_communication_conversation_history_storage_ecosystem",
    "global_communication_media_sharing_storage_ecosystem",
    "global_communication_file_transfer_storage_ecosystem",
    "global_communication_encryption_key_storage_ecosystem"
]

def validate_category_packages():
    return [name for name in CATEGORY_PACKAGES if not (ROOT / name).is_dir()]
