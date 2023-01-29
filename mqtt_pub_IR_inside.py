# Import the IR Sensor
import RPi.GPIO as GPIO

# Include the Paho Mqtt https://pypi.org/project/paho-mqtt/ 
import paho.mqtt.client as mqtt    
import time

# Init the Sensor pin 
sensor = 16
led = 18

# Init people
people = 0

# Init the Board pins
GPIO.setmode(GPIO.BOARD)
# Init the behavior of Sensor for input and LED for output
GPIO.setup(sensor, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

# Init the broker (api): comm b/w publisher & subscriber
mqttBroker = "mqtt.eclipseprojects.io"
# Inside Bus Sensor Publishing
client = mqtt.Client("Inside_IR")
# Connect to the Broker (Host Website)
client.connect(mqttBroker)

# Driver Program
try: 
    while True:

        # Reinit the Sensor and LED
        GPIO.setup(sensor, GPIO.IN)
        GPIO.setup(led, GPIO.OUT)

        # Sensor is off
        while GPIO.input(sensor) == GPIO.HIGH:
            # Keep the LED Off
            GPIO.output(led, False)

            time.sleep(.1)
            # Sensor is on
            while GPIO.input(sensor) == GPIO.LOW:
                # Keep the LED on
                print("1")
                GPIO.output(led, True)
                # Publish to People Topic
                people+=1
                # Publish to the topic People 
                client.publish("PEOPLE", people)
                print("Just published " + str(people) + " to topic PEOPLE")
                
                time.sleep(.5) 
finally:
   print("clean up") 
   GPIO.cleanup() # cleanup all GPIO 
        


