<?php
declare(strict_types=1);

/** Identity/credential reference contract. Actual secrets are injected by secure runtime. */
final class CohereClassifyAuthenticationContext
{
    public function __construct(
        public readonly string $tenantId,
        public readonly string $actorId,
        public readonly string $credentialReference
    ) {}
}
