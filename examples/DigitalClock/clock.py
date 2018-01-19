from m5stack import *
import time, _thread, machine

def clock():
    rtc = machine.RTC()
    print("Synchronize time from NTP server ...")
    lcd.println("Synchronize time from NTP server ...")
    rtc.ntp_sync(server="cn.ntp.org.cn")

    lcd.clear()
    lcd.setBrightness(200)
    lcd.font(lcd.FONT_7seg, fixedwidth=True, dist=16, width=2)
    
    while True:
        d = time.strftime("%Y-%m-%d", time.localtime())
        t = time.strftime("%H:%M:%S", time.localtime())
        lcd.print(d, lcd.CENTER, 50, lcd.ORANGE)
        lcd.print(t, lcd.CENTER, 130, lcd.ORANGE)
        time.sleep(1)

_thread.start_new_thread('Clock', clock, ())