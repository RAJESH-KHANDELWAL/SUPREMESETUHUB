<?php
/** Metadata reader for Adobe Express Storage; no Adobe API calls are performed. */
final class AdobeExpressStorage {
    public static function describe(): array {
        return ['ecosystem_id'=>'ADOBE_EXPRESS_STORAGE_ECOSYSTEM','provider'=>'ADOBE',
            'category'=>'express','implementation_state'=>'FOUNDATION_INITIALIZED',
            'external_connection_state'=>'NOT_CONFIGURED','storage_operations_enabled'=>false];
    }
}
