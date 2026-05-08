import sensors, motors

from time import sleep_ms

while True:
    cmd = sensors.manual_command()
    print(cmd)
    motors.apply_app_command(cmd)
    sleep_ms(50)
