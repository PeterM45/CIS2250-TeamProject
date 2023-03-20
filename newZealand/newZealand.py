import pandas as pd

# Read baby names
df = pd.read_csv('baby-names-2023-01-09.csv')
# remove any whitespace and change case of name
df['Name'] = df['Name'].str.strip().str.title()

# separate by gender
boys_df = df[df['Sex'] == 'M']
girls_df = df[df['Sex'] == 'F']

boys_df = df[df['Sex'] == 'M'].copy()
girls_df = df[df['Sex'] == 'F'].copy()

# calculate ranks for boys and girls separately
boys_df.loc[:, 'Rank'] = boys_df.groupby('Year')['Count'].rank(
  ascending=False, method='dense').astype(int)
girls_df.loc[:, 'Rank'] = girls_df.groupby('Year')['Count'].rank(
  ascending=False, method='dense').astype(int)

# sort by year and rank in ascending order
boys_df = boys_df.sort_values(by=['Year', 'Rank'], ascending=[True, True])
girls_df = girls_df.sort_values(by=['Year', 'Rank'], ascending=[True, True])

# create csv files for genders
boys_df[['Rank', 'Year', 'Name', 'Count']].rename(columns={
  'Count': 'Frequency'
}).to_csv('newZealandMales.csv', index=False, lineterminator='\n')
girls_df[['Rank', 'Year', 'Name', 'Count']].rename(columns={
  'Count': 'Frequency'
}).to_csv('newZealandFemales.csv', index=False, lineterminator='\n')
