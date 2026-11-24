<?php
declare(strict_types=1);

/** Safe public domain metadata contract; no credentials or account data. */
final class FinanceServiceWorkBusinessDomainContract
{
    private function __construct(private array $data) {}

    public static function fromArray(array $payload): self
    {
        $domainId = trim((string)($payload['domain_id'] ?? ''));
        $name = trim((string)($payload['name'] ?? ''));
        if ($domainId === '' || $name === '') {
            throw new InvalidArgumentException('DOMAIN_ID_AND_NAME_REQUIRED');
        }
        $blocked = ['token', 'access_token', 'refresh_token', 'client_secret',
                    'api_key', 'secret', 'account_number', 'card_number', 'cvv'];
        $safe = array_diff_key($payload, array_flip($blocked));
        $safe['execution_enabled'] = false;
        return new self($safe);
    }

    public function toArray(): array { return $this->data; }
}
