<?php
declare(strict_types=1);
final class CohereRerankAuthenticationContext
{
    public function __construct(public readonly string $tenantId, public readonly string $actorId, public readonly string $credentialReference) {}
}
