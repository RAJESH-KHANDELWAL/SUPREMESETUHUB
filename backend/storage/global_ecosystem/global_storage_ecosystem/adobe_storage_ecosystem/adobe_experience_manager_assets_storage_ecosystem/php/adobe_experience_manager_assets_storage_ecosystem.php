<?php
/** Metadata reader for Adobe Experience Manager Assets Storage; no Adobe API calls are performed. */
final class AdobeExperienceManagerAssetsStorage {
    public static function describe(): array {
        return ['ecosystem_id'=>'ADOBE_EXPERIENCE_MANAGER_ASSETS_STORAGE_ECOSYSTEM','provider'=>'ADOBE',
            'category'=>'experience_manager_assets','implementation_state'=>'FOUNDATION_INITIALIZED',
            'external_connection_state'=>'NOT_CONFIGURED','storage_operations_enabled'=>false];
    }
}
