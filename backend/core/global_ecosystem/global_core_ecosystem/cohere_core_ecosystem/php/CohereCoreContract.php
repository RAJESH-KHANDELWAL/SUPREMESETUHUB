<?php
declare(strict_types=1);

/**
 * Minimal PHP interoperability contract for Cohere CORE.
 * This class validates capability identifiers only; it never calls Cohere.
 */
final class CohereCoreContract
{
    private const CAPABILITIES = ['classify', 'command', 'embed', 'rerank', 'tokenize'];

    public function supports(string $capability): bool
    {
        return in_array(strtolower(trim($capability)), self::CAPABILITIES, true);
    }

    public function validate(array $request): array
    {
        $capability = strtolower(trim((string)($request['capability'] ?? '')));
        if (!$this->supports($capability)) {
            return ['ok' => false, 'status' => 'rejected', 'errors' => ['Unsupported Cohere capability']];
        }
        if (!isset($request['inputs']) || !is_array($request['inputs'])) {
            return ['ok' => false, 'status' => 'rejected', 'errors' => ['inputs must be an array']];
        }
        return ['ok' => true, 'status' => 'validated', 'capability' => $capability];
    }
}
