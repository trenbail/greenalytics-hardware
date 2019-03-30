"""
Here is where the controller will live for the hardware
"""

import time
from getmac import get_mac_address
from greenaliticsapi import APIInterface
from sensor import lightsensor
from sensor import temperaturesensor


def run():
    postData = APIInterface()

    paramdict = {"UTCTime": time.time(), "MACID": get_mac_address(), "SensorValue": None}
    while True:
        tempsensor.query_sensor()
        temperature = tempsensor.get_temperature()
        temperature = temperature * 9/5 + 32
        humidity = tempsensor.get_humidity()

        lightlevel = lightsensor.get_level()

        paramdict.update({"UTCTime": time.time(), "SensorValue": temperature})
        #postData.post("greenalytics.ga:5000/api/hardware/temperature" , data=paramdict)
        print(paramdict)

        paramdict.update({"UTCTime": time.time(), "SensorValue": humidity})
        #postData.post("greenalytics.ga:5000/api/hardware/humidity", data=paramdict)
        print(paramdict)

        paramdict.update({"UTCTime": time.time(), "SensorValue": lightlevel})
        #postData.post("greenalytics.ga:5000/api/hardware/light", data=paramdict)
        print(paramdict)

        #print("Temperature= {} Humidity = {}".format(temperature, humidity))
        #print("Light Level = {}\n\n".format(lightlevel))

        time.sleep(1)

lightsensor = lightsensor.LightSensor(0)
temperaturesensor = temperaturesensor.TemperatureSensor(2)


run()

