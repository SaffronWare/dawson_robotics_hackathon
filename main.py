from pico_car import *
from time import sleep

refresh = 60

car = pico_car()


Tracing_OL = Pin(2, Pin.IN)
Tracing_IL = Pin(3, Pin.IN)
Tracing_IR = Pin(4, Pin.IN)
Tracing_OR = Pin(5, Pin.IN)

def line_following():
    forward_s = 500
    turn_s = 100
    car.Car_Run(forward_s, forward_s)



    out_left, in_left = Tracing_OL.value(), Tracing_IL.value()
    out_right, in_right = Tracing_OR.value(),Tracing_IR.value()

    inside_path = not in_left and not in_right

    if inside_path:
        car.Car_Run(forward_s,forward_s)
        print("F")
    elif in_left and not in_right:
        car.Car_Right(turn_s, turn_s)
        print("R")
    elif in_right and not in_left:
        car.Car_Left(turn_s,turn_s)
        print("L")
    elif not out_left:
        car.Car_Left(turn_s,turn_s)
    elif not out_right:
        car.Car_Right(turn_s,turn_s)
    else:
        car.Car_Stop()
        print("S")

    print(f"out_left : {out_left}, in_left : {in_left}")
    print(f"out_right {out_right}, in_right : {in_right}")







while True:
    line_following()
    sleep(1/refresh)
    car.Car_Stop()