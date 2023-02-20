from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('weather_data/sitka_weather_2014.csv')
lines = path.read_text().splitlines()


reader = csv.reader(lines)
header_row = next(reader)

# Extract dates and high temperatures.
dates, highs = [], []
for row in reader:
    current_date = datetime.strptime(row[0], '%Y-%m-%d')
    high = int(row[1])
    dates.append(current_date)
    highs.append(high)

# Plot the high temperatures
plt.style.use('seaborn')

fig, ax = plt.subplots()
ax.plot(dates,highs, color='red')

# Format plot
ax.set_title("Daily High Temperatures, 2021, fontsize=24")
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)



plt.show()

