import paho.mqtt.client as mqtt
from threading import Timer
import time
import json


client =mqtt.Client("Zakir1")
broker= "broker.hivemq.com"
port=1883

def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))

def on_message(client, userdata, message):
    print("topic: "+message.topic+"	"+"payload: "+str(message.payload))
    print('\n')


client.on_connect = on_connect  #attach the callback function to the client object 
client.on_message = on_message	#attach the callback function to the client object 

tempSensorData={
  "msg": "advData",
  "gmac": "D03304000182",
  "obj": [
      {
      "dmac": "8131000A33DD",
      "rssi": "-83",
      "data1": "0201060303AAFE1116AAFE20000B7111000084610900D67B62"
    },
    {
      "dmac": "3904000A33DD",
      "rssi": "-70",
      "data1": "0201060303AAFE1116AAFE20000B17150000592D5D00599354"
    }
  ],
  "seq": 2896
}


dt = {"light" : "ON"}

data = json.dumps(dt)

client.connect(broker, port, 60)
print ("connecting to broker")

# client.loop_start() #start the loop


client.subscribe("sensor/data") #receive the same data that are being published
print ("subscribed")


def publish():
    client.publish("sensor/data", data )  # publish
    Timer(2.0, publish).start() # publish every 2 seconds


publish() # initialise the function

# time.sleep(4) # wait
# client.loop_stop() #stop the loop
client.loop_forever() # to maintain continuous network traffic flow with the broker


