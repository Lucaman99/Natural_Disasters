from bs4 import BeautifulSoup
import requests
from matplotlib import pyplot as plt
from types import *

text = []
text2 = []
text3 = []
text4 = []

web = requests.get("http://cdd.publicsafety.gc.ca/rslts-eng.aspx?cultureCode=en-Ca&boundingBox=&provinces=&eventTypes=&eventStartDate=&injured=&evacuated=&totalCost=&dead=&normalizedCostYear=1&dynamic=false")
g = web.content

soup = BeautifulSoup(g, "html.parser")

storage = soup.find_all("td")

for a in storage:
    text.append(a.get_text())

counter = 7

for b in text:
    if (counter%8 == 0):
        text2.append(b)
    counter = counter + 1

other_counter = 4

for b in text:
    if (other_counter%8 == 0):
        if (b != "Unknown"):
            text3.append(b)
        else:
            text3.append(0)
    other_counter = other_counter + 1

oc = 1

for b in text:
    if (oc%8 == 0):
        if (b != "Unknown"):
            text4.append(b[1:].replace(",", ""))
        else:
            text4.append(0)
    oc = oc + 1

print(text4)



finder = ["Earthquake", "Wildfire", "Storm", "Flood", "Landslide", "Tornado", "Avalanche", "Tsunami", "Drought"]
count_array = [0, 0, 0, 0, 0, 0, 0, 0, 0]

over = 0
for j in text2:
    co = 0
    for r in finder:
        if (j.find(r) > 0):
            count_array[co] = count_array[co] + int(text4[over])
        co = co + 1
    over = over + 1

print(count_array)

fi = ["EQ", "WF", "ST", "FL", "LS", "TO", "AV", "TS", "DR"]

plt.bar(fi, count_array, align = 'center')
plt.title("Natural Disasters")
plt.xlabel("Type of disaster")
plt.ylabel("Number")

plt.show()
