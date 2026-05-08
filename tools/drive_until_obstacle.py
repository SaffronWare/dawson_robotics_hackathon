import time
import motors
import sensors
from states import OBSTACLE_CM


RUN_MS = 20000
LOOP_MS = 40
DRIVE_SPEED = 0.45
PRINT_EVERY_MS = 250
OBSTACLE_CONFIRM_READS = 3


motors.stop()
print("drive until obstacle: no line following")
print("drive until obstacle: stop threshold_cm:", OBSTACLE_CM)
print("drive until obstacle: confirm reads:", OBSTACLE_CONFIRM_READS)

start_ms = time.ticks_ms()
last_print_ms = start_ms
close_reads = 0

try:
    while time.ticks_diff(time.ticks_ms(), start_ms) < RUN_MS:
        now = time.ticks_ms()
        distance = sensors.ultrasonic_cm()

        if distance <= OBSTACLE_CM:
            close_reads += 1
        else:
            close_reads = 0

        if close_reads >= OBSTACLE_CONFIRM_READS:
            motors.stop()
            print("obstacle confirmed:", distance, "cm")
            break

        motors.forward(DRIVE_SPEED)

        if time.ticks_diff(now, last_print_ms) >= PRINT_EVERY_MS:
            print("distance_cm:", distance, "close_reads:", close_reads)
            last_print_ms = now

        time.sleep_ms(LOOP_MS)
    else:
        print("timeout without obstacle")
finally:
    motors.stop()
    print("drive until obstacle: stopped")
