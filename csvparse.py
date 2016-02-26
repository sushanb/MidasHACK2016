import csv
mycsv = csv.reader(open('people_01033020100.csv'))
isFirstrow = True
total_population = 0 #variable declaration for Cognitive
cognitive_yes = 0
cognitive_no = 0
cognitive_na = 0
ambu_na=0 #Variable declaration for Ambu
ambu_no=0
ambu_yes=0
for row in mycsv:
	if isFirstrow:
		isFirstrow = False
		continue 
	', '.join(row)
	#cognitive
	drem_value = row[252]
	if drem_value == '1':
		cognitive_yes += 1
	elif drem_value == '2':
		cognitive _no += 1
	else:	
		congnitive_na += 1
	#ambu
	ambu_value = row[249] 
	if ambu_value=='1':  #Yes for Ambu
        	ambu_yes+=1
    	elif ambu_value=='2': #N/A for Ambu
        	ambu_no+=1
    	else: #No for Ambu
        	ambu_na+=1
#total_population is the same for all difficulties
total_population += cognitive_yes + cognitive_no + congnitive_na
#average cognitive difficulty
avg_cogn_yes = (cognitive_yes / total_population) * 10
avg_cogn_no = (cognitive_no / total_population) * 100
avg_cogn_na = (cognitive_ / total_population) * 10
#average ambulatory difficulty
avg_ambu_yes = (ambu_yes / total_population) * 100 
avg_ambu_no = (ambu_no / total_population) * 100
avg_ambu_na = (ambu_na / total_population) * 100




