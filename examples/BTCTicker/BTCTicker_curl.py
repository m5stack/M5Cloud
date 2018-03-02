'''
Arduino version:
https://github.com/dankelley2/M5Stack_BTCTicker

Response (JSON)
  last	    Last BTC price.
  high	    Last 24 hours price high.
  low	      Last 24 hours price low.
  vwap	    Last 24 hours volume weighted average price.
  volume	  Last 24 hours volume.
  bid	      Highest buy order.
  ask	      Lowest sell order.
  timestamp	Unix timestamp date and time.
  open	    First price of the day.
  
  m5stack.com/api/btc/ticker/btcusd.json
'''

from m5stack import *
from utils import *
import utime as time
import machine
import urequests
import ujson
import curl
import utils
import m5cloud
import gc


# def timeout_reset(timer):
#     import machine
#     machine.reset()


# t1 = machine.Timer(2)
# t1.init(period=60*1000*60*6, mode=t1.PERIODIC, callback=timeout_reset)


def main():
    lcd.clear()
    lcd.setBrightness(800)
    lcd.setTextColor(lcd.WHITE, lcd.BLACK)
    lcd.font('SFArch_48.fon')
    lcd.print('BTC Price', lcd.CENTER, 25, lcd.ORANGE)
    prev_price = ''
    timereset = time.ticks_ms() + (60*1000)
    while True:
        if not m5cloud.idle():
            break
        try:
            # btc_data = get_btc_price()
            gc.collect()
            lcd.triangle(300,0, 319,0, 319,19, lcd.YELLOW, lcd.YELLOW)
            r = curl.get('http://api.m5stack.com/btc')
            lcd.triangle(300,0, 319,0, 319,19, lcd.BLUE, lcd.BLUE)
            btc_data = ujson.loads(r[2])
            print(btc_data)
            print('')
            if btc_data:
                # Max price
                high = btc_data['high']
                high = high[:(high.find('.')+3)]
                lcd.font(lcd.FONT_DejaVu18)
                lcd.print('Max:', 20, 192, lcd.GREEN)
                lcd.print(high, 5, 215, lcd.GREEN)

                # Min price
                low = btc_data['low']
                low = low[:(low.find('.')+3)]
                lcd.font(lcd.FONT_DejaVu18)
                lcd.print('Min:', 255, 192, lcd.RED)
                lcd.print(low, lcd.RIGHT, 215, lcd.RED)

                # Last Price
                price = btc_data['last']
                if not price == prev_price:
                    lcd.rect(0, 100, 320, 48, lcd.BLACK, lcd.BLACK)
                    lcd.font('SFArch_48.fon')
                    lcd.print('$ '+price, lcd.CENTER, 100, color=lcd.WHITE)

                # Symbol
                _offset = 175
                if price > prev_price:
                  lcd.rect(140, _offset, 41, 26, lcd.BLACK, lcd.BLACK)
                  lcd.triangle(160,_offset, 140,_offset+25, 180,_offset+25, lcd.GREEN, lcd.GREEN)
                elif price < prev_price:
                  lcd.rect(140, _offset, 41, 26, lcd.BLACK, lcd.BLACK)
                  lcd.triangle(160,_offset+25, 140,_offset, 180,_offset, lcd.RED, lcd.RED)
                prev_price = price

        except:
            pass
        time.sleep(5)

main()

