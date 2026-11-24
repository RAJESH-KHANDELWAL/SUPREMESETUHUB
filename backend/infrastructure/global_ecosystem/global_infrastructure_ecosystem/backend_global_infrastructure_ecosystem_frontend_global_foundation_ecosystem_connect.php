<?php
/** Backend Global Infrastructure -> Frontend Global Foundation contract checker. */
final class BackendGlobalInfrastructureFrontendGlobalFoundationConnector
{
    private string $infrastructureRoot;
    private string $foundationRoot;

    public function __construct()
    {
        $this->infrastructureRoot = __DIR__;
        $repositoryRoot = dirname(__DIR__, 4);
        $this->foundationRoot = $repositoryRoot . '/frontend/foundation/global_ecosystem/global_foundation_ecosystem';
    }

    private function check(string $root): array
    {
        $required = ['__init__.py', 'manager.py', 'manager.php'];
        $checks = [];
        foreach ($required as $name) {
            $checks[$name] = is_file($root . '/' . $name);
        }
        return ['path' => $root, 'checks' => $checks, 'healthy' => !in_array(false, $checks, true)];
    }

    public function connect(): array
    {
        $infrastructure = $this->check($this->infrastructureRoot);
        $foundation = $this->check($this->foundationRoot);
        return [
            'name' => 'BACKEND GLOBAL INFRASTRUCTURE -> FRONTEND GLOBAL FOUNDATION',
            'infrastructure' => $infrastructure,
            'foundation' => $foundation,
            'connected' => $infrastructure['healthy'] && $foundation['healthy'],
            'connection_type' => 'filesystem contract check; not a runtime bridge',
        ];
    }
}
