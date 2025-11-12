"""
MQTT Button Publisher - Sense HAT Joystick Integration

This script demonstrates how to use a Raspberry Pi's Sense HAT joystick
to publish messages to an MQTT broker. When the user presses the middle
button on the joystick, a message is sent to the MQTT topic on the
test.mosquitto.org broker. This is useful for creating IoT applications
where physical button presses trigger remote events.

Key Components:
- Sense HAT: Detects joystick button press events
- MQTT Client: Connects to a broker and publishes messages
- Event Loop: Continuously monitors for button presses
"""

import time
import paho.mqtt.client as mqtt
from sense_hat import SenseHat

# Initialise the Sense HAT
sense = SenseHat()

# MQTT connection details
MQTT_BROKER = "test.mosquitto.org"
MQTT_PORT = 1883
MQTT_TOPIC = "/fxwalsh/test"
MESSAGE = "Hello HDip Comp Sci 2025  \n A Button Press Event occurred on Frank's RPi"

# Set up MQTT client
client = mqtt.Client()

# Connect to the MQTT broker
client.connect(MQTT_BROKER, MQTT_PORT, 60)

# Start the client loop in a background thread
client.loop_start()
#Function to publish the message to the MQTT topic
def publish_message():
    client.publish(MQTT_TOPIC, MESSAGE)
    print("Message published:", MESSAGE)

# Main loop to detect joystick button press
try:
    while True:
        # Check if the middle button is pressed
        for event in sense.stick.get_events():
            if event.action == "pressed" and event.direction == "middle":
                publish_message()
        time.sleep(0.1)  # Small delay to reduce CPU usage
except KeyboardInterrupt:
    print("Exiting...")
finally:
    client.loop_stop()
    client.disconnect()
