#Panadas Startups data
import pandas as pd
df = pd.read_csv('Week3/Startups in 2021 end (1).csv',delimiter=",",parse_dates=[5], date_format={'date_added': '%d-%m-%Y'})

print(df)

print("df - data types" , df.dtypes)

print("df.info():   " , df.info() )

# display the last three rows
print('Last five Rows:')
print(df.tail(5))

# display the first three rows
print('First five Rows:')
print(df.head(5))
print()

#Summary of Statistics of DataFrame using describe() method.
print("Summary of Statistics of DataFrame using describe() method", df.describe())

#Counting the rows and columns in DataFrame using shape(). It returns the no. of rows and columns enclosed in a tuple.
print("Counting the rows and columns in DataFrame using shape() : " ,df.shape)
print()

#Access Columns by name

