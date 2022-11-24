"""4  digit 7 segment display
"""
from machine import I2C, RTC

i2c = I2C(scl=33, sda=32, freq=400000)
rtc = RTC()
last = "    "
i2c.writeto(0x30, b'\x30\x02')

while True:
	now = "{5:02}:{6:02}".format(*rtc.datetime())
	if now != last:
		i2c.writeto(0x30, "\x20" + now)
		last = now


