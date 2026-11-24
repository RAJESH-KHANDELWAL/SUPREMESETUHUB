<?php
/** Metadata reader for Adobe Workfront Storage; no Adobe API calls are performed. */
final class AdobeWorkfrontStorage {
    public static function describe(): array {
        return ['ecosystem_id'=>'ADOBE_WORKFRONT_STORAGE_ECOSYSTEM','provider'=>'ADOBE',
            'category'=>'workfront','implementation_state'=>'FOUNDATION_INITIALIZED',
            'external_connection_state'=>'NOT_CONFIGURED','storage_operations_enabled'=>false];
    }
}
