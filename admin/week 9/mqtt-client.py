import paho.mqtt.client as mqtt

MQTT_BROKER = "test.mosquitto.org"
MQTT_PORT = 1883
MQTT_TOPIC = "/fxwalsh/test"
#MQTT_TOPIC = "/#"


def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print(f"Connected to {MQTT_BROKER}")
        client.subscribe(MQTT_TOPIC)
        print(f"Subscribed to {MQTT_TOPIC}")
    else:
        print(f"Connection failed with reason code: {reason_code}")


def on_message(client, userdata, message):
    payload = message.payload.decode("utf-8", errors="replace")
    print("\n--- Message received ---")
    print(f"Topic: {message.topic}")
    print(f"QoS: {message.qos}")
    print("Payload:")
    print(payload)
    print("------------------------")


def on_disconnect(client, userdata, disconnect_flags, reason_code, properties):
    print(f"Disconnected. Reason code: {reason_code}")


# Paho 2.x style client
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect

client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.loop_forever()