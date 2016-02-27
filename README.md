# Midas Public Health and Data Visualization Hackathon 2016

Visualizing the ISG Synthetic Ecosystem for MIDAS Public Health Data Visualization
Mapping visual, hearing, cognitive and ambulatory difficulties by state.

We used MIDAS Informatics Services Group's data of synthetic population of the United States. Our goal was to represent the population suffering from visual, cognitive, hearing and ambulatory difficulties. Using this the public health sector can focus on the types of disorders that are more common in their state. 

For analysing the large chunk of datasets that we got from Apollo website(excluding the household csv file) of each counties of United States (which was above 700 GB), we used serial processing python script on a 64 core cluster available at our university Computer Learning and Design Center Lab. The data was mapped, reduced, and dumped to json data suitable for visualization.

For the front end, we are using HTML, CSS, jQuery, core JavaScript. We chose d3js for US states visualization. We were able to visualize the data from the 50 states plus the District of Columbia. 


Contributers:
Saurav K Aryal
Susan Bhattarai
Sumit Dhungel
Swapnil Tamrakar
