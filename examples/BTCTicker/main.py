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
'''

from m5stack import *
from utils import *
import urequests
import ujson
import utime as time
import curl
import _thread

# # Used curl
# def get_btc_price():
#   try:
#     #r = urequests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
#     r = curl.get("https://www.bitstamp.net/api/ticker/")
#     return ujson.loads(r[2])
#   except:
#     return False


def main():
    lcd.clear()
    lcd.setBrightness(500)
    lcd.setTextColor(lcd.WHITE, lcd.BLACK)
    lcd.font('SFArch_48.fon')
    lcd.print('BTC Price', lcd.CENTER, 25, lcd.ORANGE)
    prev_price = ''
    while True:
        try:
            # btc_data = get_btc_price()
            r = urequests.get("https://www.bitstamp.net/api/ticker/")
            btc_data = ujson.loads(r.text)
            print(btc_data)
            if btc_data:
                # Max price
                high = btc_data['high'][:-1]
                lcd.font(lcd.FONT_DejaVu18)
                lcd.print('Max:', 20, 192, lcd.GREEN)
                lcd.print(high, 5, 215, lcd.GREEN)

                # Min price
                low = btc_data['low'][:-1]
                lcd.font(lcd.FONT_DejaVu18)
                lcd.print('Min:', 255, 192, lcd.RED)
                lcd.print(low+' ', lcd.RIGHT, 215, lcd.RED)

                # Last Price
                price = btc_data['last'][:-1]
                if not price == prev_price:
                    lcd.rect(0, 100, 320, 48, lcd.BLACK, lcd.BLACK)
                    lcd.font('SFArch_48.fon')
                    lcd.print('$ '+price, lcd.CENTER, 100, color=lcd.WHITE)

                # Symbol
                _offset = 180
                if price > prev_price:
                  lcd.rect(140, _offset, 41, 26, lcd.BLACK, lcd.BLACK)
                  lcd.triangle(160,_offset, 140,_offset+25, 180,_offset+25, lcd.GREEN, lcd.GREEN)
                elif price < prev_price:
                  lcd.rect(140, _offset, 41, 26, lcd.BLACK, lcd.BLACK)
                  lcd.triangle(160,_offset+25, 140,_offset, 180,_offset, lcd.RED, lcd.RED)
                prev_price = price
                
            gc.collect()
            time.sleep(1)
        except:
            pass


main()

