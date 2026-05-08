import time
import sensors
import motors
from states import OBSTACLE_CM


RUN_MS = 30000
LOOP_MS = 40
FORWARD_SPEED = 0.55
TURN_SPEED = 0.65
SEARCH_SPEED = 0.55
LINE_LOST_STOP_MS = 700
PRINT_EVERY_MS = 250
OBSTACLE_CONFIRM_READS = 3


def direction_from_values(values):
    left_outer, left_inner, right_inner, right_outer = values

    if left_inner == 0 and right_inner == 0:
        return 0
    if left_inner == 0 or left_outer == 0:
        return -1
    if right_inner == 0 or right_outer == 0:
        return 1
    return None


def apply_direction(direction, last_direction, lost_ms):
    if direction == 0:
        motors.forward(FORWARD_SPEED)
    elif direction == -1:
        motors.turn_left(TURN_SPEED)
    elif direction == 1:
        motors.turn_right(TURN_SPEED)
    elif lost_ms < LINE_LOST_STOP_MS and last_direction == -1:
        motors.spin_left(SEARCH_SPEED)
    elif lost_ms < LINE_LOST_STOP_MS and last_direction == 1:
        motors.spin_right(SEARCH_SPEED)
    else:
        motors.stop()


motors.stop()
print("line until obstacle: stop threshold_cm:", OBSTACLE_CM)
print("line until obstacle: confirm reads:", OBSTACLE_CONFIRM_READS)

start_ms = time.ticks_ms()
last_print_ms = start_ms
last_line_ms = start_ms
last_direction = 0
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

        values = sensors.line_values()
        direction = direction_from_values(values)

        if direction is not None:
            last_line_ms = now
            last_direction = direction

        lost_ms = time.ticks_diff(now, last_line_ms)
        apply_direction(direction, last_direction, lost_ms)

        if time.ticks_diff(now, last_print_ms) >= PRINT_EVERY_MS:
            print(
                "line:",
                values,
                "dir:",
                direction,
                "distance_cm:",
                distance,
                "close_reads:",
                close_reads,
            )
            last_print_ms = now

        time.sleep_ms(LOOP_MS)
    else:
        print("timeout without obstacle")
finally:
    motors.stop()
    print("line until obstacle: stopped")
