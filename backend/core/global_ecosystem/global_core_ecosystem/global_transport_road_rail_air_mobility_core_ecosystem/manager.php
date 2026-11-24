<?php
declare(strict_types=1);

/**
 * PHP interoperability facade for transport CORE metadata results.
 * Python remains the canonical catalogue and orchestration implementation.
 */
final class GlobalTransportCoreManager
{
    public static function normalizeResult(array $payload): array
    {
        foreach (['success', 'ecosystem_id', 'status'] as $required) {
            if (!array_key_exists($required, $payload)) {
                throw new InvalidArgumentException('TRANSPORT_CORE_RESULT_MISSING_' . strtoupper($required));
            }
        }
        if ($payload['ecosystem_id'] !== 'GLOBAL-TRANSPORT-ROAD-RAIL-AIR-MOBILITY-CORE-ECOSYSTEM') {
            throw new InvalidArgumentException('TRANSPORT_CORE_ECOSYSTEM_ID_MISMATCH');
        }
        return $payload;
    }
}
