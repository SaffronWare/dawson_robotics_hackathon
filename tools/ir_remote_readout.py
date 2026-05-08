import time
import sensors
import motors


motors.stop()
print("IR remote readout: point remote at receiver")
print("IR remote readout: expected Up=1 Left=4 Right=6 Down=9 Sound=5")
print("IR remote readout: Ctrl-C to stop")

while True:
    value = sensors.ir_remote_value()
    if value is not None:
        print("ir_value:", value)
    time.sleep_ms(20)
