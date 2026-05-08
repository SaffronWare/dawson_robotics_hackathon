import time
import sensors
import motors


motors.stop()
print("team remote serial test: no motor control")
print("IR expected: Up=1 Left=4 Right=6 Down=9 Sound=5")
print("Press remote buttons. Ctrl-C to stop.")

last_app = None

while True:
    ir_value = sensors.ir_remote_value()
    if ir_value is not None:
        print("ir_value:", ir_value)

    app_cmd = sensors.app_command()
    if app_cmd != last_app:
        print("app_command:", app_cmd)
        last_app = app_cmd

    motors.stop()
    time.sleep_ms(20)
