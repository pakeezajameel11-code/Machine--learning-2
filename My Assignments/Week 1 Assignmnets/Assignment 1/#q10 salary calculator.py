#q10 salary calculator
basic_salary = float(input("enter basic_salary:"))
HRA = (20/100)*(basic_salary)
DA = (15/100)*(basic_salary)
total_salary = basic_salary+HRA+DA
print("House Rent Allaownce is:", HRA)
print("Dearness Allownce is:", DA)
print("total salary is:", total_salary)