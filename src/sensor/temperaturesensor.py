"""
This is where the temperature sensor class will go.
"""
import Adafruit_DHT
import datetime
from time import sleep


class TemperatureSensor:

    def __init__(self, pin):
        self.pin = pin
        self.sensor = Adafruit_DHT.DHT22
        self.humidity = None
        self.temperature = None

    def query_sensor(self):
        self.humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
        file = open('log.txt', 'a')
        while temperature is None:
            self.humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
            file.write('{}: There was an issue getting the temp \r\n'.format(datetime.datetime.now()))
            sleep(2)
            print("Error getting Temp")
        file.close()
        self.temperature = temperature * 9/5 + 32

    def get_temperature(self):
        return self.temperature

    def get_humidity(self):
        return self.humidity

