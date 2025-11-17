# The Last Algorithm , "AI Science Fiction Story"

#  list all vowels in it
story = input("Enter a story: ")
vowels = "aeiouAEIOU"
words = [w for w in story.split() if any(v in w for v in vowels)]   #.split() divides the story into separate words (by spaces).
print(words)

# list with all nouns in srory
#nouns = str(input("enter nouns:"))
nouns = []

for i in range(4): #how many nouns you want to enter
   word = input("Enter a noun: ")
   nouns.append(word)

print(nouns)

#list with nouns last element should a nested list of numbers in it
nouns = []

for i in range(5): 
    word = input("Enter a noun: ")
    nouns.append(word)

print(nouns)

# tuple with all nouns in it
nouns = tuple()

for i in range(4): 
  word = input("Enter a noun: ")
  nouns += (word),

print(nouns)

# tuple with nouns, last element nested tuple with numbers in it
nouns = tuple()

for i in range(5): 
   word = input("Enter a noun: ")
   nouns += (word),

print(nouns)

#sets with all nouns, last element nested sets with numbers in it
nouns = set()

for i in range(5): 
   word = input("Enter a noun: ")
   nouns.add(word)

print(nouns)

# dictionary with all nouns, last element nested dictionary with numbers in it
nouns = {}

for i in range(5):
     word = input("Enter a noun: ")
     nouns[i + 1] = word   # key = number, value = noun

print(nouns)


