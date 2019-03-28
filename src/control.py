"""
Here is where the controller will live for the hardware
"""
import time
from sensor import lightsensor
from sensor import temperaturesensor


def run(tempsensor, lightsensor):
    while(True):
        tempsensor.query_sensor()
        tempsensor = tempsensor.get_temperature()
        humidity = tempsensor.get_humidity

        lightlevel = lightsensor.get_level()

        print("Temperature= ", temperature, " ", "Humidity = ", humidity)
        print("\n Light Level = ", lightlevel, "\n\n")

        time.sleep(1)


light = lightsensor.LightSensor(0)
temperature = temperaturesensor.TemperatureSensor(2)

run(temperature, light)

