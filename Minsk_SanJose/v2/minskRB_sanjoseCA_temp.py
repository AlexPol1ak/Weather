import csv
from datetime import datetime
from matplotlib import pyplot as plt

minsk = 'data/minsk_f.csv'
sanjose = 'data/san_jose.csv'

# Извлекаем данные для Минска
with open(minsk) as file1:
	reader1 = csv.reader(file1)
	headers1 = next(reader1)
    # Чтение заголовков. Минск.
	for index1, header1 in enumerate(headers1):
		print(index1,header1)
    # Извлечение дат, максимальных и минимальных температур.Минск
	m_dates, m_highs, m_lows = [], [], []
	i1 = 0
	for row1 in reader1:
		try:
			m_date = datetime.strptime(row1[2], '%Y-%m-%d')
			m_high = int(row1[5])
			m_low = int(row1[6])
		except:
			i1 += 1
			print(f"На дату {m_date} нет данных.")
		else:
			m_dates.append(m_date)
			m_highs.append(m_high)
			m_lows.append(m_low)
	print(f'В файле {file1} отсуствуют данные за: {i1} дней.')


with open(sanjose) as file:
	reader = csv.reader(file)
	headers = next(reader)
	#Чтение заголовков San-Jose.

	for index, header in enumerate(headers):
		print(index, header)
    # Извлечение дат, максимальных и минимальных температур.San-Jose
	s_dates, s_highs, s_lows = [], [], []
	i2 = 0
	for row_s in reader:
		try:
			s_date = datetime.strptime(row_s[1], '%Y-%m-%d')
			s_high = int(row_s[3])
			s_low = int(row_s[4])
		except:
			i2 += 1
			print(f"На дату {s_date} нет данных.")	
		else:
			s_dates.append(s_date)
			s_highs.append(s_high)
			s_lows.append(s_low)
	print(f'В файле {file1} отсуствуют данные за: {i2} дней.')

#Сравнение максимальных температур.
plt.style.use('seaborn')

fig1, max_t = plt.subplots(figsize=(12,10))
max_t.plot(s_dates,s_highs,c='red',linewidth=2, alpha=0.8)
max_t.plot(m_dates,m_highs,c='orange',linewidth=2, alpha=0.8)
max_t.scatter(s_dates, s_highs, s=10, c='red',alpha=0.7)
max_t.scatter(m_dates, m_highs,s=10, c='orange',alpha=0.7,)
#plt.fill_between(m_dates, s_highs, m_highs, facecolor='orange',alpha=0.1)
max_t.set_title("Сравнение максимальных температур.\nSan Jose, Ca (красная линия) - Минск, РБ (оранжевая линия)", fontsize = 24)
max_t.set_xlabel('Дата', fontsize=16)
fig1.autofmt_xdate()
max_t.set_ylabel("Температура (F)", fontsize=16)
plt.tick_params(axis='both', which ='major', labelsize =16)

plt.show()

# Сравнение минимальных температур
fig2, min_t = plt.subplots(figsize=(12,10))
min_t.plot(s_dates,s_lows,c='green',linewidth=2,alpha=0.7)
min_t.plot(m_dates,m_lows,c='blue',linewidth=2, alpha=0.6)
min_t.scatter(s_dates, s_lows, s=10, c='green',alpha=0.7)
min_t.scatter(m_dates, m_lows,s=10, c='blue',alpha=0.7,)
#plt.fill_between(m_dates, s_highs, m_highs, facecolor='orange',alpha=0.1)
min_t.set_title("Сравнение  минимальных температур.\nSan Jose, Ca (зеленая линия) - Минск, РБ (синяя линия)", fontsize = 24)
min_t.set_xlabel('', fontsize=16)
fig2.autofmt_xdate()
min_t.set_ylabel("Температура (F)", fontsize=16)
plt.tick_params(axis='both', which ='major', labelsize =16)

plt.show()
