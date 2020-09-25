import paho.mqtt.client as mqtt # Import the MQTT client
import time # The time library is useful for delays
from subprocess import check_output # Function to return output of console commands
import json # Import json to send data as json file
import os

def try_connecting():
    global is_connected
    try:
      ourClient.connect("mqtt.beia-telemetrie.ro", 1883) # Connect to the MQTT broker
      is_connected=True
      tmp_arr=[]
      try:
        with open("/home/pi/Serban_Apostol/temporary.log", "r") as tmp:
          for x in tmp:
            tmp_arr.append(str(x))
        os.remove("/home/pi/Serban_Apostol/temporary.log")
      except:
        pass
      for x in tmp_arr:
        ourClient.publish("training/device/Serban_Apostol", str(x))
        time.sleep(0.1)
    except:
      print("No MQTT connection at the moment...")
      is_connected=False

is_connected=False
ourClient = mqtt.Client("proba_practica") # Create a MQTT client object
#try_connecting()
#ourClient.subscribe("training/device/Serban_Apostol") # Subscribe to the topic

while True:
  try_connecting()
  temp = str(check_output("/opt/vc/bin/vcgencmd measure_temp", shell=True)) # Get CPU temperature from bash
  info = {"CPU_temp":temp[7:11]}
  print(info)
  with open("/home/pi/Serban_Apostol/CPU_temp.log", "a") as log:
    log.write(str(info)+"\n")
  if is_connected:
    ourClient.publish("training/device/Serban_Apostol", json.dumps(info)) # Publish time and CPU temperature to MQTT broker
  else:
    with open("/home/pi/Serban_Apostol/temporary.log", "a") as tmp:
      tmp.write(json.dumps(info)+"\n")
  time.sleep(10) # Sleep for 10 seconds
