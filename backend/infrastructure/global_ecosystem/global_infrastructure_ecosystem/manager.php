<?php
/** Structural health manager for the Global Infrastructure Ecosystem. */
final class BackendGlobalInfrastructureEcosystemManager {
    public const NAME = 'BACKEND GLOBAL INFRASTRUCTURE ECOSYSTEM';
    public const VERSION = '1.1.0';
    private const DOMAINS = ['backup','billing','cdn','containers','database','dns','domains','email','firewall','ftp','hosting','ipam','load_balancer','model','monitoring','network','object_storage','security','server','ssl','storage'];
    public function health(): array {
        $root = __DIR__;
        $backendRoot = dirname(dirname(dirname($root)));
        $required = ['README.md','__init__.py','catalog.py','capabilities.py','governance.py','integrations.py','models.py','providers.py','registry.py','schemas.py','service.py','services.py','structure.py','manager.py','manager.php'];
        $checks = [];
        foreach ($required as $name) { $checks['root_file_' . $name] = is_file($root . '/' . $name); }
        foreach (['__init__.py','controller.py','repository.py','service.py','hostinger_catalog.py'] as $name) {
            $checks['canonical_module_' . $name] = is_file($root . '/modules/' . $name);
        }
        $checks['core_integration_adapter'] = is_file($root . '/integrations/core/__init__.py');
        $checks['global_core_integration_adapter'] = is_file($root . '/integrations/global_core_ecosystem/__init__.py');
        foreach (self::DOMAINS as $domain) {
            $checks['domain_' . $domain] = is_dir($root . '/' . $domain) && is_file($root . '/' . $domain . '/__init__.py');
            $checks['domain_global_ecosystem_' . $domain] = is_dir($root . '/' . $domain . '/global_ecosystem');
        }
        $checks['backend_global_hostinger_api'] = is_file($backendRoot . '/global_ecosystem/global_hosting_ecosystem/hostinger_api.py');
        $checks['backend_global_nsfwinfra'] = is_file($backendRoot . '/global_ecosystem/nsfwinfra_ecosystem/nsfwinfra.py');
        $healthy = !in_array(false, $checks, true);
        $present = 0;
        foreach (self::DOMAINS as $domain) { if ($checks['domain_' . $domain]) { $present++; } }
        return ['name'=>self::NAME,'version'=>self::VERSION,
                'status'=>$healthy?'READY':'INCOMPLETE',
                'expected_domain_count'=>count(self::DOMAINS),'present_domain_count'=>$present,
                'checks'=>$checks,'healthy'=>$healthy,'provider_operations_enabled'=>false];
    }
}
