# Include the Paho Mqtt https://pypi.org/project/paho-mqtt/ 
import paho.mqtt.client as mqtt
import time

# def IR_inside(client, userdata, message):
#     print("Received message '" + str(message.payload) + "' on topic '"
#        + message.topic + "' with QoS " + str(message.qos))
#     print("position 3")

# Printing publishers message
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

# client.message_callback_add("PEOPLE/Inside_IR", IR_inside)
# client.on_message = on_message

# ENTER CODE HERE Subtract people if IR_inside then IR_Outside

# ENTER CODE HERE Add if IR_outside then IR_inside

time.sleep(30)
client.loop_end()