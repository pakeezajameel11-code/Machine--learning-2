#copy code
import numpy as np

data = np.genfromtxt(
    "Week3/FastFoodRestaurants.csv",
    delimiter=",",
    names=True,
    dtype=None,       # auto detect types
    encoding="utf-8"
)

print(data.dtype.names)   # show available columns

# Access directly:
addresses = data["address"]
cities = data["city"]
countries = data["country"]
names = data["name"]
postalcodes = data["postalCode"].astype(str)
websites = data["websites"]

print(names[:5], cities[:5])
