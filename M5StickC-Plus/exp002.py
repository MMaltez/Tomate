"""LCD 7-segment font.

* What is the size of the 7-seg font
  depending on dist and width parameters of attri7seg?

@author Miguel Maltez
@date 20220822
"""
from m5stack import lcd, btnA, btnB
import time, sys

def drawTitle():
	lcd.clear(0x101010)
	lcd.font(lcd.FONT_Default)
	lcd.print("7-seg test", lcd.RIGHT,0)

def sevensegtest(dist, width):
	lcd.font(lcd.FONT_7seg)
	lcd.attrib7seg(dist, width, True, lcd.RED)
	lcd.set_bg(lcd.BLACK)
	lcd.set_fg(lcd.WHITE)
	sw, sh = lcd.fontSize()
	lcd.rect(0,0, sw,sh, lcd.MAGENTA)
	lcd.print("06:59",0,0,lcd.RED)
	print(dist, width, sw, sh)

lcd.setRotation(3) # landscape with button to the right

for width in range(24):
	for dist in range(68):
		drawTitle()
		sevensegtest(dist, width)
		while not btnA.isPressed():
			time.sleep_ms(100)
			if btnB.isPressed():
				sys.exit()
