import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'

with open(filename) as f:
	file = csv.reader(f)
	reader = next(file)
	print(reader)

	for index, column_header in enumerate(reader):
		print(index,column_header)

	prcp,data = [], []
	for row in file:
		prc_p = float(row[3])
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		prcp.append(prc_p)
		data.append(current_date)

plt.style.use('seaborn')
fig, ax = plt.subplots(figsize=(10,9))
ax.plot(data, prcp, c='blue')
fig.autofmt_xdate()
plt.title('Minimum and maximum precipitation for 2020.Sitka', fontsize=18)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Precipitation', fontsize=14)
plt.tick_params(axis='both', which ='major', labelsize =12)
plt.show()




