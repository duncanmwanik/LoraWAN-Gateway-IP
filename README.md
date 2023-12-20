#Publishes updated IP addresses of a LoRaWAN gateway connected to a Raspberry Pi to an MQTT topic that can be subscribed to from a Vue.js web app.

## folder :file_folder: raspberry_pi
- Contains python files to run on the Raspberry Pi.
- The script publishes the os IP address after a while, on repeat.

## folder :file_folder: user_interface
- A Vue.js to subscibe to the MQTT topic on request.
