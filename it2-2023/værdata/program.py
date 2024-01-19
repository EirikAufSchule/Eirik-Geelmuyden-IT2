import datafil
import matplotlib.pyplot as plt
import datetime as dt
import sys
min = []
max = []
mornTemp = []
dayTemp = []
eveTemp = []
nightTemp = []
x = []
for day in datafil.vaerdata["daily"]:
    date = int(str(dt.date.fromtimestamp(day["dt"]))[-2:])
    x.append(date)

    maxTemp = day["temp"]["max"]
    minTemp = day["temp"]["min"] 

    max.append(maxTemp)
    min.append(minTemp)

    mornTemp.append(day["temp"]["morn"])
    dayTemp.append(day["temp"]["day"])
    eveTemp.append(day["temp"]["eve"])
    nightTemp.append(day["temp"]["night"])

    print(date,maxTemp)

plt.fill_between(x,max,min, alpha=.5)
plt.grid()
plt.plot(x, mornTemp, color = "orange", label = "morning")
plt.plot(x, dayTemp, color = "red", label = "day")
plt.plot(x, eveTemp, color = "purple", label = "evening")
plt.plot(x, nightTemp, color = "blue", label = "night")
plt.legend()
plt.show()