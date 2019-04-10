#!/usr/bin/python

import paho.mqtt.client as mqtt
import time

client =mqtt.Client("Zakir1")
broker= "broker.hivemq.com"
port=1883

def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))

def on_message(client, userdata, message):
    print("topic: "+message.topic+"	"+"payload: "+str(message.payload))

client.on_connect = on_connect
client.on_message = on_message



client.connect(broker, port, 60)
print "connecting to broker"

# client.loop_start() #start the loop


client.subscribe("device/light")
print "subscribing..."

client.publish("device/light","ON")
print "publishing..."

# time.sleep(4) # wait
# client.loop_stop() #stop the loop
client.loop_forever() # to maintain continuous network traffic flow with the broker


