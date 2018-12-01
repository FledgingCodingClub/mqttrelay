# mqttrelay
RaspberryPi MQTT relay to combine and forward multiple mqtt topics or raw sensor data to a network endpoint for long term storage or analysis.  

## Goals/purpose
- Take multiple endpoints that don't have network connectivity as input
  - MQTT transmitters
  - raw sensor data
  - other raw data that can be translated to an MQTT topic
- Send combined MQTT data streams to a network endpoint (homeassistant planned)

## dependencies
- homeassistant (or alternate network endpoint) that is configured to recieve MQTT streams
- RaspberryPi with network connectivity
- Sensor endpoints that transmit mqtt streams or raw data to Raspberry PI GPIO ports 

