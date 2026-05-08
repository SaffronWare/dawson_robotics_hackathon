import time
import motors


POWER = 0.65
RUN_MS = 700
PAUSE_MS = 500


def pulse(label, action):
    print(label)
    action(POWER)
    time.sleep_ms(RUN_MS)
    motors.stop()
    time.sleep_ms(PAUSE_MS)


print("motor test: lift wheels before running")
motors.stop()
time.sleep_ms(PAUSE_MS)
pulse("left motor / turn left", motors.turn_left)
pulse("right motor / turn right", motors.turn_right)
pulse("forward", motors.forward)
pulse("backward", motors.backward)
motors.stop()
print("motor test: complete")
