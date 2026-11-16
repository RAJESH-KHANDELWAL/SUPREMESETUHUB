<?php
/** Metadata reader for Adobe Cloud Storage and Collaboration; no Adobe API calls are performed. */
final class AdobeCloudStorageAndCollaborationStorage {
    public static function describe(): array {
        return ['ecosystem_id'=>'ADOBE_CLOUD_STORAGE_AND_COLLABORATION_STORAGE_ECOSYSTEM','provider'=>'ADOBE',
            'category'=>'cloud_storage_and_collaboration','implementation_state'=>'FOUNDATION_INITIALIZED',
            'external_connection_state'=>'NOT_CONFIGURED','storage_operations_enabled'=>false];
    }
}
