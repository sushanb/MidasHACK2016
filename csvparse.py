import csv
mycsv = csv.reader(open('people_01033020100.csv'))
isFirstrow = True
total_population = 0
cognitive_yes = 0
cognitive_no = 0
cognitive_na = 0
for row in mycsv:
	if isFirstrow:
		isFirstrow = False
		continue 
	', '.join(row)

	print row[247] #DEYE 
	print row[246] #Dear
	print row[249] #Ambu
	drem_value = row[252]
	if drem_value == '1':
		cognitive_yes += 1
	elif drem_value == '2':
		cognitive _no += 1
	else:	
		congnitive_na += 1

total_population += cognitive_yes + cognitive_no + congnitive_na

avg_cogn_yes = (cognitive_yes / total_population) * 10
avg_cogn_no = (cognitive_no / total_population) * 100
avg_cogn_na = (cognitive_ / total_population) * 10




