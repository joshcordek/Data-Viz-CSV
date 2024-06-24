# 1)changing the file to include all the data for the year of 2018
# 2) change the title to - Daily and low high temperatures - 2018
# 3) extract low temps from the file and add to chart
# 4) shade in the area between high and low



import csv
from datetime import datetime

infile = open('sitka_weather_2018_simple.csv', 'r')

csv_file = csv.reader(infile)

header_row = next(csv_file)

print(header_row)

for index, col_header in enumerate(header_row):
    print(index, col_header)


highs = []
dates= []
lows = []


some_date = datetime.strptime('2018-07-01', '%Y-%m-%d')
print(some_date)



for row in csv_file:
    highs.append(int(row[5]))
    lows.append(int(row[6]))
    some_date = datetime.strptime(row[2], '%Y-%m-%d')
    dates.append(some_date)

print(highs[:5])
print(dates[:5])

import matplotlib.pyplot as plt

fig = plt.figure()

plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c ='blue', alpha =0.5)



plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha=0.1)

plt.title("Daily low and high temperatures - 2018", fontsize= 16)
plt.xlabel("Dates", fontsize=16)
plt.ylabel("Temps (F)", fontsize= 16)
plt.tick_params(axis= "both", which="major", labelsize=16)

fig.autofmt_xdate()

plt.show()


plt.subplot(2,1,1)
plt.plot(dates,highs, c='red')
plt.title("Highs")

plt.subplot(2,1,2)
plt.plot(dates,lows, c='blue')
plt.title("Lows")

plt.suptitle("Highs and Lows for Sitka, Alaska")

plt.show()