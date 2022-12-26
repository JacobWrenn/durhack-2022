from flask import Flask, jsonify, request, send_from_directory, url_for, redirect, send_file
from flask_cors import CORS, cross_origin
from DATA import data
import datetime


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


def refreshData():
    global data
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

        #sleep(1)


def proc(d):
    nd = {}
    for k, v in d.items():
        new = {}
        for r in v["Result"]:
            date = str(datetime.datetime.fromtimestamp(int(r["MessageDate"].strip("/Date()"))/1000))
            new[date] = {}
            for x, y in zip(r["DataTypes"].split("|"), r["PlotValues"].split("|")):
                new[date][x] = y
        nd[k] = new
    return nd

dataset = proc(data)

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'











import numpy as np
import random
import math

input_vector1 = np.array([17, 5])
input_vector2 = np.array([1, 6])
# Modified from Durham CT 9.2 Neural Network Example

class NeuralNetwork:
    def __init__(self, learning_rate):
        
        self.weights = np.array([np.random.randn(), np.random.randn()])
        self.bias = np.random.randn()
        self.learning_rate = learning_rate

    def _sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def _sigmoid_deriv(self, x):
        return self._sigmoid(x) * (1 - self._sigmoid(x))

    def predict(self, input_vector):
        layer_1 = np.dot(input_vector, self.weights) + self.bias
        layer_2 = self._sigmoid(layer_1)
        prediction = layer_2
        return prediction

    def _compute_gradients(self, input_vector, target):
        layer_1 = np.dot(input_vector, self.weights) + self.bias
        layer_2 = self._sigmoid(layer_1)
        prediction = layer_2

        derror_dprediction = 2 * (prediction - target)
        dprediction_dlayer1 = self._sigmoid_deriv(layer_1)
        dlayer1_dbias = 1
        dlayer1_dweights = (0 * self.weights) + (1 * input_vector)

        derror_dbias = (
            derror_dprediction * dprediction_dlayer1 * dlayer1_dbias
        )
        derror_dweights = (
            derror_dprediction * dprediction_dlayer1 * dlayer1_dweights
        )

        return derror_dbias, derror_dweights

    def _update_parameters(self, derror_dbias, derror_dweights):
        self.bias = self.bias - (derror_dbias * self.learning_rate)
        self.weights = self.weights - (
            derror_dweights * self.learning_rate
        )

learning_rate = 0.1

def neuralRandom(realValue=21):
    neural_network = NeuralNetwork(learning_rate)

    if neural_network.predict(input_vector1) < 0.5:
        return realValue-(3*(neural_network.predict(input_vector2)))
    else:
        return realValue+(3*(neural_network.predict(input_vector2)))

def neuralRandomType(type, realValue=None):
    if type == 'temp':
        if realValue == None:
            realValue = 21
        mult = 1.5
    if type == 'hum':
        if realValue == None:
            realValue = 44
        mult = 3.5
    if type == 'co2':
        if realValue == None:
            realValue == 200
        mult = 100

    neural_network = NeuralNetwork(learning_rate)

    if neural_network.predict(input_vector1) < 0.5:
        return realValue-(mult*(neural_network.predict(input_vector2)))
    else:
        return realValue+(mult*(neural_network.predict(input_vector2)))








import matplotlib.pyplot as plt
import numpy as np
import datetime



def co2Graph():
    global data
    dates = list(data["co2"].keys())
    CO2s = list(data["co2"].values())
 
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






















@app.route('/')
@cross_origin()
def base():
    return redirect("http://ihatetechdomains.tech:5000/index.html", code=302)

@app.route('/<path:path>')
@cross_origin()
def serveFolder(path):
    return send_from_directory('../client/dist', path)

@app.route('/data')
@cross_origin()
def get_incomes():
    return jsonify(dataset)

@app.route('/refresh')
@cross_origin()
def refreshD():
    global dataset
    refreshData()
    dataset = proc(data)
    return jsonify(dataset)

@app.route('/neuralRandom')
@cross_origin()
def neuralRand():
    return jsonify(neuralRandom())


@app.route('/co2graph')
@cross_origin()
def get_co2graph():
    return send_file("CO2.png")

@app.route('/co2graph_refresh')
@cross_origin()
def refresh_co2graph():
    co2Graph()
    return send_file("CO2.png")


if __name__ == "__main__":
    app.run(host='0.0.0.0')