"""
Here is where the controller will live for the hardware
"""
import time
from sensor import lightsensor
from sensor import temperaturesensor


def run(tempsensor, lightsensor):
    while(True):
        tempsensor.query_sensor()
        temperature = tempsensor.get_temperature()
        temperature = temperature * 9/5 + 32
        humidity = tempsensor.get_humidity()

        lightlevel = lightsensor.get_level()

        print("Temperature= {} Humidity = {}\n".format(temperature, humidity))
        print("Light Level = {}\n\n".format(lightlevel))

        time.sleep(1)


lightsensor = lightsensor.LightSensor(0)
temperaturesensor = temperaturesensor.TemperatureSensor(2)

run(temperaturesensor, lightsensor)

