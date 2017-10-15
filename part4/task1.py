import pandas as pd
import numpy as np

"""
This assignment includes data i/o using python and a bit of data wrangling
This will be helpful for your final mini project.
All the useful datasets are present inside data folder
"""

#1
# read csv_sample1.csv using read_csv function and store in df1
df1 = pd.read_csv('data/csv_sample1.csv')

#2
# read  csv_sample1.csv using read_table function and store in df2
df2 = pd.read_table('data/csv_sample1.csv')

#3
# read csv_sample2.csv using read_csv without header and store in df3
df3 = pd.read_csv('data/csv_sample2.csv', header=None)


#4
"""
read csv_sample2.csv in df4
rename the columns as "new_col1", "new_col2", "new_col3", "new_col4" and "new_value"
assign new_value column as index
"""
df4 = pd.read_csv('data/csv_sample2.csv', index_col='new_value', names = ["new_col1", "new_col2", "new_col3", "new_col4", "new_value"])

#5
# read space_sep.txt using read_table and store in df5
df5 = pd.read_table('data/space_sep.txt')

#6
# read skip_row.csv using read_csv while skipping the rows 0, 2, 3 and 6
df6 = pd.read_csv('data/skip_row.csv', skiprows=[0,2,3,6])

#7
# read null_data.csv in df7. Drop the rows with null values. store the resulting data frame in df8
df7 = pd.read_csv('data/null_data.csv')
df8 = df7.dropna()

#8
# fill the null values in df7 using with 1000 and name the new data frame df8

df8 = df7.fillna(value=1000)

#9
# use forward to fill the null values in df7 data frame

df8 = df7.fillna(method='ffill')


#10
df9 = pd.DataFrame({'col1':[1,2,np.nan,4,5], 'col2':[9,np.nan,7,6,5]})
# fill the nan values of df9 with mean of column
df9.fillna(df9.mean())
