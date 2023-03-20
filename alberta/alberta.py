import pandas as pd

# Read baby names from 1980-2020
df = pd.read_csv('./alberta/baby-names-frequency_1980_2020.csv')
# remove any whitespace and change to upper
df['Name'] = df['Name'].str.strip()

# separate by gender
boys_df = df[df['Gender'] == 'Boy']
girls_df = df[df['Gender'] == 'Girl']

boys_df = df[df['Gender'] == 'Boy'].copy()
girls_df = df[df['Gender'] == 'Girl'].copy()

# calculate ranks for boys and girls separately
boys_df.loc[:, 'Rank'] = boys_df.groupby('Year')['Frequency'].rank(
  ascending=False, method='dense').astype(int)
girls_df.loc[:, 'Rank'] = girls_df.groupby('Year')['Frequency'].rank(
  ascending=False, method='dense').astype(int)

# create csv files for genders
boys_df[['Rank', 'Year', 'Name', 'Frequency']].to_csv('./alberta/albertaMales.csv',
                                                      index=False,
                                                      line_terminator='\n')
girls_df[['Rank', 'Year', 'Name', 'Frequency']].to_csv('./alberta/albertaFemales.csv',
                                                       index=False,
                                                       line_terminator='\n')
"""
2021 FILE
"""
# Read baby names from 2021
new_df = pd.read_csv('./alberta/baby-names-frequency_1980_2020.csv')
new_df['Name'] = df['Name'].str.strip()

new_boys_df = new_df[new_df['Gender'] == 'Boy']
new_girls_df = new_df[new_df['Gender'] == 'Girl']

new_boys_df = df[df['Gender'] == 'Boy'].copy()
new_girls_df = df[df['Gender'] == 'Girl'].copy()

# calculate ranks for the new data separately
new_boys_df.loc[:, 'Rank'] = boys_df.groupby('Year')['Frequency'].rank(
  ascending=False, method='dense').astype(int)
new_girls_df.loc[:, 'Rank'] = girls_df.groupby('Year')['Frequency'].rank(
  ascending=False, method='dense').astype(int)

# append the data from this file onto the data from the prev file
with open('./alberta/albertaMales.csv', 'a') as f:
  new_boys_df[['Rank', 'Year', 'Name',
               'Frequency']].to_csv(f,
                                    header=False,
                                    index=False,
                                    line_terminator='\n')

with open('./alberta/albertaFemales.csv', 'a') as f:
  new_girls_df[['Rank', 'Year', 'Name',
                'Frequency']].to_csv(f,
                                     header=False,
                                     index=False,
                                     line_terminator='\n')
