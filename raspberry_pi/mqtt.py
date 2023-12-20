import time

import paho.mqtt.client as mqtt

from ip_address import get_ip_address

mqtt_ip = 'broker.emqx.io' 
mqtt_port = 1883
mqtt_topic = 'gateway/id/ip'

# wait time to retry a failed connection to the mqtt broker
connect_retry_wait_time = 3

client = mqtt.Client()

def connectToMQTTBroker():
    # keep retrying a connection if failed
    while client.connect(mqtt_ip, mqtt_port) != 0:
        print("Couldn't connect to the MQTT broker. Retrying...")
        # wait a while
        time.sleep(connect_retry_wait_time)

        print("Connected to the MQTT broker successfully...")
 
def publishUpdatedIpAddress():
    client.publish(mqtt_topic, get_ip_address())
    print("Published gateway IP...")
    client.disconnect()
