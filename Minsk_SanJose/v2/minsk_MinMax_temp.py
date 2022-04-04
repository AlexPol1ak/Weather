import csv
from datetime import datetime
from matplotlib import pyplot as plt

file = 'data/minsk.csv'
with open(file) as f:
	reader = csv.reader(f)
	header = next(reader)

	for index, head in enumerate(header):
		print(index,head)

	t_min,t_max, date = [], [], []
	missing_date = []
	for row in reader:
		date1 = datetime.strptime(row[1], '%Y-%m-%d')
		try:
			temp_min = float(row[10])
			temp_max = float(row[8])
		except:
			print(f"Данные для даты -{date} не найдены ")
			missing_date.append(date1)
		else:
			t_min.append(temp_min)
			t_max.append(temp_max)
			date.append(date1)

plt.style.use('seaborn')
fig, ax = plt.subplots(figsize=(10,9))
ax.plot(date,t_min, c='blue', alpha=0.5)
ax.plot(date,t_max, c='red', alpha=0.5)
plt.fill_between(date, t_max, t_min, facecolor='blue',alpha=0.1)

head = 'Минимальная и максимальная температура по Минску.\n2021.'
plt.title(head, fontsize=16)
plt.xlabel('', fontsize=14)
plt.ylabel('Температура °С',fontsize=14)
fig.autofmt_xdate()
plt.tick_params(axis='both', width=1,which='major',labelsize=12)

plt.show()