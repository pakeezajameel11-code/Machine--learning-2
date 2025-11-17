# list Operation
# python program to find the largets number in a list
list = [45, 36, 16, 78, 92, 45]
largest = max(list)
print("The largest number is:", largest)

#print 2nd largest number from list
list2 = list(map(int, input("Enter numbers: ").split()))

largest = max(list2)
list2.remove(largest)
second_largest = max(list2)

print("2nd largest number:", second_largest)

# largest even and largest odd number from that list
list3 = list(map(int, input("Enter numbers: ").split()))

even = [n for n in list3 if n % 2 == 0]
odd = [n for n in list3 if n % 2 != 0]

if even:
    print("Largest even number:", max(even))
else:
    print("No even number in the list.")

if odd:
    print("Largest odd number:", max(odd))
else:
    print("No odd number in the list.")

#average of the list
list4 = list(map(int, input("Enter numbers: ").split()))

average = sum(list4) / len(list4)

print("Average of the list:", average)

#count occurrence of element in the list
list5 = list(map(int, input("Enter numbers: ").split()))   
element = int(input("Enter the element to count: "))    ##numbers.count(element), counts how many times that element appears.

count = list5.count(element)

print(f"{element} occurs {count} times in the list.")  #f"{element} occurs {count} times",  prints neatly using f-string.

#union of two list
list6 = list(map(int, input("Enter first list: ").split()))
list7 = list(map(int, input("Enter second list: ").split()))

union_list = list(set(list6) | set(list7))  #  | → union operator for sets (combines both without repeating elements).
print("Union of two lists:", union_list)

# swap the first and last element of list
numbers = list(map(int, input("Enter numbers: ").split()))
numbers[0], numbers[-1] = numbers[-1], numbers[0]

print("List after swapping:", numbers)

#remove duplicate from list
list8 = list(map(int, input("Enter numbers: ").split()))
new_list = list(set(numbers))      #set(numbers) → removes all duplicate elements automatically
print("List after removing duplicates:",new_list)

#return the length of the longest word from the list
listwords = input("Enter words separated by space: ").split()
longest = max(listwords, key=len)

print("The longest word is:", longest)
print("Length of the longest word:", len(longest))


#program to generate random numbers from 1 to 20 and append them to the list
import random
list9 = [random.randint(1, 20) for i in range(10)]
print("Random numbers list:", list9)

#