<?php
declare(strict_types=1);

/** Identity and opaque credential-reference contract; no secrets are stored. */
final class CohereEmbedAuthenticationContext
{
    public function __construct(
        public readonly string $tenantId,
        public readonly string $actorId,
        public readonly string $credentialReference
    ) {}
}
