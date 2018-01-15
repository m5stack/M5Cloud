from m5stack import *
import urequests

r = urequests.get("http://www.baidu.com")
print(r.text)
