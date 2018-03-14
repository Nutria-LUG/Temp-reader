from acmepins import GPIO
import dht
import time
import datetime

instance = dht.DHT(pin='PC0')

result = instance.read()
if result.is_valid():
    print("Temperature: %d C" % result.temperature)
    print("Humidity: %d %%" % result.humidity)
else :
    print("Sensor reading failure")

