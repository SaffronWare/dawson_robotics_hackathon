from pico_car import *
from time import sleep
import sensors, motors

from time import sleep_ms

refresh = 100

car = pico_car()


Tracing_OL = Pin(2, Pin.IN)
Tracing_IL = Pin(3, Pin.IN)
Tracing_IR = Pin(4, Pin.IN)
Tracing_OR = Pin(5, Pin.IN)
was_turning=False
def line_following():
    global was_turning
    forward_s = 1000
    turn_s = 150
    timres = 0
    while True:

        

        
        car.Car_Stop()
        sleep(0.02/refresh)
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
            timers = 0
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
            timers += 1/refresh
            car.Car_Stop()

            if timers > 0.1:
                return

        
            #("S")

        #(f"out_left : {out_left}, in_left : {in_left}")
        #(f"out_right {out_right}, in_right : {in_right}")



def go_in_box():
    sensor = ultrasonic()
    distance = 10000
    times = 0
    while distance >= 60:
        distance = sensor.Distance_accurate()
        sleep(1/8)
        car.Car_Run(500,500)
        #car.Car_Left(100,100)
        times += 1/8
    car.Car_Left(40,40)
    sleep(0.1)
    times = 0
    while distance > 45:
        distance = sensor.Distance_accurate()
        
        times  += 1/8
        car.Car_Run(100,100)
        sleep(1/8)
    car.Car_Stop()

def manual_control():
    while True:
        cmd = sensors.manual_command()
        print(cmd)
        motors.apply_app_command(cmd)
        sleep_ms(50)


line_following()
go_in_box()
manual_control()
