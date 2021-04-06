# Exercise: Upper-casing countries
"""
Let's support our countries by making a new list of upper-case countries.

## Example:
Using the str.upper() method to make an upper-case string:

lower_dog = "dog"
upper_dog = "dog".upper()  # "DOG"
"""

# Raw Data: List the names of origin countries in your team, all in lowercase
lower_countries = ["india", "france", "spain", "germany"]   # e.g. ["finland", "taiwan"]

# Script (fill in here):
upper_countries = []
for country in lower_countries:
    upper_countries.append(country.upper())
   
# Output:
print(upper_countries)
