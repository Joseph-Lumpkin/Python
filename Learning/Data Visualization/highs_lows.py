# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 21:34:06 2019

@author: Joseph
"""

import csv
from matplotlib import pyplot as plt
from datetime import datetime as dt

filename = 'var/sitka_weather_2014.csv'

with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	
	for index, column_header in enumerate(header_row):
		print(index, column_header)
		
	#Extract the high temps from the CSV file.
	dates, highs, lows = [], [], []
	for row in reader:
		current_date = dt.strptime(row[0], "%Y-%m-%d")
		dates.append(current_date)
		high = int(row[1])
		highs.append(high)
		low = int(row[3])
		lows.append(low)
		
	print(highs)
	
	#Plotting the data.
	fig = plt.figure(dpi=128, figsize=(10,6))
	plt.plot(dates, highs, c='red', alpha = 0.5)
	plt.plot(dates, lows, c='blue', alpha = 0.5)
	plt.fill_between(dates, highs, lows, facecolor='blue', alpha = 0.1)
	
	#Formatting the plot.
	plt.title("Daily High and Low Temperatures - 2014", fontsize=24)
	plt.xlabel('', fontsize=16)
	fig.autofmt_xdate()
	plt.ylabel("Temperature (F)", fontsize=16)
	plt.tick_params(axis='both', which='major', labelsize=16)
	
	plt.show()