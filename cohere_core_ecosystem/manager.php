<?php
declare(strict_types=1);

/**
 * Cohere Core PHP facade.
 * This facade validates metadata payload shape only; it does not call Cohere.
 */
final class CohereCoreManager
{
    public const ECOSYSTEM_ID = 'COHERE-CORE-ECOSYSTEM';
    public const STATUS = 'interface_only';

    public function status(): array
    {
        return [
            'success' => true,
            'ecosystem_id' => self::ECOSYSTEM_ID,
            'status' => self::STATUS,
            'capability_count' => 5,
            'live_provider_calls_enabled' => false,
            'api_calls_performed' => 0,
        ];
    }

    public function validateCapability(string $capability, array $payload): array
    {
        $allowed = ['classify', 'command', 'embed', 'rerank', 'tokenize'];
        $normalized = strtolower(trim($capability));
        if (!in_array($normalized, $allowed, true)) {
            return ['success' => false, 'status' => 'rejected', 'errors' => ['CAPABILITY_NOT_REGISTERED']];
        }

        foreach (['api_key', 'token', 'access_token', 'refresh_token', 'client_secret', 'password'] as $secretKey) {
            if (array_key_exists($secretKey, $payload)) {
                return ['success' => false, 'status' => 'rejected', 'errors' => ['SECRET_FIELD_NOT_ALLOWED']];
            }
        }

        return [
            'success' => true,
            'status' => 'CORE_CONTRACT_ONLY',
            'capability' => $normalized,
            'api_call_performed' => false,
        ];
    }
}
