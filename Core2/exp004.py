"""LCD 7-segment font.

* What is the size of the 7-seg font
  depending on dist and width parameters of attri7seg?

@author Miguel Maltez
@date 20220822
@date 20221123
"""
from m5stack import lcd, btnA, btnB
import time, sys
import machine

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
rtc = machine.RTC()

def showTimer():
	lcd.font(lcd.FONT_7seg)
	lcd.attrib7seg(40, 5, True, lcd.WHITE)
	lcd.set_bg(lcd.BLACK)
	lcd.set_fg(lcd.WHITE)
	lcd.print("{5:02}:{6:02}".format(*rtc.datetime()),0,0)

def showTime(dist=24, width=3):
	lcd.font(lcd.FONT_7seg)
	lcd.attrib7seg(dist, width, True, lcd.WHITE)
	lcd.set_bg(lcd.BLACK)
	lcd.set_fg(lcd.WHITE)
	lcd.print("{4:02}:{5:02}:{6:02}".format(*rtc.datetime()),0,lcd.BOTTOM)

def showDate():
	lcd.font(lcd.FONT_7seg)
	lcd.attrib7seg(8, 1, True, lcd.WHITE)
	lcd.set_bg(lcd.BLACK)
	lcd.set_fg(lcd.WHITE)
	lcd.print("{0:04}-{1:02}-{2:02}".format(*rtc.datetime()),lcd.CENTER, 130)

lcd.font(lcd.FONT_Default)
lcd.print("Start", 0,0)

showTimer()
showDate()
showTime()
