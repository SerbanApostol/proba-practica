from arrowhead_client.system.consumer import ConsumerSystem

temp_consumer = ConsumerSystem(
		'consumer_test',
		'localhost',
        	'1338',
        	'')#,
#        	'certificates/consumer_test.key',
#	        'certificates/consumer_test.crt')


temp_consumer.add_consumed_service('echo', method_name='GET')
temp_consumer.add_consumed_service('cpu_temp', method_name='POST')

connected=False
if __name__ == '__main__':
  while not connected:
    try:
      echo_response = temp_consumer.consume_service('echo')
      cpu_temp_response = temp_consumer.consume_service('cpu_temp')
      print(echo_response)
      print(cpu_temp_response)
      print('Done')
      connected=True
    except Exception as e:
      print(e)