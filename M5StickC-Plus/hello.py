# Hello world
from m5stack import *
from m5ui import *
from uiflow import *
from easyIO import *

setScreenColor(0x111111)


led_on = None
spk_vol = None
spk_vol_inc = None


label0 = M5TextBox(14, 45, "Hello", lcd.FONT_DejaVu40, 0xFFFFFF, rotate=0)
title0 = M5Title(title="Hello World", x=3, fgcolor=0xFFFFFF, bgcolor=0xff6600)
label_date = M5TextBox(17, 105, "date", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label_time = M5TextBox(14, 137, "time", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label_voltage = M5TextBox(14, 176, "voltage", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label_current = M5TextBox(14, 201, "current", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label_batt = M5TextBox(95, 216, "batt", lcd.FONT_Default, 0xc1d34b, rotate=0)
label_spk = M5TextBox(96, 91, "spk", lcd.FONT_Ubuntu, 0x2f2f97, rotate=0)
label_temp = M5TextBox(87, 131, "temp", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
label1 = M5TextBox(94, 174, "Text", lcd.FONT_Default, 0xFFFFFF, rotate=0)

from numbers import Number



def buttonB_wasPressed():
  global led_on, spk_vol, spk_vol_inc
  if led_on:
    M5Led.off()
    led_on = False
  else:
    M5Led.on()
    led_on = True
  pass
btnB.wasPressed(buttonB_wasPressed)

def buttonA_wasPressed():
  global led_on, spk_vol, spk_vol_inc
  if spk_vol >= 100:
    spk_vol_inc = -5
  elif spk_vol <= 0:
    spk_vol_inc = 5
  spk_vol = (spk_vol if isinstance(spk_vol, Number) else 0) + spk_vol_inc
  speaker.setVolume(spk_vol)
  speaker.tone(2400, 200)
  pass
btnA.wasPressed(buttonA_wasPressed)


led_on = False
spk_vol_inc = 5
spk_vol = 0
speaker.setVolume(spk_vol)
while True:
  label_date.setText(str((str((rtc.now()[0])) + str(((str('-') + str(((str((rtc.now()[1])) + str(((str('-') + str((rtc.now()[2]))))))))))))))
  label_time.setText(str((str((rtc.now()[3])) + str(((str(':') + str(((str((rtc.now()[4])) + str(((str(':') + str((rtc.now()[5]))))))))))))))
  label_voltage.setText(str((str(("%.3f"%float((axp.getBatVoltage())))) + str('V'))))
  label_current.setText(str((str(("%.1f"%float((axp.getBatCurrent())))) + str('mA'))))
  label_batt.setText(str((str(("%.0f"%float((map_value((axp.getBatVoltage()), 3.7, 4.1, 0, 100))))) + str('%'))))
  label_spk.setText(str(spk_vol))
  label_temp.setText(str("%.1f"%float((axp.getTempInAXP192()))))
  label1.setText(str(axp.getVBusCurrent()))
  wait_ms(2)
