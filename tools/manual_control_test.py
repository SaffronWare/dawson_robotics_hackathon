import time
import sensors
import motors


RUN_MS = 60000
PRINT_EVERY_MS = 250


motors.stop()
print("manual control test: connect YahboomRobot app or use IR remote")
print("manual control test: commands drive motors for 60 seconds")
print("manual control test: app stop, IR Sound key, or timeout stops the robot")

start_ms = time.ticks_ms()
last_print_ms = start_ms
last_cmd = None

try:
    while time.ticks_diff(time.ticks_ms(), start_ms) < RUN_MS:
        now = time.ticks_ms()
        cmd = sensors.manual_command()
        motors.apply_app_command(cmd)

        if cmd != last_cmd or time.ticks_diff(now, last_print_ms) >= PRINT_EVERY_MS:
            print("app_command:", cmd)
            last_cmd = cmd
            last_print_ms = now

        time.sleep_ms(20)
finally:
    motors.stop()
    print("manual control test: stopped")
