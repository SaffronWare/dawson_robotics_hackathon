import time
from machine import ADC
from pico_car import pico_car


POWER = 180
RUN_MS = 700
SAMPLE_MS = 100


battery = ADC(28)
vsys = ADC(29)
motor = pico_car()


def raw_power():
    return battery.read_u16(), vsys.read_u16()


def print_power(label):
    bat, sys = raw_power()
    print("{}: adc28={} adc29={}".format(label, bat, sys))


def run_step(label, left, right):
    print(label, "left_pwm", left, "right_pwm", right)
    motor.Car_Run(left, right)
    start = time.ticks_ms()
    while time.ticks_diff(time.ticks_ms(), start) < RUN_MS:
        print_power("  load")
        time.sleep_ms(SAMPLE_MS)
    motor.Car_Stop()
    time.sleep_ms(400)
    print_power("  after")


motor.Car_Stop()
print("motor battery diagnostic: lift wheels or hold robot")
print("motor battery diagnostic: Yahboom note says adc power above 26000")
print_power("idle")
run_step("left motor only", POWER, 0)
run_step("right motor only", 0, POWER)
run_step("both motors", POWER, POWER)
motor.Car_Stop()
print("motor battery diagnostic: stopped")
