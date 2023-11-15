# My Data Science Journey

## Previous Experience
My background in data analysis mostly revolves around worked on various projects involving data exploration, statistical analysis and modeling. 


## Fun with Data: Exploring a Random Dataset


### Steps to Retrieve the Data:

1. **Search for a dataset relating to ice cream:**
   I performed a quick search for ice cream and dataset" and found a dataset on kaggle. 

2. **Download the dataset:**
   I downloaded the dataset from website, saving it as a CSV file named `Ice Cream Sales and Temperature.csv`.

### Python Code to Generate a Plot:

```python
import pandas as pd
import matplotlib.pyplot as plt

# data set
file_path = 'Contacts/Ice Cream Sales and Temperature.csv'

# Variables of interest 
column_names = ['Temperature (Celsius)', 'Ice Cream Sales']

# Load the dataset into a DataFrame
ice_cream_df = pd.read_csv(file_path, names=column_names, skiprows=1)

# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(ice_cream_df['Temperature (Celsius)'], ice_cream_df['Ice Cream Sales'], c='green', label='Ice Cream Sales')
plt.title('Ice Cream Sales vs. Temperature')
plt.xlabel('Temperature (°C)')
plt.ylabel('Revenue ($)')
plt.legend()
plt.show()
