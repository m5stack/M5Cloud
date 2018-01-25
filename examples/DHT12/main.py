import time
from dht12 import DHT12
sensor = DHT12()

while True:
    sensor.measure()
    print("Temperature:%.2f" % (sensor.temperature()))
    print("Humidity:%.2f \n" % (sensor.humidity()))
    time.sleep(1)