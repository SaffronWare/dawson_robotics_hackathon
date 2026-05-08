from pico_car import *
from time import sleep

refresh = 200

car = pico_car()


Tracing_OL = Pin(2, Pin.IN)
Tracing_IL = Pin(3, Pin.IN)
Tracing_IR = Pin(4, Pin.IN)
Tracing_OR = Pin(5, Pin.IN)
was_turning=False
def line_following():
    global was_turning
    forward_s = 170
    turn_s = 55
    while True:


        car.Car_Stop()
        sleep(0.1/refresh)
        out_left, in_left = Tracing_OL.value(), Tracing_IL.value()
        out_right, in_right = Tracing_OR.value(),Tracing_IR.value()

        inside_path = not in_left and not in_right

        if not inside_path:
            #car.Car_Stop()
            pass

        if was_turning:
            #car.Car_Stop()
            was_turning = False
        elif inside_path:
            was_turning = False
            car.Car_Run(forward_s,forward_s)
            #("F")
        elif in_left and not in_right:
            car.Car_Right(turn_s, turn_s)
            #("R")
        elif in_right and not in_left:
            car.Car_Left(turn_s,turn_s)
            #("L")
        elif not out_left:
            car.Car_Left(turn_s,turn_s)
        elif not out_right:
            car.Car_Right(turn_s,turn_s)
        else:
            car.Car_Stop()
            #("S")

        #(f"out_left : {out_left}, in_left : {in_left}")
        #(f"out_right {out_right}, in_right : {in_right}")





line_following()
