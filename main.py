import pandas as pd
import csv

df = pd.read_csv('data.csv')
drop_cols = ['ID','NAME','CITY','CPERSON','EMPLCNT','CONTRCOST']
df.drop(columns=drop_cols, axis=1, inplace=True)

country_totals = df.groupby(['COUNTRY']).sum()
country_totals.sort_values(by=['CONTRCNT', 'COUNTRY'], ascending=False, inplace=True)

first_row = country_totals.iloc[0]
country=first_row.name
contracts=first_row.values[0]

print('Country with the largest number of customers\' contracts:')
print(f'{country} ({contracts} contracts)')