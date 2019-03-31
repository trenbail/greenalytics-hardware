"""
Here is where the the interface for the API will be.
"""
import time
import requests
from getmac import get_mac_address


class APIInterface:
    def __init__(self,url):
        self.url = url
        self.lastPost = None
        self.lastSent = {"HardwareMAC": get_mac_address(), "UTCTime": time.time(), "SensorValue": None}

    def post(self,value):
        self.lastSent.update({"UTCTime": round(time.time()), "SensorValue": round(value)})
        temp = requests.post(self.url, json=self.lastSent)
        self.lastPost = temp
        return temp

    def get_status(self):
        return self.lastPost.status_code

    def get_last_sent(self):
        return self.lastSent
