import os
import csv
import json

indir = '/home/saurav/MidasHACK2016/'

# Initialize a value dict to be used to store values for each state.
values_dict = {
	'avg_cogn_yes': 0, 
	'avg_cogn_no': 0, 
	'avg_cogn_na': 0, 
	'avg_ambu_yes': 0, 
	'avg_ambu_no': 0, 
	'avg_ambu_na': 0, 
	'vision_difficulty_yes': 0, 
	'vision_difficulty_no': 0, 
	'vision_difficulty_na': 0,
	'avg_hear_yes':0, 
	'avg_hear_no':0, 
	'avg_hear_na':0
}
# Initialize a state dict for final values
state_dict = {
	'HI': {}, 
	'AK': {}, 
	'FL': {}, 
	'SC': {}, 
	'GA': {}, 
	'AL': {}, 
	'NC': {}, 
	'TN': {}, 
	'RI': {}, 
	'CT': {}, 
	'MA': {},
	'ME': {}, 
	'NH': {}, 
	'VT': {}, 
	'NY': {}, 
	'NJ': {}, 
	'PA': {}, 
	'DE': {},
	'MD': {},
	'WV': {},
	'KY': {}, 
	'OH': {}, 
	'MI': {}, 
	'WY': {}, 
	'MT': {},
	'ID': {},
	'WA': {},
	'DC': {},
	'TX': {},
	'CA': {},
	'AZ': {},
	'NV': {}, 
	'UT': {}, 
	'CO': {}, 
	'NM': {}, 
	'OR': {}, 
	'ND': {}, 
	'SD': {}, 
	'NE': {}, 
	'IA': {}, 
	'MS': {}, 	
	'IN': {}, 
	'IL': {}, 
	'MN': {}, 
	'WI': {}, 
	'MO': {}, 
	'AR': {}, 
	'OK': {}, 
	'KS': {}, 
	'LA': {}, 
	'VA': {}
}

for key in state_dict:
	dir_path = indir + key
	isFirstrow = True	#bool to skip first row read
	total_population = 0 #variable declaration for Cognitive
	cognitive_yes = 0
	cognitive_no = 0
	cognitive_na = 0
	ambu_na=0 #Variable declaration for Ambu
	ambu_no=0
	ambu_yes=0
	count_1 = 0#variable declaration for vison difficulty 
	count_2 = 0
	other_count = 0
	hearing_yes = 0 #variable declaration for hearing disability
	hearing_no = 0
	hearing_na = 0
	for file in os.listdir(dir_path):
		mycsv = csv.reader(open(dir_path + '/' + file))
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
				cognitive_no += 1
			#ambu
			ambu_value = row[249] 
			if ambu_value =='1':  #Yes for Ambu
			    ambu_yes+=1
			elif ambu_value == '2':
				ambu_no+=1
		    #Vison effect Deye
		    #Deye for vision
			deye_count = row[247]
			if deye_count == '1':
			    count_1 += 1
			elif deye_count == '2':
			    count_2 += 1
			#Hearing difficulty
			#dear
			dear_value=row[246]
			if dear_value == '1':
			    hearing_yes += 1
			elif dear_value == '2':
			    hearing_no += 1
	#total_population is the same for all difficulties
	total_population = cognitive_yes + cognitive_no + cognitive_na
	#average cognitive difficulty
	avg_cogn_yes = float(cognitive_yes) / total_population * 100 
	avg_cogn_no = float(cognitive_no) / total_population * 100 
	avg_cogn_na = 100.0 - avg_cogn_no - avg_cogn_yes
	#average ambulatory difficulty
	avg_ambu_yes = float(ambu_yes) / total_population * 100  
	avg_ambu_no = float(ambu_no) / total_population * 100 
	avg_ambu_na = 100.0 - avg_cogn_no - avg_cogn_yes
	#average vision difficulty
	vision_difficulty_yes = float(count_1) / total_population * 100 
	vision_difficulty_no = float(count_2)/ total_population * 100 
	vision_na = 100.0 - vision_difficulty_no - vision_difficulty_yes
	#average hearing difficulty
	avg_hear_yes = float(hearing_yes) / total_population * 100
	avg_hear_no = float(hearing_no) / total_population * 100
	avg_hear_na = 100.0 - avg_hear_no - avg_hear_yes
	print '--------------'
	state_dict[key]['avg_cogn_yes'] = avg_cogn_yes	
	state_dict[key]['avg_cogn_no'] = avg_cogn_no
	state_dict[key]['avg_cogn_na'] = avg_cogn_na
	state_dict[key]['avg_ambu_yes'] = avg_ambu_yes
	state_dict[key]['avg_ambu_no'] = avg_ambu_no
	state_dict[key]['avg_ambu_na'] = avg_ambu_na
	state_dict[key]['vision_difficulty_yes'] = vision_difficulty_yes
	state_dict[key]['vision_difficulty_no'] = vision_difficulty_no
	state_dict[key]['vision_na'] = vision_na
	state_dict[key]['avg_hear_yes'] = avg_hear_yes
	state_dict[key]['avg_hear_no'] = avg_hear_no
	state_dict[key]['avg_hear_na'] = avg_hear_na
	#writing all files to a json file.
	with open("data.json","w") as f:
		json.dump(state_dict, f)
	




