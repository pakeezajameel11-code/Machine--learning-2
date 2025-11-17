# String manipulation
# check  if a string is a pangram or not
string = input("enter a pangram string:").lower() #.lower convert uppercase into lowercase.
alphabet = "abcdefghijklmnopqrstuvwxyz"
is_pangram = all([letter in  string for letter in alphabet])  #creates a list of True/False values for each letter. #all() returns True only if all letters are found

if is_pangram:
    print("yes, its a pangram.")

else:
    print("No, its not a pangram.") 

# program to replace blanck space with hyphen
string1 = input("enter string:")
string2 = string1.replace(" ", "_") #replace, replaces every space with a hyphen
print("after replacement:", string2)

# program to find larger string without buit function
string2 = input("enter string1:")
string3 = input("enter string2:")

# count lengths manually
count1 = 0
for _ in string2:
    count1 += 1

count2 = 0
for _ in string3:
    count2 += 1     # for string 2 we make a separate variable (count2) and a separate loop to count it.

# compare
if count1 > count2:
    print("First string is larger.")
elif count2 > count1:
    print("Second string is larger.")
else:
    print("Both strings are equal in length.")

# lower and upper case count of a string
string4 = input("enter string:")
upper = len([ch for ch in string4 if ch.isupper()])
lower = len([ch for ch in string4 if ch.islower()])

print("uppercase:", upper)
print("lowercases:", lower)


# Anagram strings, two strings, rearrange srting1 to form sring2
str1 = input("enter string1:").replace(" "," ").lower()  #.replace(" ", "") → removes spaces.
str2 = input("enter string2:").replace(" "," ").lower()  #.lower() ignores uppercase/lowercase differences.
#sorted() arranges letters in order, so both strings can be compared
if sorted(str1) == sorted(str2):
    print("yes strings are anagram:")
else:  
    print("No, the strings are not anagram")


#program check if a substring in a string
string5 = input("enter string:")
substring = input("Enter substring to find: ")

if substring in string5:
    print("Yes, substring found.")
else:
    print("No, substring not found.")

#program to calculate length of a string without liabrary function
string6 = input("enter string:")
count = 0
for _ in string6:
    count +=1

print("lenght of string:", count)

# new string made up of first & last 2 character of string
string7 = input("enter string:")
first_ch = string7[0]
secondlast_ch = string7[-2]
last_ch = string7[-1]

print("new string:", first_ch+secondlast_ch+last_ch)

# program to display which letters in the two strings with but not in both

