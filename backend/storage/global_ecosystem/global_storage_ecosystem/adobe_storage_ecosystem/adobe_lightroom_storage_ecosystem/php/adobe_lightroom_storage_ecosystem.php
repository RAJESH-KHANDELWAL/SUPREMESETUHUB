<?php
/** Metadata reader for Adobe Lightroom Storage; no Adobe API calls are performed. */
final class AdobeLightroomStorage {
    public static function describe(): array {
        return ['ecosystem_id'=>'ADOBE_LIGHTROOM_STORAGE_ECOSYSTEM','provider'=>'ADOBE',
            'category'=>'lightroom','implementation_state'=>'FOUNDATION_INITIALIZED',
            'external_connection_state'=>'NOT_CONFIGURED','storage_operations_enabled'=>false];
    }
}
