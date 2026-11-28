<?php
/** Metadata reader for Adobe Document Cloud Storage; no Adobe API calls are performed. */
final class AdobeDocumentCloudStorage {
    public static function describe(): array {
        return ['ecosystem_id'=>'ADOBE_DOCUMENT_CLOUD_STORAGE_ECOSYSTEM','provider'=>'ADOBE',
            'category'=>'document_cloud','implementation_state'=>'FOUNDATION_INITIALIZED',
            'external_connection_state'=>'NOT_CONFIGURED','storage_operations_enabled'=>false];
    }
}
