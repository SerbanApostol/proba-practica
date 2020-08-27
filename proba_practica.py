import paho.mqtt.client as mqtt # Import the MQTT client
import time # The time library is useful for delays
from subprocess import check_output # Function to return output of console commands
import json # Import json to send data as json file

def try_connecting():
  is_connected=False
  while not is_connected:
    try:
      ourClient.connect("mqtt.beia-telemetrie.ro", 1883) # Connect to the MQTT broker
      is_connected=True
    except:
      print("No MQTT connection at the moment...")
      time.sleep(2)

is_connected=False
ourClient = mqtt.Client("proba_practica") # Create a MQTT client object
try_connecting()
ourClient.subscribe("training/device/Serban_Apostol") # Subscribe to the topic
ourClient.on_disconnect=try_connecting

while True:
  temp = check_output("/opt/vc/bin/vcgencmd measure_temp", shell=True) # Get CPU temperature from bash
  now = time.strftime("%d-%b-%Y,%H:%M:%S") # Get time
  info = {"CPU_temp":temp[5:9]}
  if not is_connected:
    ourClient.publish("training/device/Serban_Apostol", json.dumps(info)) # Publish time and CPU temperature to MQTT broker
  time.sleep(10) # Sleep for 10 seconds
