import dht12, time
sensor = dht12.DHT12()

while True:
    sensor.measure()
    print("Temperature:%.2f" % (sensor.temperature()))
    print("Humidity:%.2f \n" % (sensor.humidity()))
    time.sleep(1)