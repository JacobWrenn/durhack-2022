import matplotlib.pyplot as plt
from DATA import data as dataA
import numpy as np
import datetime

data = {}

for k, v in dataA.items():
    new = {}
    for r in v["Result"]:
        date = str(datetime.datetime.fromtimestamp(int(r["MessageDate"].strip("/Date()"))/1000))
        new[date] = {}
        for x, y in zip(r["DataTypes"].split("|"), r["PlotValues"].split("|")):
            new[date][x] = y
    data[k] = new



dates = list(data["co2"].keys())
CO2s = list(data["co2"].values())
Humidities = list(map(lambda x: x["Percentage"], data["humidity1"].values()))
Temperature = list(map(lambda x: x["TemperatureData"], data["humidity2"].values()))


for x in range(len(dates)):
    dates[x] = dates[x].split(" ")

DatesCO2 = []

for x in range(0,7):
    time = []
    co2 = []

    for y in range(len(dates)):
        daysAgo = datetime.datetime.strftime(datetime.datetime.today() - datetime.timedelta(days=x), "%Y-%m-%d")
        if dates[y][0] == daysAgo:
            time.append(dates[y][1])
            co2.append(int(CO2s[y]["PPM"]))


    DatesCO2.append([daysAgo, time, co2])


dates = list(data["humidity1"].keys())

for x in range(len(dates[0])):
    dates[x] = dates[x].split(" ")

DatesHumAndTemp = []

for x in range(0,7):
    time = []
    humidities = []
    temperature = []
    
    time2 = []
    humidities2 = []
    temperature2 = []

    for y in range(len(dates)):
        daysAgo = datetime.datetime.strftime(datetime.datetime.today() - datetime.timedelta(days=x), "%Y-%m-%d")
        if dates[y][0] == daysAgo: 
            time.append(dates[y][1])
            humidities.append(Humidities[y])
            temperature.append(Temperature[y])
    

    DatesHumAndTemp.append([daysAgo, time, humidities, temperature])



CO2Plot = plt.subplot2grid((3, 3), (0, 0), rowspan=3, colspan=3)


for y in range(0,7):

    datesArray = []
    for x in range(len(DatesCO2[y][1])):
        datesArray.append(DatesCO2[y][1][x].split(":"))

    actualTime = datesArray

    for x in range(len(datesArray)):
        actualTime[x] = int(datesArray[x][0]) + int(datesArray[x][1]) / 60

    timeGraph = np.array(actualTime)
    CO2Graph = np.array(DatesCO2[y][2])

    CO2Plot.scatter(timeGraph, CO2Graph, s=10)

xMin = 0
xMax = 24
xScale = 1

yMin = 0
yMax = 450
yScale = 50

CO2Plot.set_title("CO2")
CO2Plot.set_xlabel("Time")
CO2Plot.set_ylabel("CO2 / ppm")
CO2Plot.legend([DatesCO2[0][0], DatesCO2[1][0], DatesCO2[2][0], DatesCO2[3][0], DatesCO2[4][0], DatesCO2[5][0], DatesCO2[6][0]])
CO2Plot.set(xlim=(xMin, xMax), xticks=np.arange(xMin, xMax + xScale, xScale), ylim=(yMin, yMax), yticks=np.arange(yMin, yMax + yScale, yScale))

plt.savefig('CO2.png')
CO2Plot.remove()
