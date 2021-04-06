# Exercise: Upper-casing countries
"""
Let's support our countries by making a new list of upper-case countries.

## Example:
Using the str.upper() method to make an upper-case string:

lower_dog = "dog"
upper_dog = "dog".upper()  # "DOG"
"""

# Raw Data: List the names of origin countries in your team, all in lowercase
lower_countries = ["germany", "united states", "egypt", "china", "netherlands"]   # e.g. ["finland", "taiwan"]

# Script (fill in here):
upper_countries = []
for lower_country in lower_countries:
    upper_countries.append(lower_country.upper())
    
# Output:
print(upper_countries)
