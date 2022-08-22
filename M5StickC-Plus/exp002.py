"""LCD 7-segment font.

* What is the size of the 7-seg font
  depending on dist and width parameters of attri7seg?

@author Miguel Maltez
@date 20220822
"""
from m5stack import lcd, btnA
import time

def drawTitle():
	lcd.clear()
	lcd.font(lcd.FONT_Default)
	lcd.print("7-seg test", lcd.RIGHT,0)

def sevensegtest(dist, width):
	lcd.font(lcd.FONT_7seg)
	lcd.attrib7seg(dist, width, False, lcd.GREEN)
	lcd.set_bg(lcd.BLACK)
	lcd.set_fg(lcd.WHITE)
	lcd.print("07:59",0,0,lcd.RED)
	sw, sh = lcd.fontSize()
	print(dist, width, sw, sh, sw*5)

lcd.setRotation(3) # landscape with button to the right
drawTitle()
sevensegtest(24,4)

while not btnA.isPressed():
	time.sleep_ms(100)

drawTitle()
sevensegtest(24,6)
