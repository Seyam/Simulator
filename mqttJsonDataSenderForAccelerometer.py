import paho.mqtt.client as mqtt
from threading import Timer
import time
import json


client =mqtt.Client("Zakir123")
broker= "broker.hivemq.com"
port=1883

def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))

def on_message(client, userdata, message):
    print("topic: "+message.topic+"	"+"payload: "+str(message.payload))
    print('\n')


client.on_connect = on_connect  #attach the callback function to the client object 
client.on_message = on_message	#attach the callback function to the client object 

dummySensorData = {
 
  "accDataList" : [
      {
        "devId": "101",
        "X": "-0.11663",
        "Y": "1.9462",
        "Z": "-0.36802",
        "timestamp" : "29-01-2019 01:56:30"
      }
  ]
}




data = json.dumps(dummySensorData)
jsonData = json.loads(data)

print jsonData['accDataList']



client.connect(broker, port, 60)
print "connecting to broker"

# client.loop_start() #start the loop


client.subscribe("sensor/data1") #receive the same data that are being published
print "subscribed"


def publish():
    client.publish("sensor/data1", data )  # publish
    Timer(2.0, publish).start() # publish every 2 seconds


publish() # initialise the function

# time.sleep(4) # wait
# client.loop_stop() #stop the loop
client.loop_forever() # to maintain continuous network traffic flow with the broker


