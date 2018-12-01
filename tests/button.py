#!/usr/bin/python
# simple program to test button inputs
# uses internal pull down resistor on GPIO 12
# shows button state on=pressed on GPIO 23

from gpiozero import LED, Button
from signal import pause


led = LED(23)
button = Button(12)

button.when_pressed = led.on
button.when_released = led.off

pause()

