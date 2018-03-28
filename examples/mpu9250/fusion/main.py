# fusiontest.py Simple test program for sensor fusion on Pyboard
# Author Peter Hinch
# Released under the MIT License (MIT)
# Copyright (c) 2017 Peter Hinch
# V0.8 14th May 2017 Option for external switch for cal test. Make platform independent.
# V0.7 25th June 2015 Adapted for new MPU9x50 interface
from m5stack import lcd, buttonA, buttonB
from machine import Pin
import utime as time
from mpu9250 import MPU9250
from fusion import Fusion
from machine import I2C

i2c = I2C(sda = 21, scl = 22)
imu = MPU9250(i2c)
fuse = Fusion()


def getmag():                               # Return (x, y, z) tuple (blocking read)
    return imu.mag.xyz

if buttonA.isPressed():
    print("Calibrating. Press switch when done.")
    fuse.calibrate(getmag, BtnB.press, lambda : time.sleep(0.1))
    print(fuse.magbias)

if False:
    mag = imu.magnetic # Don't include blocking read in time
    accel = imu.acceleration # or i2c
    gyro = imu.gyro
    start = time.ticks_us()  # Measure computation time only
    fuse.update(accel, gyro, mag) # 1.97mS on Pyboard
    t = time.ticks_diff(time.ticks_us(), start)
    print("Update time (uS):", t)


lcd.clear()
lcd.font(lcd.FONT_Small)
lcd.setTextColor(lcd.WHITE, lcd.BLACK)
count = 0

while not buttonA.isPressed():
    accel = imu.acceleration
    gyro = imu.gyro
    mag = imu.magnetic
    fuse.update(accel, gyro, mag) # Note blocking mag read

    print("         Heading      Pitch       Roll:")
    print("        {:8.3f}   {:8.3f}   {:8.3f}".format(fuse.heading, fuse.pitch, fuse.roll))
    print("ACCEL:  {:8.3f}   {:8.3f}   {:8.3f}".format(accel[0], accel[1], accel[2]))
    print("GYRO:   {:8.3f}   {:8.3f}   {:8.3f}".format(gyro[0], gyro[1], gyro[2]))
    print("MAG:    {:8.3f}   {:8.3f}   {:8.3f}\n".format(mag[0], mag[1], mag[2]))

    lcd.print("ACCEL: {:+7.2f}  {:+7.2f}  {:+7.2f}".format(accel[0], accel[1], accel[2]), lcd.CENTER, 20)
    lcd.print("GYRO:  {:+7.2f}  {:+7.2f}  {:+7.2f}".format(gyro[0], gyro[1], gyro[2]), lcd.CENTER, 40)
    lcd.print("MAG:   {:+7.2f}  {:+7.2f}  {:+7.2f}".format(mag[0], mag[1], mag[2]), lcd.CENTER, 60)

    lcd.print("Heading      Pitch      Roll", lcd.CENTER, 120)
    lcd.print("{:+7.2f}    {:+7.2f}    {:+7.2f}".format(fuse.heading, fuse.pitch, fuse.roll), lcd.CENTER, 137)
    time.sleep_ms(10)
