import time
import motors


POWER = 0.55
RUN_MS = 600
PAUSE_MS = 500


def pulse(label, action):
    print(label)
    action(POWER)
    time.sleep_ms(RUN_MS)
    motors.stop()
    time.sleep_ms(PAUSE_MS)


print("team motor test: lift wheels before running")
motors.stop()
time.sleep_ms(PAUSE_MS)
pulse("forward", motors.forward)
pulse("backward", motors.backward)
pulse("spin left", motors.spin_left)
pulse("spin right", motors.spin_right)
motors.stop()
print("team motor test: complete")
