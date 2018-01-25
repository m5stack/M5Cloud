from m5stack import *
from faces import Faces

keyboard = Faces()

# read once
print("Key value:", end='')
print(keyboard.read())

# callback
def keyboard_cb(value):
  print("Key value:", end='')
  print(value)
  lcd.print(value)

keyboard.callback(keyboard_cb)