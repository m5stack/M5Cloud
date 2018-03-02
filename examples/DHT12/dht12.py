"""
MicroPython Aosong DHT12 I2C driver
"""

class DHTBaseI2C:
    def __init__(self, i2c=None, addr=0x5c):
        if i2c == None:
            from machine import I2C, Pin
            self.i2c = I2C(sda=21, scl=22)
        else:
            self.i2c = i2c
        self.addr = addr
        self.buf = bytearray(5)
    def measure(self):
        buf = self.buf
        self.i2c.readfrom_mem_into(self.addr, 0, buf)
        if (buf[0] + buf[1] + buf[2] + buf[3]) & 0xff != buf[4]:
            raise Exception("checksum error")

class DHT12(DHTBaseI2C):
    def humidity(self):
        return self.buf[0] + self.buf[1] * 0.1

    def temperature(self):
        t = self.buf[2] + (self.buf[3] & 0x7f) * 0.1
        if self.buf[3] & 0x80:
            t = -t
        return t