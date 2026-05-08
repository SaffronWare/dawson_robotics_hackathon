import time
from machine import ADC
import motors


CHANNELS = (26, 27, 28, 29)


motors.stop()
adcs = []
for channel in CHANNELS:
    try:
        adcs.append((channel, ADC(channel)))
    except Exception as exc:
        print("adc_init_error:", channel, repr(exc))

print("adc battery probe: raw 0..65535")
print("adc battery probe: compare readings with robot battery on/off")

for _ in range(20):
    values = []
    for channel, adc in adcs:
        values.append("{}={}".format(channel, adc.read_u16()))
    print("adc:", " ".join(values))
    time.sleep_ms(250)
