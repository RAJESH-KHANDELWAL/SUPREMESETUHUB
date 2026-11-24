<?php
declare(strict_types=1);

/** Stable PHP value contract for classification results. */
final class FinanceServiceWorkBusinessContract
{
    private function __construct(private array $data) {}

    public static function fromArray(array $payload): self
    {
        $ecosystemId = trim((string)($payload['ecosystem_id'] ?? ''));
        $status = trim((string)($payload['status'] ?? ''));
        if ($ecosystemId === '' || $status === '') {
            throw new InvalidArgumentException('ECOSYSTEM_ID_AND_STATUS_REQUIRED');
        }
        return new self([
            'success' => (bool)($payload['success'] ?? false),
            'ecosystem_id' => $ecosystemId,
            'status' => $status,
            'data' => is_array($payload['data'] ?? null) ? $payload['data'] : [],
            'errors' => is_array($payload['errors'] ?? null) ? $payload['errors'] : [],
            'execution_enabled' => false,
        ]);
    }

    public function toArray(): array { return $this->data; }
}
