import csv
from datetime import datetime

with open('death_valley_2018_simple.csv', 'r') as infile:
    csv_file = csv.reader(infile)
    header_row = next(csv_file)
    
    dv_dates = []
    dv_highs = []
    dv_lows = []
    
    for row in csv_file:
        try:
            high = int(row[header_row.index('TMAX')])
            low = int(row[header_row.index('TMIN')])
            current_date = datetime.strptime(row[header_row.index('DATE')], '%Y-%m-%d')
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dv_dates.append(current_date)
            dv_highs.append(high)
            dv_lows.append(low)

with open('sitka_weather_2018_simple.csv', 'r') as infile:
    csv_file = csv.reader(infile)
    header_row = next(csv_file)
    
    s_dates = []
    s_highs = []
    s_lows = []
    
    for row in csv_file:
        try:
            high = int(row[header_row.index('TMAX')])
            low = int(row[header_row.index('TMIN')])
            current_date = datetime.strptime(row[header_row.index('DATE')], '%Y-%m-%d')
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            s_dates.append(current_date)
            s_highs.append(high)
            s_lows.append(low)

import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

ax1.plot(dv_dates, dv_highs, c='red', alpha=0.5)
ax1.plot(dv_dates, dv_lows, c='blue', alpha=0.5)
ax1.fill_between(dv_dates, dv_highs, dv_lows, facecolor='blue', alpha=0.1)
ax1.set_title('Daily low and high temperatures for Death Valley, CA (2018)', fontsize =12)
ax1.set_xlabel('Dates', fontsize = 12)
ax1.set_ylabel('Temperature (F)', fontsize = 12)

ax2.plot(s_dates, s_highs, c='red', alpha=0.5)
ax2.plot(s_dates, s_lows, c='blue', alpha=0.5)
ax2.fill_between(s_dates, s_highs, s_lows, facecolor='blue', alpha=0.1)
ax2.set_title('Daily low and high temperatures for Sitka, AK (2018)', fontsize = 12)
ax2.set_xlabel('Dates', fontsize = 12)
ax2.set_ylabel('Temperature (F)', fontsize = 12)

plt.show()
