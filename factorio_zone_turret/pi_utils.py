from time import sleep

from gpiozero import LED, PWMLED

red_led = PWMLED(17)


def led_on():
    red_led.on()


def led_off():
    red_led.off()


while True:
    for i in range(0, 255):
        sleep(0.01)
        red_led.value = i
    for i in range(255, 0):
        sleep(0.01)
        red_led.value = i
