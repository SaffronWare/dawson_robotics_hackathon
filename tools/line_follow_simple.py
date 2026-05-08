import time
import sensors
import motors


RUN_MS = 20000
LOOP_MS = 40
FORWARD_SPEED = 0.55
TURN_SPEED = 0.65
SEARCH_SPEED = 0.55
LINE_LOST_STOP_MS = 700
PRINT_EVERY_MS = 250


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
print("line follow simple: black tape on light floor")
print("line follow simple: Ctrl-C to stop")

start_ms = time.ticks_ms()
last_print_ms = start_ms
last_line_ms = start_ms
last_direction = 0

try:
    while time.ticks_diff(time.ticks_ms(), start_ms) < RUN_MS:
        now = time.ticks_ms()
        values = sensors.line_values()
        direction = direction_from_values(values)

        if direction is not None:
            last_line_ms = now
            last_direction = direction

        lost_ms = time.ticks_diff(now, last_line_ms)
        apply_direction(direction, last_direction, lost_ms)

        if time.ticks_diff(now, last_print_ms) >= PRINT_EVERY_MS:
            print("line:", values, "dir:", direction, "lost_ms:", lost_ms)
            last_print_ms = now

        time.sleep_ms(LOOP_MS)
finally:
    motors.stop()
    print("line follow simple: stopped")
