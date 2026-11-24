<?php
/** Metadata reader for Adobe Creative Cloud Assets Storage; no Adobe API calls are performed. */
final class AdobeCreativeCloudAssetsStorage {
    public static function describe(): array {
        return ['ecosystem_id'=>'ADOBE_CREATIVE_CLOUD_ASSETS_STORAGE_ECOSYSTEM','provider'=>'ADOBE',
            'category'=>'creative_cloud_assets','implementation_state'=>'FOUNDATION_INITIALIZED',
            'external_connection_state'=>'NOT_CONFIGURED','storage_operations_enabled'=>false];
    }
}
