USD = input("Enter Amount in USD (e.g. 50$): ")

# remove $ sign if present
USD = USD.replace("$", "")

# convert to number
USD = int(USD)

PKR = 284.34
Convert = USD * PKR
print( Convert )


