import datetime
import time
import random

import paho.mqtt.client as mqtt


def generate(whatsapp_count , voice_count , Email_count  ):
    max=7000
    stopflag = 0
    y= random.randint(300, 500)
    if whatsapp_count+y >max:
        whatsapp_count=max-1
    else:
        whatsapp_count = whatsapp_count + y

    y = random.randint(300, 500)


    if voice_count + y > max:
        voice_count = max-1
    else:
        voice_count = voice_count + y


    y = random.randint(300, 500)
    if Email_count + y > max:
        Email_count = max-1
    else:
        Email_count = Email_count + y

    sales_count=whatsapp_count+voice_count+Email_count

    if sales_count==(max-1)*3:
        stopflag=1

    return whatsapp_count,voice_count,Email_count,sales_count ,stopflag

def on_connect(client, userdata, flags, rc,dummy):
    print('Connected with result code '+str(rc))
    client.subscribe("cmd/one")
    # client.subscribe('testtopic/ABC')
def on_message(client, userdata, msg):
    print("received message on topic "+msg.topic+"content: "+str(msg.payload))

def on_publish (client, obj, mid, reason_code, properties):
    pass

client = mqtt.Client(client_id="x"  , callback_api_version=mqtt.CallbackAPIVersion.VERSION2)


client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish
counter=1
while True:
    try:

        # brokerIP="192.168.20.4"
        brokerIP="13.51.206.43"
        # brokerIP = "172.16.21.177"
        Topic_name="cmd/one"
        # Topic_name = "testtopic/one"
        # Topic_name="newtopic"

        # Topic_name="basicMQTT1"
        print("connecting . . . .")
        # client.username_pw_set("splunk","splunk")
        client.username_pw_set("x", "x")
        client.connect(brokerIP, 1883, 60)
        client.loop_start()
        # client.connect(brokerIP, 8883, 60)
        print("connected to broker")
        break
    except Exception as E:
        print(str(E))
        time.sleep(5*counter)
        counter+=1

# Publish a message
# for x in range(3):
sales_count=0
whatsapp_count=0
voice_count=0
Email_count=0
while True:
    counter+=1
    sales_count+=1
    whatsapp_count+=1
    voice_count+=1
    Email_count+=1
    stopflag=False
    # whatsapp_count , voice_count , Email_count , sales_count  , stopflag= generate(whatsapp_count , voice_count , Email_count )
    msg = ('{ "w":[ { "tag":"sales_count", "value":'+str(sales_count)+'} , { "tag":"whatsapp_count", "value":'+str(whatsapp_count)+'} , { "tag":"Email_count", "value":'+str(Email_count)+'} , { "tag":"voice_count", "value":'+str(voice_count)+'}], "ts":"' + str(time.ctime()) + '" }')
    # result = client.publish(Topic_name, payload=(msg), qos=0)
    # print(str(result) + 'published message on topic {' + Topic_name + '} content:' + str(msg))
    msg = ('"sales_count":'+str(sales_count)+'}')

    result = client.publish("data/device_id", payload=(msg), qos=0)
    print(str(result) + 'published message on topic {test/hello} content:' + str(msg))

    time.sleep(5)
    if stopflag:
        break


