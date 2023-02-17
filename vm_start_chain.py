#Aline Garcia-Sanchez
#Isabel Fernandez
import paho.mqtt.client as mqtt
import time 
from datetime import datetime
import socket
def on_connect(client, userdata, flags, rc):
    print("Connected to RPI with result code " + str(rc))

    client.subscribe("pi/pong")
    client.message_callback_add("pi/pong", on_message_from_RPI)
def on_message(client, userdata, msg):
    num = int(msg.payload.decode())
    print("Print num: ", num)
    num+=1
    client.publish("pi/ping", num)
def on_message_from_RPI(client, userdata, msg):
    num = int(msg.payload.decode())
    print("Printing num: ", num)
    num+=1
    time.sleep(1)
    client.publish("pi/ping", num)
if __name__ == '__main__':
    ip_address = "172.20.10.9"
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(host="172.20.10.9", port=1883, keepalive=60)

    client.loop_start()
    time.sleep(1)

    num = 0;
    client.publish("pi/ping", num)
    print("Publishing ping")

    while True:
        pass
