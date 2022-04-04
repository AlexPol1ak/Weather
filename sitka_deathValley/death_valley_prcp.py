import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	title = next(reader)

	for index, header in enumerate(title):
		print(index, header)

	dates, prcp = [], []
	for row in reader:
		date = datetime.strptime(row[2], '%Y-%m-%d')
		p_rcp = float(row[3])
		dates.append(date)
		prcp.append(p_rcp)

plt.style.use('seaborn')
fig, ax = plt.subplots(figsize=(10,9))
ax.plot(dates,prcp, c='blue')
plt.title('Precipitation. Death Valley .2020', fontsize=16)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Precipitation', fontsize=14)
fig.autofmt_xdate()
plt.tick_params(axis='both', which ='minor',width=1, labelsize =12)
plt.show()

