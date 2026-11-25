<?php
/** Provider identity and architecture boundary contract (metadata only). */
class SalesforceCoreContract {
    public static function identity(): array { return ['provider_id'=>'salesforce','ecosystem_id'=>'SALESFORCE-CORE-ECOSYSTEM','name'=>'Salesforce Core Ecosystem']; }
    public static function boundaries(): array { return ['metadata_only'=>true,'api_transport_in_core'=>false,'credential_storage'=>'EXTERNAL_SECRET_STORE_ONLY','live_connections_verified'=>false]; }
}
