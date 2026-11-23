<?php
declare(strict_types=1);

/**
 * Thin PHP interoperability facade for Twilio Core metadata.
 * Python remains canonical. This class performs no Twilio API requests.
 */
final class TwilioCoreManager
{
    public const ECOSYSTEM_ID = 'TWILIO-CORE-ECOSYSTEM';
    public const STATUS = 'CORE_CATALOG_ONLY';

    public function status(): array
    {
        return [
            'success' => true,
            'ecosystem_id' => self::ECOSYSTEM_ID,
            'status' => self::STATUS,
            'api_transport_in_core' => false,
            'credentials_configured' => false,
            'live_connection_verified' => false,
        ];
    }
}
