import paho.mqtt.client as mqtt # Import the MQTT library
import time # The time library is useful for delays
from subprocess import check_output # Function to return output of console commands
import os

ourClient = mqtt.Client("proba_practica") # Create a MQTT client object
ourClient.connect("mqtt.beia-telemetrie.ro", 1883) # Connect to the MQTT broker
ourClient.subscribe("/training/device/Serban_Apostol/") # Subscribe to the topic

while True:
  temp = check_output("/opt/vc/bin/vcgencmd measure_temp", shell=True) # Get CPU temperature
  now = time.strftime("%d-%b-%Y,%H:%M:%S") # Get time
  info = now + ' ' + str(temp[5:9])[2:6]
  ourClient.publish("/training/device/Serban_Apostol/", info) # Publish time and CPU temperature to MQTT broker
  # Writing to local file
  filename = "/home/pi/Serban_Apostol/temp.txt"
  try:
    with open(filename, 'a') as f:
        f.write(info + '\n')
        f.close()
  except:
    print("File does not exist!")
  time.sleep(20) # Sleep for 20 seconds