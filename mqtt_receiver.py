import paho.mqtt.client as mqtt # Import the MQTT library
from influxdb import InfluxDBClient

def messageFunction (client, userdata, message):
  message = str(message.payload.decode("utf-8")).split() #Convert message to string
  
  #Connecting to the database
  client = InfluxDBClient(host='localhost', port=8086)
  client.switch_database('Date_Proba_Practica')
  json_body = [
    {
      "measurement": "CPU_temp",
      "fields": {
        "time": message[0],
        "temperture(Celsius)": message[1]
      }
    }
  ]
  client.write_points(json_body)
  client.close()

ourClient = mqtt.Client("proba_practica") # Create a MQTT client object
ourClient.connect("mqtt.beia-telemetrie.ro", 1883) # Connect to the MQTT broker
ourClient.subscribe("/training/device/Serban_Apostol/") # Subscribe to the topic
ourClient.on_message = messageFunction # Attach the messageFunction to subscription
client = InfluxDBClient(host='localhost', port=8086)
dbs = str(client.get_list_database())
if 'Date_Proba_Practica' in dbs:
  client.create_database('Date_Proba_Practica')
client.close()
ourClient.loop_start() # Start the MQTT client

