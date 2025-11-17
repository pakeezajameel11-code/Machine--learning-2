#Loop ManipulatiOn
# first 10 natural no using while loop
i = 1
print("first 10 natural numbers")
while i <= 10:
    print(i)
    i+=1

#input user, print even no till that input
n = int(input("enter value:"))
for i in range(2, n + 1, 2):
    print(i)

#input user, print odd no till that input 
n = int(input("enter value:"))
print("odd numbers:")
for i in range(1, n + 1, 2):
    print(i)

#input user, print prime no till that input   
print("prime numbers")
n = int(input("enter value:"))
for num in range(2, n + 1):   #Outer loop, goes through numbers 2 to n
    for i in range(2, num):   #Inner loop, checks if num is divisible by any smaller number
        if num % i == 0:       
            break
    else:                   #The else after for runs only if no break occurs, meaning the number is prime
        print(num)

# Multiplication table of given number      
n = int(input("enter value:"))
for i in range(1, 11):
    print(n, "x", i, "=", n * i)
