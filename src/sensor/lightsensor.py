"""
In this file will be the integration of the light sensor
"""
from gpiozero import MCP3008


class LightSensor:
    def __init__(self, channel):
        self.channel = channel
        self.value = None

    def get_level(self):
        level = MCP3008(self.channel, max_voltage=5)
        return level.raw_value
