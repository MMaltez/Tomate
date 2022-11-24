from m5stack import *
from m5stack_ui import *
from uiflow import *
from m5stack import touch

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xbec0d1)


value = None
led_state = None


label0 = M5Label('Text', x=53, y=67, color=0x000, font=FONT_MONT_30, parent=None)
label1 = M5Label('Text', x=0, y=218, color=0x000, font=FONT_MONT_22, parent=None)
switch0 = M5Switch(x=217, y=66, w=70, h=30, bg_c=0xCCCCCC, color=0x0288FB, parent=None)
slider0 = M5Slider(x=50, y=13, w=220, h=12, min=0, max=100, bg_c=0xa0a0a0, color=0x08A2B0, parent=None)


# Describe this function...
def toogleLED():
  global value, led_state
  if led_state:
    power.setPowerLED(False)
    led_state = False
  else:
    power.setPowerLED(True)
    led_state = True


def switch0_on():
  global value, led_state
  power.setPowerLED(True)
  pass
switch0.on(switch0_on)

def slider0_changed(value):
  global led_state
  screen.set_screen_brightness(value)
  pass
slider0.changed(slider0_changed)

def buttonC_wasPressed():
  global value, led_state
  label0.set_text('C pressed')
  pass
btnC.wasPressed(buttonC_wasPressed)

def buttonB_wasPressed():
  global value, led_state
  label0.set_text('B pressed')
  power.setVibrationEnable(True)
  pass
btnB.wasPressed(buttonB_wasPressed)

def buttonA_wasPressed():
  global value, led_state
  label0.set_text('A pressed')
  pass
btnA.wasPressed(buttonA_wasPressed)

def switch0_off():
  global value, led_state
  power.setPowerLED(False)
  pass
switch0.off(switch0_off)


screen.set_screen_brightness(25)
lcd.font(lcd.FONT_Default)
while True:
  label1.set_text(str(touch.read()))
  if touch.status():
    if 40 ** 2 > ((touch.read()[0]) - 160) ** 2 + ((touch.read()[1]) - 120) ** 2:
      lcd.circle((touch.read()[0]), (touch.read()[1]), 3, color=0x3333ff)
      toogleLED()
  wait_ms(2)

def buttonB_wasReleased():
  global value, led_state
  power.setVibrationEnable(False)
  pass
btnB.wasReleased(buttonB_wasReleased)
