import time
import sensors
import motors


INTERVAL_MS = 250


motors.stop()
print("ultrasonic readout: Ctrl-C to stop")

while True:
    print("distance_cm:", sensors.ultrasonic_cm())
    time.sleep_ms(INTERVAL_MS)
