import time

from mqtt import connectToMQTTBroker,publishUpdatedIpAddress
 
# wait time to publish an updated IP adress
publish_wait_time = 3

while True:
    connectToMQTTBroker()
    
    publishUpdatedIpAddress()

    # keeps publishing an updated ip address after a while
    time.sleep(publish_wait_time)
