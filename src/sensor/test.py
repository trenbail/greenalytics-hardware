import requests
tempdict = {"Temp":"temp", "Temp1":"temp1"}


r = requests.post(url="http://192.168.1.132:55431/api/plantgroup/hardware/light", json={"HardwareMAC":"34:00:00:23", "UTCTime":"420000", "SensorValue": 421})

print(r.url)