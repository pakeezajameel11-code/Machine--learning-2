# numpy practice FastFoodRestaurants
import numpy as np
address, city, country, lat, long, name = np.genfromtxt('Week3/FastFoodRestaurants.csv', delimiter=',', invalid_raise=False,  usecols=(0,1,2,4,5,6), unpack=True, dtype=None ,skip_header=1)

print(address)
print(city)
print(country)
print(lat)
print(long)
print(name)


# Perform basic arithmetic operations
addition = long + lat
subtraction = lat - long
#multiplication = long * lat
#division = long / lat

print("fastfood  Long - lat - Addition:", addition)
#print("fastfood  Long - lat - Subtraction:", subtraction)
#print("fastfood Long - lat - Multiplication:", multiplication 
#rint("fastfood Long - lat - Division:", division)
# 2D Array
D2fastfood = np.array([city, 
                         country])
print ("fastfood city and country - 2 dimentional arrary - " ,D2fastfood)
# check the dimension of array1, 
print("fastfood city and country - 2 dimentional arrary - dimension" , D2fastfood.ndim) 
#return total number of elements in array1
print("fastfood city and country 2 dimentional arrary - total number of elements" ,D2fastfood.size) 
#return a tuple that gives size of array in each dimension
print("fastfood city and country - 2 dimentional arrary - gives size of array in each dimension" ,D2fastfood.shape)
# check the data type of array1
print("fastfood city and country- 2 dimentional arrary - data type" ,D2fastfood.dtype) 

D2fastfoodslice=  D2fastfood[:2,:5]
print("fastfood city and country - 2 dimentional arrary - Slicing array - D2realestate[:2,:8]", D2fastfoodslice)
print("fastfood city and country - 2 dimentional arrary - dimension" , D2fastfoodslice.ndim) 

#d3 fastfood address, country and name
D3fastfood = np.array([city, 
                         address,
                         name])
print ("fastfood city, address and name - 3 dimentional arrary - " ,D3fastfood)
# check the dimension of array1, 
print("fastfood city, address and name - 3 dimentional arrary - dimension" , D3fastfood.ndim) 
#return total number of elements in array1
print("fastfood city, address and name 3 dimentional arrary - total number of elements" ,D3fastfood.size) 
#return a tuple that gives size of array in each dimension
print("fastfood city, address and name - 3 dimentional arrary - gives size of array in each dimension" ,D3fastfood.shape)
# check the data type of array1
print("fastfood city, address and name - 3 dimentional arrary - data type" ,D3fastfood.dtype) 

