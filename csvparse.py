import csv
mycsv = csv.reader(open('people_01033020100.csv'))
isFirstrow = True
for row in mycsv:
	if isFirstrow:
		isFirstrow = False
		continue 
	', '.join(row)
	print row[247] #DEYE 
	print row[246] #Dear
	print row[249] #Ambu
	print row[252] #Congnitive
	





