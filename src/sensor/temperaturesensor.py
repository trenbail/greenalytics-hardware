"""
This is where the temperature sensor class will go.
"""
import Adafruit_DHT

class TemperatureSensor:

    def __init__(self, pin):
        self.pin = pin
        self.sensor = Adafruit_DHT.DHT22
        self.humidity = None
        self.temperature = None

    def query_sensor(self):
        self.humidity, self.temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)

    def get_temperature(self):
        return self.temperature

    def get_humidity(self):
        return self.humidity

