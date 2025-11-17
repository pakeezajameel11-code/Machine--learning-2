# List Manipulation
my_list = [22, 34, "car", "bike", 65]
rev_list = my_list[::-1]
print(rev_list)

# list square
list1 = [2, 3, 4, 5, 7, 8]
list2 = [x**2 for x in list1]
print(list2)

#remove empty strings from list
list1 = ["apple", "" "banana", "" "cherry" ""]
lists = [x for x in list1 if x]
print(lists)

# add new item after a specified item
lst = [13, "book", "butter", 25, 32]
lst.insert(2, "bitter")
new = lst
print("adding new item after a specified item:", new)

# replace lists item with new value if found
list = [10, 20, 30, 40, 50]
old_value = 30
new_value = 65
if old_value in list:
    index = list.index(old_value)
    list[index] = new_value

print(list)
