from DATA import data
import datetime

nd = {}

for k, v in data.items():
    new = {}
    for r in v["Result"]:
        date = str(datetime.datetime.fromtimestamp(int(r["MessageDate"].strip("/Date()"))/1000))
        new[date] = {}
        for x, y in zip(r["DataTypes"].split("|"), r["PlotValues"].split("|")):
            new[date][x] = y
    nd[k] = new

print(nd)