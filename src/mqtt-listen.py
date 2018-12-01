#!/usr/bin/python
# program to listen on pin 12 for a button press and
# send an MQTT message when it is pressed or released
import paho.mqtt.publish as publish
from gpiozero import Button
from signal import pause

mqttsrv='127.0.0.1'
led = LED(23)
button = Button(12)

def button_down():
  led.on
  publish.single("buttonTest", "button pressed", hostname=mqttsrv)

def button_up():
  led.off
  publish.single("buttonTest", "button releasd", hostname=mqttsrv)

button.when_pressed = button_down()
button.when_released = button_up()


pause()

