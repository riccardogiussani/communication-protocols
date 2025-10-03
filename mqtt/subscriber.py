import paho, os
from paho.mqtt import client

client = client.Client(
        callback_api_version=client.CallbackAPIVersion.VERSION2
    )

# enable TLS for secure connection
client.tls_set(tls_version=paho.mqtt.client.ssl.PROTOCOL_TLS)
# set username and password
client.username_pw_set("admin", os.environ['MQTT_PWD'])
# connect to HiveMQ Cloud on port 8883 (default for MQTT)
client.connect(os.environ['MQTT_HOST'], 8883)

def on_message(client, userdata, msg):
    print("Received: ", str(msg.payload.decode()), " from topic: ", msg.topic)

client.subscribe("sensors/#", qos=1)

client.on_message = on_message

client.loop_forever()