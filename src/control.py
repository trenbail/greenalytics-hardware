"""
Here is where the controller will live for the hardware
"""

import time
import requests
from getmac import get_mac_address
from greenaliticsapi import APIInterface
from sensor import lightsensor
from sensor import temperaturesensor


def run():
    postData = APIInterface()

    paramdict = {"HardwareMAC": get_mac_address(),"UTCTime": time.time(), "SensorValue": None}
    while True:
        temperaturesensor.query_sensor()
        temperature = temperaturesensor.get_temperature()
        temperature = temperature * 9/5 + 32
        humidity = temperaturesensor.get_humidity()

        lightlevel = lightsensor.get_level()

        paramdict.update({"UTCTime": round(time.time()), "SensorValue": round(temperature)})
        postData.post("http://greenalytics.ga:5000/api/hardware/temperature", paramdict)
        print(postData.status_code)

        paramdict.update({"UTCTime": round(time.time()), "SensorValue": round(humidity)})
        postData.post("http://greenalytics.ga:5000/api/hardware/humidity", paramdict)
        print(postData.status_code)

        paramdict.update({"UTCTime": round(time.time()), "SensorValue": lightlevel})
        postData.post("http://greenalytics.ga:5000/api/hardware/light", paramdict)
        print(postData.status_code)

        print("Temperature= {} Humidity = {}".format(temperature, humidity))
        print("Light Level = {}\n\n".format(lightlevel))

        time.sleep(1)


lightsensor = lightsensor.LightSensor(0)
temperaturesensor = temperaturesensor.TemperatureSensor(2)


run()

