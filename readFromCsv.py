import pandas as pd
import os

#read data from CSV file
with open('cancer_data.csv', 'r') as file:
    #write data to DF choosing necessary columns
    df = pd.read_csv(file,
                     usecols=['cancer_site',
                              'year',
                              'sex',
                              'total_costs',
                              'initial_year_after_diagnosis_cost',
                              'last_year_of_life_cost'])

    #replace names of columns
    df.rename(columns={'total_costs': 'total',
                       'initial_year_after_diagnosis_cost': 'first_year_costs',
                       'last_year_of_life_cost': 'last_year_costs'}, inplace=True)

#calculate the number of years in disease for each patient
df['disease_years'] = round(((df.total - df.first_year_costs) / df.last_year_costs), 1)
#print(df[(df.sex == 'Females')].head())

list_of_years = df['year'].unique()

#create folder for csv files
path = './CSV_files'
ifExists = os.path.exists(path)
if not ifExists:
    os.makedirs(path)

#devide DF to separate CSV files by year
for year in list_of_years:
    #print(df.loc[df['year'] == year])
    df.loc[df['year'] == year].to_csv('./CSV_files/%s.csv' % year)
