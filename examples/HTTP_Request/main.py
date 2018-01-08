from m5stack import *
import requests

def getHTMLText(url):
  try:
    r = requests.get(url)
    r.raise_for_status()
    return r.text
  except:
    return 'ERROR'

print(getHTMLText("http://www.baidu.com"))