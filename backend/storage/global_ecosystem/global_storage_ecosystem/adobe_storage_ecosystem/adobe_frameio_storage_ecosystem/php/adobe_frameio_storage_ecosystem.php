<?php
/** Metadata reader for Adobe Frame.io Storage; no Adobe API calls are performed. */
final class AdobeFrameioStorage {
    public static function describe(): array {
        return ['ecosystem_id'=>'ADOBE_FRAMEIO_STORAGE_ECOSYSTEM','provider'=>'ADOBE',
            'category'=>'frameio','implementation_state'=>'FOUNDATION_INITIALIZED',
            'external_connection_state'=>'NOT_CONFIGURED','storage_operations_enabled'=>false];
    }
}
