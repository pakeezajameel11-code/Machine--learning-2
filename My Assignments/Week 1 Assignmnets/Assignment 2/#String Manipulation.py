#String Manipulation
#new string
string=input("Enter a new string")
first_character=string[0]
last_character=string[-1]
middle_character=string[len(string)//2]

print(first_character)
print(last_character)
print(middle_character)

print(first_character+middle_character+last_character)

# count occourence of all characters in string
string1 = input("Enter a string: ")

# Create an empty dictionary
count = {}

# Loop through each character in the string
for char in string1:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

# Print the result
for char, freq in count.items():
    print(f"'{char}' : {freq}")

#reverse given string
str = "Butterfly"
rev_str = str[::-1]
print(rev_str)

#split string on hyphen
string1 = "cat-fish-cow"
string2 = string1.split("-")
print(string2)


#remove special symbols
text = input("Enter a string: ")

# Keep only letters, numbers, and spaces
clean_text = ""
for char in text:
    if char.isalnum() or char.isspace():
        clean_text += char

print("String without special symbols or punctuation:")
print(clean_text)