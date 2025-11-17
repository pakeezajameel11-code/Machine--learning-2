#Dictionary Manipulation
# check if a value exist in a dictionary
my_dict = {'a': 10, 'b': 20, 'c': 30}

if 20 in my_dict.values():
    print("Value exists")
else:
    print("Value not found")

#get the key of a minimum value from dictionary
dict1 = {"maths": 88, "science": 58, "history": 22}
min_value = min(dict1.values())
print("Minimum value is:", min_value)


#delete a list from dictionary
my_dict2 = {"name": "sara", "marks": [75, 66, 89] }
del my_dict2["marks"]
print(my_dict2)

