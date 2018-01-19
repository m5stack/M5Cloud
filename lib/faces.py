"""
M5Stack MicroPython FACES keyboard I2C driver
"""

class Faces:
  def __init__(self):
    from machine import I2C
    self.i2c = I2C(sda=21, scl=22)
    self.addr = 0x08
    self.cb = None

  def read(self):
    return self.i2c.readfrom(self.addr, 1)

  def _callback(self, pin):
    from machine import Pin
    if pin == Pin(5):
      self.cb(self.read())
      
  def callback(self, cb):
    from machine import Pin
    self.pin = Pin(5)
    self.pin.init(Pin.IN)
    self.pin.irq(trigger=Pin.IRQ_FALLING, handler=self._callback)
    self.cb = cb
