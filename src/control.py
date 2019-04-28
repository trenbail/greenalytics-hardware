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
        #  Polls the temperature/humidity sensor for current temp
        temperaturesensor.query_sensor()
        temperature = temperaturesensor.get_temperature()
        humidity = temperaturesensor.get_humidity()

        #  Polls the MCP3008 for the light data
        lightlevel = lightsensor.get_level()

        # Sends a POST request to the API containing Light Data
        light_api.post(lightlevel)

        # Sends a POST request to the API containing the Temperature data
        temperature_api.post(temperature)

        # Sends a Post request to the API containing the Humidity data
        humidity_api.post(humidity)

        print(humidity_api.get_status())
        print(temperature_api.get_status())
        print(light_api.get_status())

        time.sleep(1)


lightsensor = lightsensor.LightSensor(0)
temperaturesensor = temperaturesensor.TemperatureSensor(2)

run()

