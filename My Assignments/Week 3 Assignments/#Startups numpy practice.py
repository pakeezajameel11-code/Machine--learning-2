#startups numpy practice
import numpy as np

company, valuation, date_joined, industry, select_investors = np.genfromtxt('Week3/Startups in 2021 end (1).csv', delimiter=',', usecols=(1,2,3,6,7), unpack=True, dtype=None,skip_header=1)

print(company)
print(valuation)
print(date_joined)
print(industry)
print(select_investors)

# for stats operations on valuation, first convert valuation's strings values into  integer,(float values)
# by using list comprehension, (dollar sign skip by slicing and indexing s[1:]) so it takes whole value as int as given index is 1, and skip the dollar sign (index 0)
# then pass the values in an array by type conversion for furthur operations

valuationnum_strings = np.array([s[1:] for s in valuation])
valnum_array = valuationnum_strings.astype(float)
print(valnum_array)
# applying stats opration on valuation column
print("Startsups valuation mean: " , np.mean(valnum_array))
print("Startsups valuation mean: " , np.average(valnum_array))
print("Startsups valuation standard deviation: " , np.std(valnum_array))
print("Startsups valuation median: " , np.median(valnum_array))
print("Startsups valuation mean:" , np.min(valnum_array))
print("Startsups valuation max: " , np.max(valnum_array))
#startups valuation  - maths operations
print("Startsups valuation square: " , np.square(valnum_array))
print("Startsups valuation sqrt: " , np.sqrt(valnum_array))
print("Startsups valuation pow: " , np.power(valnum_array))
print("Startsups valuation abs: " , np.abs(valnum_array))


#2d array
D2Startups = np.array([company, 
                         select_investors])
print ("startups company and select investor - 2 dimentional arrary - " ,D2Startups)
# check the dimension of array1, 
print("startups company and select investor - 2 dimentional arrary - dimension" , D2Startups.ndim) 
#return total number of elements in array1
print("startups company and select investor 2 dimentional arrary - total number of elements" ,D2Startups.size) 
#return a tuple that gives size of array in each dimension
print("startups company and select investor - 2 dimentional arrary - gives size of array in each dimension" ,D2Startups.shape)
# check the data type of array1
print("startups company and select investor- 2 dimentional arrary - data type" ,D2Startups.dtype) 

#slicing array
D2StartupsSlice =  D2Startups[:2,:8]
print("startups company and select investor - 2 dimentional arrary - Slicing array - D2realestate[:2,:8]", D2StartupsSlice)
print("startups company and select investor - 2 dimentional arrary - dimension" , D2StartupsSlice.ndim) 

# Indexing array
D2StartupsSliceItemOnly=  D2StartupsSlice[0,1]
print("startups company and select investor- 2 dimentional arrary - Index array - D2LongLatSlice[1,5] " , D2StartupsSliceItemOnly)
D2StartupsSlice2ItemOnly=  D2StartupsSlice[0, 2]
print("startups company and select investor - 2 dimentional arrary - index array - D2LongLatSlice2[0, 2] " , D2StartupsSlice2ItemOnly)

#