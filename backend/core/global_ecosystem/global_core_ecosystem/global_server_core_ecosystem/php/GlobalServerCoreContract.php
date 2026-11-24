<?php
declare(strict_types=1);

/**
 * Language-neutral GLOBAL SERVER CORE result contract.
 *
 * Validates and sanitizes read-only metadata. It never provisions servers,
 * authenticates with providers, stores credentials or performs API transport.
 */
final class GlobalServerCoreContract
{
    private array $payload;

    private function __construct(array $payload)
    {
        $this->payload = $payload;
    }

    public static function fromArray(array $payload): self
    {
        foreach (['success', 'ecosystem_id', 'status'] as $required) {
            if (!array_key_exists($required, $payload)) {
                throw new InvalidArgumentException('SERVER_CORE_FIELD_REQUIRED: ' . $required);
            }
        }
        if (!is_bool($payload['success']) ||
            !is_string($payload['ecosystem_id']) ||
            !is_string($payload['status'])) {
            throw new InvalidArgumentException('SERVER_CORE_CONTRACT_TYPE_INVALID');
        }
        if ($payload['ecosystem_id'] !== 'GLOBAL-SERVER-CORE-ECOSYSTEM') {
            throw new InvalidArgumentException('SERVER_CORE_ECOSYSTEM_ID_INVALID');
        }
        return new self(self::sanitize($payload));
    }

    public static function fromJson(string $json): self
    {
        $decoded = json_decode($json, true, 512, JSON_THROW_ON_ERROR);
        if (!is_array($decoded)) {
            throw new InvalidArgumentException('SERVER_CORE_JSON_OBJECT_REQUIRED');
        }
        return self::fromArray($decoded);
    }

    public function toArray(): array
    {
        return $this->payload;
    }

    public function toJson(): string
    {
        return json_encode(
            $this->payload,
            JSON_THROW_ON_ERROR | JSON_UNESCAPED_SLASHES
        );
    }

    public function isLiveProviderConnectionVerified(): bool
    {
        return ($this->payload['live_provider_connections_verified'] ?? false) === true;
    }

    private static function sanitize(array $value): array
    {
        $blocked = [
            'token', 'access_token', 'refresh_token', 'client_secret',
            'api_key', 'secret', 'authorization', 'password', 'private_key',
            'credential', 'credentials',
        ];
        $clean = [];
        foreach ($value as $key => $item) {
            if (in_array(strtolower((string) $key), $blocked, true)) {
                continue;
            }
            if (is_array($item)) {
                $item = self::sanitize($item);
            }
            $clean[$key] = $item;
        }
        return $clean;
    }
}
