# Homework 2 Report

## Python Code

```python
import pandas as pd

### APARMENT PRICES ###
# Task 1: Calculate the price per square meter

data = pd.read_csv('Booli_sold.csv')

data['ppsqm'] = data['soldPrice'] / data['livingArea']

# Task 2: Rank the top 5 most expensive apartments w.r.t ppsqm
top_5_expensive = data.sort_values(by='ppsqm', ascending=False).head(5)

print(top_5_expensive)

# Task 3: What is the average ppsqm in the dataset?
average_ppsqm = data['ppsqm'].mean()

print(average_ppsqm)

# Task 4: Highlight an aspect of the data that you find interesting. Explain your choice.
# My choice: the maximum rent for apartments. why? Good to know since you are most likely paying your loan and rent together each month
max_rent_index = data['rent'].idxmax()

max_rent_row = data.loc[max_rent_index]

print("Row with Maximum Rent:")
print(max_rent_row)

### THE SWEDISH ELECTION ###

# Task 1: Calculate the total number of legitimate votes

election_data = pd.read_csv('2018_R_per_kommun.csv', sep=';')

eligible_votes = election_data['RÖSTER GILTIGA'].sum()

print(eligible_votes)

# Task 2: Find the index of the maximum votes for 'S'
max_vote_index = election_data['S'].idxmax()

max_vote_kommunnamn = election_data.loc[max_vote_index, 'KOMMUNNAMN']

print("KOMMUNNAMN with Maximum Votes for 'S':", max_vote_kommunnamn)

# Task 3: Rank the (3) municipalities with the highest participation (valdeltagande).
election_data['VALDELTAGANDE'] = pd.to_numeric(election_data['VALDELTAGANDE'], errors='coerce')

top_participation = election_data.sort_values(by='VALDELTAGANDE', ascending=False).head(3)[['KOMMUNNAMN', 'VALDELTAGANDE']]

print("Top 3 Municipalities with Highest Participation:")
print(top_participation)

