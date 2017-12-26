from m5stack import *
import time

lcd.font(lcd.FONT_7seg, fixedwidth=True, dist=16, width=2)
lcd.setBrightness(200)

while True:
    d = time.strftime("%Y-%m-%d", time.localtime())
    t = time.strftime("%H:%M:%S", time.localtime())
    lcd.print(d, lcd.CENTER, 50, lcd.ORANGE)
    lcd.print(t, lcd.CENTER, 130, lcd.ORANGE)
    time.sleep(1)