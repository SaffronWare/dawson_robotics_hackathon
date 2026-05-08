import sensors
import motors


motors.stop()

print("smoke: imports ok")
print("line:", sensors.line_values())
print("ultrasonic_cm:", sensors.ultrasonic_cm())
print("app_command:", sensors.app_command())
motors.stop()
