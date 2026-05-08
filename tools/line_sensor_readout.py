import time
import sensors
import motors


motors.stop()
print("line sensor readout: left_outer left_inner right_inner right_outer")
print("line sensor readout: Ctrl-C to stop")

while True:
    print("line:", sensors.line_values())
    time.sleep_ms(250)
