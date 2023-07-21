from time import sleep

from factorio_zone_turret.pi_utils import turn_green, turn_red, turn_yellow

while True:
    turn_yellow()
    sleep(1)
    turn_red()
    sleep(1)
    turn_green()
    sleep(1)
