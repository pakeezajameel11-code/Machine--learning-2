#Pandas RealEstate data
import pandas as pd
df = pd.read_csv('Week3/RealEstate-USA.csv',delimiter=",", parse_dates=[5],  date_format={'date_added': '%d-%m-%Y'})

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
status = df['status']
print("access the Name column: df : ")
print(status)
print()

# access another  column
house_size = df['house_size']
print("access another column: df : ")
print(house_size)
print()

# access multiple columns
brokeredpriceacre = df[['brokered_by','price',"acre_lot"]]
print("access multiple columns: df : ")
print(brokeredpriceacre)
print()

# .loc works on primary key/property id , if its given in data ok, otherwise code consider primary key by default
#Selecting a single row using .loc #3rdrow 52707, but 4rth row output
row3 = df.loc[2]
print("#Selecting a single row using .loc")
print(row3)
print()

#Selecting multiple rows using .loc #2nd,4rth row, but 3rd 0r 5th row output
selected_rows = df.loc[[1, 3]]
print("#Selecting multiple rows using .loc")
print(selected_rows)
print()

#Selecting a slice of rows using .loc 2 to 6th rows but (3 to 7) / 11 to 16 but 12 to 17
slicedrows = df.loc[1:5]
slicedrows1 = df.loc[10:15]
print("#Selecting a slice of rows using .loc")
print(slicedrows)
print(slicedrows1)
print()
#Conditional selection of rows using .loc
second_row = df.loc[df['bed'] == '5']
print("#Conditional selection of rows using .loc")
print(second_row)
print()

print("# Case 2 : using .loc with index_col - starts here")
# Case 2 : using .loc with index_col - starts here
df_index_col = pd.read_csv('Week3/RealEstate-USA.csv',delimiter=",",parse_dates=[5], date_format={'date_added': '%d-%m-%Y'})

print(df_index_col)
print(df_index_col.dtypes)
print(df_index_col.info())
#Second cycle - with index_col as brokeredby

#Selecting a single row using .loc
sr1 = df_index_col.loc[34632]
print("#Selecting a single row using .loc")
print(sr1)
print()

#Selecting multiple rows using .loc 16 to 20
sr2 = df_index_col.loc[[88441, 109906]]
print("#Selecting multiple rows using .loc")
print(sr2)
print()

#Selecting a slice of rows using .loc 11 to 18
sr3 = df_index_col.loc[65672:51202]
print("#Selecting a slice of rows using .loc")
print(sr3)
print()

#Conditional selection of rows using .loc
#second_row4 = df_index_col.loc[df_index_col['agency'] == 'Gateway Properties']
#print("#Conditional selection of rows using .loc")
#print(second_row4)
#print()



