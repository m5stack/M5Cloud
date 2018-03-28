from m5stack import lcd, buttonA
from mpu9250 import MPU9250
from time import sleep_ms
from machine import I2C

i2c = I2C(sda = 21, scl = 22)
imu = MPU9250(i2c)

lcd.clear()
lcd.font(lcd.FONT_Small)
lcd.setTextColor(lcd.WHITE, lcd.BLACK)

while not buttonA.isPressed():
    accel = imu.acceleration
    gyro = imu.gyro
    mag = imu.magnetic
    print("ACCEL:  {:8.3f}   {:8.3f}   {:8.3f}".format(accel[0], accel[1], accel[2]))
    print("GYRO:   {:8.3f}   {:8.3f}   {:8.3f}".format(gyro[0], gyro[1], gyro[2]))
    print("MAG:    {:8.3f}   {:8.3f}   {:8.3f}".format(mag[0], mag[1], mag[2]))
    print('')
    lcd.print("ACCEL: {:+7.2f}  {:+7.2f}  {:+7.2f}".format(accel[0], accel[1], accel[2]), lcd.CENTER, 20)
    lcd.print("GYRO:  {:+7.2f}  {:+7.2f}  {:+7.2f}".format(gyro[0], gyro[1], gyro[2]), lcd.CENTER, 40)
    lcd.print("MAG:   {:+7.2f}  {:+7.2f}  {:+7.2f}".format(mag[0], mag[1], mag[2]), lcd.CENTER, 60)
    sleep_ms(20)

lcd.print('Exit.', 0, 100)