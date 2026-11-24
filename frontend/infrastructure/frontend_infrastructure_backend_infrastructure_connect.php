<?php
/** Frontend/backend Infrastructure structure and contract checker. */
final class FrontendInfrastructureBackendInfrastructureConnector {
    private const DOMAINS = ['backup','billing','cdn','containers','database','dns','domains','email','firewall','ftp','hosting','ipam','load_balancer','model','monitoring','network','object_storage','security','server','ssl','storage'];
    public function connect(): array {
        $frontend = __DIR__;
        $repo = dirname(dirname($frontend));
        $backend = $repo . '/backend/infrastructure';
        $ecosystem = $backend . '/global_ecosystem/global_infrastructure_ecosystem';
        $frontendChecks = [
            '__init__.py'=>is_file($frontend.'/__init__.py'),
            'manager.py'=>is_file($frontend.'/manager.py'),
            'manager.php'=>is_file($frontend.'/manager.php'),
            'global_ecosystem'=>is_dir($frontend.'/global_ecosystem')
        ];
        $backendChecks = [
            'backend_infrastructure_root'=>is_dir($backend),
            'backend_manager_py'=>is_file($backend.'/manager.py'),
            'backend_manager_php'=>is_file($backend.'/manager.php'),
            'backend_global_ecosystem_manager'=>is_file($backend.'/global_ecosystem/manager.py'),
            'backend_global_infrastructure_manager'=>is_file($ecosystem.'/manager.py')
        ];
        $domains = [];
        foreach (self::DOMAINS as $domain) {
            $domains[$domain] = is_dir($ecosystem.'/'.$domain);
        }
        $backendChecks['all_21_domains_present'] = !in_array(false,$domains,true);
        $frontendHealthy = !in_array(false,$frontendChecks,true);
        $backendHealthy = !in_array(false,$backendChecks,true);
        return [
            'name'=>'FRONTEND-BACKEND INFRASTRUCTURE CONNECTOR',
            'frontend'=>['checks'=>$frontendChecks,'healthy'=>$frontendHealthy],
            'backend'=>['checks'=>$backendChecks,'domain_checks'=>$domains,
                'expected_domain_count'=>count(self::DOMAINS),
                'present_domain_count'=>count(array_filter($domains)),
                'healthy'=>$backendHealthy],
            'connected'=>$frontendHealthy && $backendHealthy,
            'connection_type'=>'local structure and contract validation; no provider mutations'
        ];
    }
}
