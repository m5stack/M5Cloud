from m5stack import *
import faces

keyboard = faces.Faces()

# read once
print("Key value:", end='')
print(keyboard.read())

# callback
def keyboard_cb(value):
  print("Key value:", end='')
  print(value)
  lcd.print(value)

keyboard.callback(keyboard_cb)