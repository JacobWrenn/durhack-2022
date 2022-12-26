from requests import get

API = "https://www.imonnit.com/json/SensorDataMessages"
headers = {
    "APIKeyID" : "oTF7sTKoqA9S",
    "APISecretKey" : "K8m3phtlfC8YOpl0A0evN95rxWAJeSZ7"
}

sensors = {
    "light" : "682607",
    "co2" : "687589",
    "door1" : "829993",
    "door2" : "687113",
    "door3" : "687114",
    "humidity1" : "633384",
    "humidity2" : "683654",
    "vib" : "814111",
    "motion" : "898918",
}

import os
from time import sleep


def getData():
    data = {}

    for k, v in sensors.items():
        PARAMS = {
            "sensorID" : sensors[k],
            "fromDate" : "11/12/2022",
            "toDate" : "11/19/2022"
        }
        d = get(
            url=API,
            headers=headers,
            params=PARAMS
        )
        print(k)
        data[k] = d.json()

        sleep(10)

    if os.path.exists("DATA.py"):
        os.remove("DATA.py")
    with open("DATA.py", "w+") as f:
        f.write(f"data = {str(data)}")

getData()