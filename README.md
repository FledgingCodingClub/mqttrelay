# mqttrelay
RaspberryPi MQTT relay to combine and forward multiple mqtt topics or raw sensor data to a network endpoint for long term storage or analysis.  

## Goals/purpose
- Take multiple endpoints that don't have network connectivity as input
  - MQTT transmitters
  - raw sensor data
  - other raw data that can be translated to an MQTT topic
- Send combined MQTT data streams to a network endpoint (Home Assistant planned)

## dependencies
- Home Assistant (or alternate network endpoint) that is configured to recieve MQTT streams
- RaspberryPi with network connectivity
- Sensor endpoints that transmit mqtt streams or raw data to Raspberry PI GPIO ports 

#### referernced sources
To provide credit to the people that help by writing guides and tutorials and to let people read more about ideas like this, I am including links to blogs and articles that helped me get started and progress on this project.
- [MQTT tutorial for RaspberryPi, Arduino, and ESP8266](https://www.baldengineer.com/mqtt-tutorial.html)
- [Home Assistant MQTT Sensor input](https://www.home-assistant.io/components/sensor.mqtt/)
- [Eqlipse MQTT an open source MQTT Broker](http://mosquitto.org/)

