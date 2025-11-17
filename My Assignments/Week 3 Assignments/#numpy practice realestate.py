#numpy practice realestate
import numpy as np
brokered_by, status, price, bed = np.genfromtxt('Week3/RealEstate-USA.csv', delimiter=',', usecols=(0,1,2,3), unpack=True, dtype=None,skip_header=1)
print(brokered_by)
print(status)
print(price)
print(bed)
# real state data statistics operations
print("Realestate Price mean: " , np.mean(price))
print("Realestate Price average: " , np.average(price))
print("Realestate Price std: " , np.std(price))
print("Realestate Price median: " , np.median(price))
print("Realestate Price percentile - 25: " , np.percentile(price,25))
print("Realestate Price percentile  - 75: " , np.percentile(price,75))
print("RealestatePrice percentile  - 3: " , np.percentile(price,3))
print("RealestatePrice min : " , np.min(price))
print("Realestate Price max : " , np.max(price))
print("Realestate Price pow: " , np.power(price,price))

# 2d array
D2realestate = np.array([brokered_by, 
                         price])
print ("realestate brokered by and price - 2 dimentional arrary - " ,D2realestate)
print(" realestate brokered by and price 2 dimentional arrary - total number of elements" ,D2realestate.size)
D2realestateSlice=  D2realestate[:2,:8]
print("realestate brokered by and price - 2 dimentional arrary - Slicing array - D2realestate[:2,:8]", D2realestateSlice)
print("realestate brokered by and price - 2 dimentional arrary - dimension" , D2realestate.ndim)

# 2D array combo of bed and price
D2realestate1 = np.array([bed,
                          price])
print ("realestate bed and price - 2 dimentional arrary - " ,D2realestate1)
print ("realestate bed and price - 2 dimentional arrary - " ,D2realestate1.ndim)
print(" realestate bed  and price 2 dimentional arrary - total number of elements" ,D2realestate1.size)
print ("realestate bed  and price - 2 dimentional arrary - " ,D2realestate1.shape)

#trying 3d array 
D3realestate = np.array([brokered_by,
                         price,
                         bed])
print ("realestate brokered by, price and bed - 3 dimentional arrary - " ,D3realestate)
print ("realestate brokered by and price and bed - 3 dimentional arrary - " ,D3realestate.ndim)
print ("realestate brokered by and price and bed - 3 dimentional arrary total no of elements - " ,D3realestate.size)
print ("realestate brokered by and price and bed - 3 dimentional arrary shape - " ,D3realestate.shape)

# trignometric Functions
pricePie = (price/np.pi) +1
# Calculate sine, cosine, and tangent
sine_values = np.sin(pricePie)
cosine_values = np.cos(pricePie)
tangent_values = np.tan(pricePie)

print("realestate Price - div - pie  - Sine values:", sine_values)
print("realestate Price - div - pie Cosine values:", cosine_values)
print("realestate Price - div - pie Tangent values:", tangent_values)

print("realestate Price - div - pie  - Exponential values:", np.exp(pricePie))

# Calculate the natural logarithm and base-10 logarithm
log_array = np.log(pricePie)
log10_array = np.log10(pricePie)

print("realestate Price - div - pie  - Natural logarithm values:", log_array)
print("realestate Price - div - pie  = Base-10 logarithm values:", log10_array)
#loops
#You should use the builtin function nditer, if you don't need to have the indexes values.
for elem in np.nditer(D2realestate):
    print(elem)

#EDIT: If you need indexes (as a tuple for 2D table), then:
for index, elem in np.ndenumerate(D2realestate):
    print(index, elem)

#loops on 3d
#You should use the builtin function nditer, if you don't need to have the indexes values.
for elem in np.nditer(D3realestate):
    print(elem)

#EDIT: If you need indexes (as a tuple for 2D table), then:
for index, elem in np.ndenumerate(D3realestate):
    print(index, elem)
