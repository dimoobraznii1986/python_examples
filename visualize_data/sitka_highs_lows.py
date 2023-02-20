from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('weather_data/sitka_weather_2014.csv')
lines = path.read_text().splitlines()


reader = csv.reader(lines)
header_row = next(reader)

# Extract dates and high temperatures.
dates, highs, lows = [], [], []
for row in reader:
    try:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        high = int(row[1])
        low = int(row[3])
    except ValueError:
        print(f"Missing data fror {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Plot the high temperatures
plt.style.use('seaborn')

fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
ax.plot(dates,highs, color='red')
ax.plot(dates,lows, color='blue')

# Format plot
ax.set_title("Daily High and Low Temperatures, 2021, fontsize=24")
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)



plt.show()