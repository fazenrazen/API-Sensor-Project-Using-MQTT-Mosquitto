# Include the Paho Mqtt https://pypi.org/project/paho-mqtt/ 
import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    # print the payload of the message and decode
    print ("Recieved message: ", str(message.payload.decode("utf-8")))


mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Application")
client.connect(mqttBroker)

# Loop for 30 seconds subscribe to temp topic
client.loop_start()
client.subscribe("PEOPLE")
# Recieved message
client.on_message = on_message
time.sleep(30)
client.loop_end()