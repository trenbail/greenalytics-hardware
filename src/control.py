"""
Here is where the controller will live for the hardware
"""

import time
from greenaliticsapi import APIInterface
from sensor import lightsensor
from sensor import temperaturesensor


def run():
    light_api = APIInterface("http://greenalytics.ga:5000/api/hardware/light")
    temperature_api = APIInterface("http://greenalytics.ga:5000/api/hardware/temperature")
    humidity_api = APIInterface("http://greenalytics.ga:5000/api/hardware/humidity")

    while True:
        temperaturesensor.query_sensor()
        temperature = temperaturesensor.get_temperature()
        humidity = temperaturesensor.get_humidity()

        lightlevel = lightsensor.get_level()
        light_api.post(lightlevel)
        print(light_api.get_status())

        if temperature is not None or humidity is not None:
            temperature_api.post(temperature)
            print(temperature_api.get_status())

            humidity_api.post(humidity)
            print(humidity_api.get_status())

        print("Temperature= {} Humidity = {}".format(temperature, humidity))
        print("Light Level = {}\n\n".format(lightlevel))

        time.sleep(1)


lightsensor = lightsensor.LightSensor(0)
temperaturesensor = temperaturesensor.TemperatureSensor(2)

run()

