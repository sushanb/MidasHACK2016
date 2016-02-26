# MidasHACK2016
Team 
Visualizing the ISG Synthetic Ecosystem for MIDAS Public Health Data Visualization
Mapping visual, hearing, cognitive and ambulatory difficulties by state

We used MIDAS Informatics Services Group's data of synthetic population of the United States. Our goal was to represent the population suffering from visual, cognitive, hearing and ambulatory difficulties.

For analysing the large chunk of datasets that we got from Apollo website(excluding the household csv file) of each counties of United States (which was above 700 GB), we used serial processing on 64 core cluster available at our university CLDC Lab.

We used Python script for reading and selecting the four columns of each CSV fields (visual, cognitive, hearing and ambulatory statistics). After this, we generated a nested dictionary where the state initials were keys and the values were the percentages of population representating our parameters.

When we fully ran our script on all data sheets of 51 states, we generated a JSON file from the nested dictionary.


Contributers:
Saurav K Aryal
Susan Bhattarai
Sumit Dhungel
Swapnil Tamrakar
