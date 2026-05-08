from pico_car import * 
from time import sleep

sensor = ultrasonic()

while True:
    print(sensor.Distance_accurate())

    sleep(1/2)

    