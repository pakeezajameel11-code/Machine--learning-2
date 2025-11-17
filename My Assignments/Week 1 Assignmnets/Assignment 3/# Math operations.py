# Math operations Programs
# area of a triangle
a = int(input("enter base in cm:"))
b = int(input("entre height in cm:"))
area_of_triangle = 1/2*(a*b)
print("area of a triangle:", area_of_triangle)

#Quotient & Remainder of two numbers
c = int(input("enter num1:"))
d = int(input("entre num2:"))
print("quotient of two numbers:", c/d )
print("remainder of the numbers:", c%d)

#print identity matrix (n)
n = int(input("Enter size: "))
for i in range(n):
    print([1 if i == j else 0 for j in range(n)])


# LCM of two numbers
import math
e = int(input("enter num1:"))
f = int(input("entre num2:"))
lcm = math.lcm(e, f) # Use the built-in math.lcm() function — it directly gives the LCM of two or more numbers.

print("The LCM of", e, "and", f, "is", lcm)

# Sum of first N Natural Numbers
N = int(input("enter natural numbers (n):"))
sum = N*(N+1)/2
print("sum of first N natural numbers:", sum)


# Two numbers that are Amicable numbers or not
num1 = int(input("enter num1:"))
num2 = int(input("entre num2:"))
# find sum of proper divisors using list comprehension
def sum_of_divisors(n):
    return sum([i for i in range(1, n) if n % i == 0])

if sum_of_divisors(num1) == num2 and sum_of_divisors(num2) == num1:
    print(num1, "and", num2, "are amicable numbers")
else:
    print(num1, "and", num2, "are not amicable numbers")

# All perfect square

# check if a number is Armstrong number
# temp = helper variable used to extract digits safely without losing the original number.
# check Armstrong number

num = int(input("Enter a number: "))

# find sum of cubes of digits
sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

# check condition
if num == sum:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")


# All Perfect Square
# program to find all perfect squares in a range

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

# list of all numbers in range
nums = list(range(start, end + 1))
print("Numbers in range:", nums)

# find smallest and largest integers whose square lies in this range
small = int(start ** 0.5)
if small * small < start:
    small += 1

large = int(end ** 0.5)

# list of perfect squares
squares = [i * i for i in range(small, large + 1)]
print("Perfect squares in range:", squares)

# find sum of digits less than 10
squares_sum_lt10 = [sq for sq in squares if sum(int(d) for d in str(sq)) < 10]
print("Squares whose digit-sum < 10:", squares_sum_lt10)

print("Smallest integer:", small)
print("Largest integer:", large)



