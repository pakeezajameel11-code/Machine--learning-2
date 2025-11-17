#Tuple Manipulaton
my_tuple = (10, 20, 30, 40, 50)
reversed_tuple = my_tuple[::-1]
print("Reversed tuple:", reversed_tuple)

#access value 20 from tuple
value= my_tuple[1]
print("accessing value 20:", value)

# swap two tuples
tup1 = ("car", "bike", "plane")
tup2 = (30, 40, 50)
# swap the tuples
tup1, tup2 = tup2, tup1
print("\nAfter swapping:")
print("tuple1 =", tup1)
print("tuple2 =", tup2)

