---
title: Notes on working with M5StickC Plus
author: Miguel Maltez José
date: 2022-08-20
---

# How to print text to the LCD screen?

- [m5stack LCD docs](https://github.com/m5stack/UIFlow-Code/wiki/Graphic)
- [lcddemo](https://github.com/m5stack/M5GO/blob/master/examples/lcddemo.py)


# scratch pad

```
FONT_Default -- 0
FONT_DejaVu18 -- 1
FONT_DejaVu24 -- 2
FONT_DejaVu40 -- 11
FONT_DejaVu56 -- 12
FONT_DejaVu72 -- 13
FONT_Ubuntu -- 3
FONT_Comic -- 4
FONT_Minya -- 5
FONT_Tooney -- 6
FONT_Small -- 7
FONT_DefaultSmall -- 8
FONT_Arial12 -- 14
FONT_Arial16 -- 15
FONT_7seg -- 9
FONT_UNICODE -- 16
```

# LCD reference

### lcd.text(x, y, text, [color], transparent=True)

Display the text at position (x,y). if color is not given use current foreground color.

* **x**: horizontal position of the upper left point in pixels, special values can be given:
	- CENTER, centers the text
	- RIGHT, right justifies the text
	- LASTX, continues from last X position; offset can be used: LASTX+n
* **y**: vertical position of the upper left point in pixels, special values can be given:
	- CENTER, centers the text
	- BOTTOM, bottom justifies the text
	- LASTY, continues from last Y position; offset can be used: LASTY+n
* **text**: string to be displayed. Two special characters are allowed in strings:
	- '\r' CR (0x0D), clears the display to EOL
	- '\n' LF (ox0A), continues to the new line, x=0


# References

* [7-segment and 14-segment font](https://www.keshikan.net/fonts-e.html)
