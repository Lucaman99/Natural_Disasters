from bs4 import BeautifulSoup
import requests
from matplotlib import pyplot as plt
from types import *

text = []
text2 = []
text3 = []
text4 = []
text5 = []

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

oq = 5

for b in text:
    if (oq%8 == 0):
        text5.append(b)
    oq = oq + 1

print(text5)



finder = ["Earthquake", "Wildfire", "Storm", "Flood", "Landslide", "Tornado", "Avalanche", "Tsunami", "Drought"]
month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

count_array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

over = 0
for j in text5:
    co = 0
    for r in month:
        print(j.find(r))
        if (j.find(r) >= 0):
            count_array[co] = count_array[co] + 1
        co = co + 1
    over = over + 1

print(count_array)

the_data = []

t = 6

for i in range(1, 9):
    the_data.append((1.03**(i))*((count_array[(5+i)%12]*(1+(0.1*i)))/5)*30)

for i in range(9, 17):
    the_data.append((1.1**(i))*((count_array[(5+i)%12]*(1+(0.1*i)))/5)*30)

for i in range(17, 25):
    the_data.append((1.03**(i))*((count_array[(5+i)%12]*(1+(0.1*i)))/5)*30)

print(the_data)

final_data = []

total = 0

final_data.append(the_data[0])

for r in range(1, len(the_data)):
    a = the_data[r] + the_data[r-1]
    final_data.append(a)

print(final_data)

total = 0

for a in final_data:
    total = total + a

print(total/24)



fi = ["EQ", "WF", "ST", "FL", "LS", "TO", "AV", "TS", "DR"]
mo = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

plt.bar(mo, count_array, align = 'center')
plt.title("Natural Disasters")
plt.xlabel("Month")
plt.ylabel("Number")

plt.show()
