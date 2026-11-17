"""Canonical storage domain taxonomy."""
DOMAINS={
 "OBJECT_STORAGE":("objects","buckets","object_versions","object_metadata"),
 "FILE_STORAGE":("files","directories","file_shares","file_metadata"),
 "USER_FILE_STORAGE":("drive_files","personal_files","sharing_metadata"),
 "BLOCK_STORAGE":("volumes","snapshots","block_devices"),
 "ARCHIVE":("cold_storage","archive_tiers","restore_metadata"),
 "BACKUP":("backup_jobs","backup_sets","restore_points"),
 "DEVICE_BACKUP":("device_backup_metadata","backup_status"),
 "FILE_SYNC":("sync_jobs","sync_state","conflict_metadata"),
 "APP_DATA_STORAGE":("application_data_metadata","app_backup_metadata")}
def list_domains(): return {k:tuple(v) for k,v in DOMAINS.items()}
