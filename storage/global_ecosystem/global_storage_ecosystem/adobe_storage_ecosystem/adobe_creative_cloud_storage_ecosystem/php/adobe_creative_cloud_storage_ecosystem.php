<?php
/** Metadata reader for Adobe Creative Cloud Storage; no Adobe API calls are performed. */
final class AdobeCreativeCloudStorage {
    public static function describe(): array {
        return ['ecosystem_id'=>'ADOBE_CREATIVE_CLOUD_STORAGE_ECOSYSTEM','provider'=>'ADOBE',
            'category'=>'creative_cloud','implementation_state'=>'FOUNDATION_INITIALIZED',
            'external_connection_state'=>'NOT_CONFIGURED','storage_operations_enabled'=>false];
    }
}
