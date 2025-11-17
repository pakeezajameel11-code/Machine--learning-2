#string
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

result = letters_in_one_but_not_both(string1, string2)

print("The letters present in one string but not in both are:")
for letter in result:
    print(letter)