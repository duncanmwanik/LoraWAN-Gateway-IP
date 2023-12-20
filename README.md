# LoraWAN Gateway IP
Publishes updated IP addresses of a LoRaWAN gateway connected to a Raspberry Pi to an MQTT topic that can be subscribed to from a Vue.js web app.

## :file_folder: raspberry_pi
- Contains python files to run on the Raspberry Pi.
- Run the `main.py` script.
- The script publishes the os IP address after a while, on repeat.

## :file_folder: user_interface
- A Vue.js web app to subscibe to the MQTT topic on request.
