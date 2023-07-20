from time import sleep

from colorzero import Color

from factorio_zone_turret.pi_utils import led


while True:
    for color in range(0, 360):  
        led.color = Color.from_hsv(color / 360, 1, 0.5)  
        sleep(0.01)
