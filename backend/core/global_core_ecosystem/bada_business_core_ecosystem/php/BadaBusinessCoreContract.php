<?php
declare(strict_types=1);

namespace SupremeSetuHub\Core\BadaBusiness;

/** Language-neutral result contract for PHP consumers of Bada Business CORE. */
final class BadaBusinessCoreContract
{
    /**
     * @param array<string, mixed> $payload
     * @return array{success: bool, ecosystem_id: string, status: string, data: array, errors: array}
     */
    public static function normalize(array $payload): array
    {
        return [
            'success' => (bool)($payload['success'] ?? false),
            'ecosystem_id' => (string)($payload['ecosystem_id'] ?? 'BADA-BUSINESS-CORE-ECOSYSTEM'),
            'status' => (string)($payload['status'] ?? 'UNKNOWN'),
            'data' => is_array($payload['data'] ?? null) ? $payload['data'] : [],
            'errors' => is_array($payload['errors'] ?? null) ? array_values($payload['errors']) : [],
        ];
    }

    public static function assertCatalogOnly(string $operation): void
    {
        $blocked = ['REGISTRATION_SUBMIT', 'PAYMENT_PROCESS', 'ORDER_CREATE', 'REFUND', 'LEAD_SUBMIT'];
        if (in_array(strtoupper(trim($operation)), $blocked, true)) {
            throw new \LogicException('Provider transaction is not enabled in CORE.');
        }
    }
}
