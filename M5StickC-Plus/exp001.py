"""Printing text to the embedded LCD screen.

@author Miguel Maltez
@date 20220820
"""
from m5stack import lcd

fonts = (
	(lcd.FONT_Default, "Default"),
	(lcd.FONT_Small, "Small"),
	(lcd.FONT_DefaultSmall, "Default"),
	(lcd.FONT_Ubuntu, "Ubuntu"),
	(lcd.FONT_Comic, "Comic"),
	(lcd.FONT_DejaVu18, "DejaVu18"),
	(lcd.FONT_DejaVu24, "DejaVu24"),
	(lcd.FONT_Minya, "Minya"),
	(lcd.FONT_Tooney, "Tooney"),
)

lcd.setRotation(3) # landscape with button to the right
lcd.clear(lcd.BLACK)

text_column = 0
lcd.setCursor(0,0)
for font, name in fonts:
	lcd.font(font)
	if lcd.text_y() + lcd.fontSize()[1] >= lcd.screensize()[1]:
		text_column = 100
		lcd.setCursor(text_column, 0)
	lcd.print(name + "\n", )
	lcd.setCursor(text_column, lcd.text_y())

# printing centered text transparent or not
tx, ty = lcd.getCursor()
lcd.set_bg(lcd.BLUE)
lcd.text(lcd.CENTER,lcd.CENTER, "Miguel", lcd.GREEN, transparent=True)
lcd.text(100,lcd.text_y() + 5, "Miguel", lcd.YELLOW, transparent=False)
