#Aline Garcia-Sanchez
#Isabel Fernandez
import paho.mqtt.client as mqtt
import time
def on_connect(client, userdata, flags, rc):
    print("Connected to RPI " + str(rc))
    
    client.subscribe("pi/ping")
    client.message_callback_add("pi/ping", on_message_from_RPI)

def on_message(client, userdata, msg):
    num = int(msg.payload.decode())
    num+=1

    client.publish("pi/pong", num)
def on_message_from_RPI(client, userdata, message):
    num = int(message.payload.decode())
    print("Priting pong: ", num)
    num+=1
    time.sleep(1)
    client.publish("pi/pong", num)
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("172.20.10.9", 1883, 60)

client.loop_forever()
