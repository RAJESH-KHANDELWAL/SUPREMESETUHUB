<?php
declare(strict_types=1);

/**
 * PHP interoperability facade for the Bada Business transport capability adapter.
 * Python remains the canonical catalogue implementation.
 */
final class GlobalTransportBusinessCoreManager
{
    public static function normalizeResult(array $payload): array
    {
        foreach (['success', 'ecosystem_id', 'status'] as $required) {
            if (!array_key_exists($required, $payload)) {
                throw new InvalidArgumentException('TRANSPORT_BUSINESS_RESULT_MISSING_' . strtoupper($required));
            }
        }
        if ($payload['ecosystem_id'] !== 'GLOBAL-BADA-BUSINESS-TRANSPORT-LOGISTICS-SUPPLY-CHAIN-SERVICE-WORK-BUSINESS-CORE-ECOSYSTEM') {
            throw new InvalidArgumentException('TRANSPORT_BUSINESS_ECOSYSTEM_ID_MISMATCH');
        }
        return $payload;
    }
}
