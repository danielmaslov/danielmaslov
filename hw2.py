import pandas as pd

data = pd.read_csv('Booli_sold.csv')

data['ppsqm'] = data['soldPrice'] / data['livingArea']



top_5_expensive = data.sort_values(by='ppsqm', ascending=False).head(5)

print(top_5_expensive)

average_ppsqm = data['ppsqm'].mean()

print(average_ppsqm)

# What is the maximum rent? good to know since you are most likelt paying your loan and rent togheter each month
max_rent_index = data['rent'].idxmax()

max_rent_row = data.loc[max_rent_index]


print("Row with Maximum Rent:")
print(max_rent_row)


#Task 2

election_data = pd.read_csv('2018_R_per_kommun.csv', sep=';')

eligable_votes = election_data['RÖSTER GILTIGA'].sum()

#print(eligable_votes)

# Find the index of the maximum votes for 'S'
max_vote_index = election_data['S'].idxmax()

max_vote_kommunnamn = election_data.loc[max_vote_index, 'KOMMUNNAMN']

print("KOMMUNNAMN with Maximum Votes for 'S':", max_vote_kommunnamn)


election_data['VALDELTAGANDE'] = pd.to_numeric(election_data['VALDELTAGANDE'], errors='coerce')

# Sort the DataFrame by 'VALDELTAGANDE' in descending order and select the top 3
top_participation = election_data.sort_values(by='VALDELTAGANDE', ascending=False).head(3)[['KOMMUNNAMN', 'VALDELTAGANDE']]

# Print the result
print("Top 3 Municipalities with Highest Participation:")
print(top_participation)

