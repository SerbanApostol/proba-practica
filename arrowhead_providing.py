from typing import Dict
import arrowhead_client as ar

cpu_temp_provider = ar.ProviderSystem('cpu_temp_provider',
                                       'localhost',
                                       1337,
                                       '')#,
                                       #keyfile='certificates/time_provider.key',
                                       #certfile='certificates/time_provider.crt')

def echo(request) -> Dict[str, str]:
    return {'cpu_temp': str(check_output("/opt/vc/bin/vcgencmd measure_temp", shell=True))[7:11]}


#@cpu_temp_provider.add_provided_service('cpu_temp', '/cpu_temp', 'HTTP-SECURE-JSON', ['GET'])
def cpu_temp():
    return {'cpu_temp': str(check_output("/opt/vc/bin/vcgencmd measure_temp", shell=True))[7:11]}


if __name__ == '__main__':
    cpu_temp_provider.add_provided_service(
            service_definition='echo',
            service_uri='echo',
            interface='HTTP-SECURE-JSON',
            http_method='GET'#,
#            view_func=echo
    )
    
    cpu_temp_provider.add_provided_service(
            service_definition='cpu_temp',
            service_uri='/cpu_temp',
            interface='HTTP-SECURE-JSON',
            http_method='GET'#,
 #           view_func=cpu_temp
    )

    cpu_temp_provider.add_provided_service(
            'lambda',
            'lambda',
            'HTTP-SECURE-JSON',
            http_method='GET'#,
#            view_func=lambda: {'lambda': True}
    )

    print(cpu_temp_provider.certfile)
    cpu_temp_provider.run_forever()
