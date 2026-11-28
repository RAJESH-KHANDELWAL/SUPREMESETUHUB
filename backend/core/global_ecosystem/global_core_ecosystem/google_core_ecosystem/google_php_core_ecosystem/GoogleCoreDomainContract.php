<?php
declare(strict_types=1);

/**
 * Cross-language response contract for Google Core domain managers.
 * This validates metadata only; it never authorizes or executes provider APIs.
 */
final class GoogleCoreDomainContract
{
    private array $payload;

    private function __construct(array $payload)
    {
        $this->payload = $payload;
    }

    public static function fromArray(array $payload): self
    {
        foreach (['success', 'domain_id', 'status'] as $required) {
            if (!array_key_exists($required, $payload)) {
                throw new InvalidArgumentException('GOOGLE_CORE_DOMAIN_FIELD_REQUIRED: ' . $required);
            }
        }
        if (!is_bool($payload['success']) ||
            !is_string($payload['domain_id']) ||
            !is_string($payload['status'])) {
            throw new InvalidArgumentException('GOOGLE_CORE_DOMAIN_CONTRACT_TYPE_INVALID');
        }
        return new self(self::sanitize($payload));
    }

    public static function fromJson(string $json): self
    {
        $decoded = json_decode($json, true, 512, JSON_THROW_ON_ERROR);
        if (!is_array($decoded)) {
            throw new InvalidArgumentException('GOOGLE_CORE_DOMAIN_JSON_OBJECT_REQUIRED');
        }
        return self::fromArray($decoded);
    }

    public function toArray(): array
    {
        return $this->payload;
    }

    public function toJson(): string
    {
        return json_encode($this->payload, JSON_THROW_ON_ERROR | JSON_UNESCAPED_SLASHES);
    }

    private static function sanitize(array $value): array
    {
        $blocked = ['token', 'access_token', 'refresh_token', 'client_secret', 'api_key', 'secret', 'authorization', 'password'];
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
