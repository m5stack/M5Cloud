from m5stack import *
import time

lcd.font(lcd.FONT_7seg, fixedwidth=True, dist=15, width=2)
lcd.setTextColor(lcd.ORANGE, lcd.BLACK)

while True:
    d = time.strftime("%Y-%m-%d", time.localtime())
    t = time.strftime("%H:%M:%S", time.localtime())
    lcd.print(d, lcd.CENTER, 60, lcd.ORANGE)
    lcd.print(t, lcd.CENTER, 130, lcd.ORANGE)
    time.sleep(1)
