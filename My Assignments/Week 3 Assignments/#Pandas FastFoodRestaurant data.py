#Pandas FastFoodRestaurant data
import pandas as pd
df = pd.read_csv('Week3/FastFoodRestaurants.csv',delimiter=",",parse_dates=[5], date_format={'date_added': '%d-%m-%Y'})

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

# access the Name column
address = df['address']
print("access the Name column: df : ")
print(address)
print()

# access another  column
postal_code = df['postalCode']
print("access another column: df : ")
print(postal_code)
print()

# access multiple columns
country_city = df[['country','city']]
print("access multiple columns: df : ")
print(country_city)
print()