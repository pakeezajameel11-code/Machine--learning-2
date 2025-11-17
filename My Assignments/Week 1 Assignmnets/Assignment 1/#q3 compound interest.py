#q3 compound interest
# Simple program to calculate compound interest

# input values
principal = int(input("Enter the principal amount: "))
rate = int(input("Enter the annual interest rate (%): "))
time = int(input("Enter the time (in years): "))
n = int(input("Enter number of times interest is compounded per year: "))

# formula for compound interest
amount = principal * (1 + rate / (100 * n)) ** (n * time)
compound_interest = amount - principal

# output
print("Compound Interest =", compound_interest)
print("Total Amount =", amount)
