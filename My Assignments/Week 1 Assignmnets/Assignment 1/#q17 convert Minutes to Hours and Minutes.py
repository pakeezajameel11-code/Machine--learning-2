#q17 convert Minutes to Hours and Minutes
minutes = int(input("Enter total minutes: "))
hours = minutes // 60
remaining = minutes % 60         #% means modulus, which gives the remainder
print("Hours:", hours, "Minutes:", remaining)
