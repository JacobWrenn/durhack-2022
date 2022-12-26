import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
"""
df = pd.read_csv('RoofSensor.csv', encoding="windows-1252")
df['FormattedValue'].str.split('@', expand=True)
df[['Humidity','Temp']] = df.FormattedValue.str.split("@", expand=True)
for column in ["Temp"]:
    df[column] = df[column].str.replace("ï¿½ C", "")
for column in ["Humidity"]:
    df[column] = df[column].str.replace("%", "")
df[['Date2','Time']] = df.Date.str.split("/2022", expand=True)
df[['Month','Day']] = df.Date2.str.split("/",expand=True)
df["FinalDate"] = df['Day'].astype(str) +"/"+ df["Month"]
df[['Time','PMAM']] = df.Time.str.split("AM",expand=True)
df[['Time','PMAM']] = df.Time.str.split("PM",expand=True)
df[['FinalTime','NaN']] = df.Time.str.split(":",expand=True)
df[['FinalHumidity','FinalNan']] = df.Humidity.str.split('.',expand=True)

df1 = pd.read_csv('StairsSensor.csv', encoding="windows-1252")
df1['Formatted Value'].str.split('@', expand=True)
df1.rename(columns = {'Formatted Value':'FormattedValue'}, inplace = True)
df1[['Humidity','Temp']] = df1.FormattedValue.str.split("@", expand=True)
for column in ["Temp"]:
    df1[column] = df1[column].str.replace("� C", "")
for column in ["Temp"]:
    df1[column] = df1[column].str.replace("° C", "")
for column in ["Humidity"]:
    df1[column] = df1[column].str.replace("%", "")
df1[['Date2','Time']] = df1.Date.str.split("/2022", expand=True)
df1[['Month','Day']] = df1.Date2.str.split("/",expand=True)
df1["FinalDate"] = df1['Day'].astype(str) +"/"+ df1["Month"]
df1[['Time','PMAM']] = df1.Time.str.split("AM",expand=True)
df1[['Time','PMAM']] = df1.Time.str.split("PM", expand=True)
df1[['FinalTime','NaN']] = df1.Time.str.split(":",expand=True)
df1[['FinalHumidity','FinalNan']] = df1.Humidity.str.split('.',expand=True)


columnsDropped = ['DataMessageGUID','Sensor Name','Value','Battery','Raw Data','Sensor State','GatewayID','Alert Sent','Signal Strength','Voltage','FormattedValue','Date','Date2','Month','Day','PMAM','Time','NaN','Humidity','FinalNan']
df.drop(columnsDropped, inplace=True, axis=1)
df1.drop(columnsDropped, inplace=True, axis=1)
df2 = pd.concat([df,df1])
df2 = df2.sort_values(by=['FinalHumidity','FinalTime'])
df2.to_csv('out.csv')

df2_1911 = df2[df2.FinalDate.eq('19/11')]
df2_1811 = df2[df2.FinalDate.eq('18/11')]
df2_1711 = df2[df2.FinalDate.eq('17/11')]
df2_1611 = df2[df2.FinalDate.eq('16/11')]
df2_1511 = df2[df2.FinalDate.eq('15/11')]
df2_1411 = df2[df2.FinalDate.eq('14/11')]
"""


# define csv file location
csv_file14 = '14Sensor.csv'
csv_file15 = '15Sensor.csv'
csv_file16 = '16Sensor.csv'
csv_file17 = '17Sensor.csv'
csv_file18 = '18Sensor.csv'
csv_file19 = '19Sensor.csv'

#create DataFrame from dictionary
interviews1 = pd.read_csv(csv_file14)
interviews2 = pd.read_csv(csv_file15)
interviews3 = pd.read_csv(csv_file16)
interviews4 = pd.read_csv(csv_file17)
interviews5 = pd.read_csv(csv_file18)
interviews6 = pd.read_csv(csv_file19)
#interviews.drop('y', inplace=True, axis=1)

interviews1.plot(kind='scatter', y='Value', x='Time')
plt.axhline(y = 50, color = 'r', linestyle = '-')
plt.savefig('Sensor1411.png')
interviews2.plot(kind='scatter', y='Value', x='Time')
plt.axhline(y = 50, color = 'r', linestyle = '-')
plt.savefig('Sensor1511.png')
interviews3.plot(kind='scatter', y='Value', x='Time')
plt.axhline(y = 50, color = 'r', linestyle = '-')
plt.savefig('Sensor1611.png')
interviews4.plot(kind='scatter', y='Value', x='Time')
plt.axhline(y = 50, color = 'r', linestyle = '-')
plt.savefig('Sensor1711.png')
interviews5.plot(kind='scatter', y='Value', x='Time')
plt.axhline(y = 50, color = 'r', linestyle = '-')
plt.savefig('Sensor1811.png')
interviews6.plot(kind='scatter', y='Value', x='Time')
plt.axhline(y = 50, color = 'r', linestyle = '-')
plt.savefig('Sensor1911.png')
