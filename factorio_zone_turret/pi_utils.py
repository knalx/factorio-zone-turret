from gpiozero import RGBLED

from colorzero import Color

led = RGBLED(17, 27, 22)


def turn_yellow():
    led.color = Color.from_rgb(255, 215, 0)


def turn_green():
    led.color = Color.from_rgb(34, 139, 34)


def turn_red():
    led.color = Color.from_rgb(139, 0, 0)
