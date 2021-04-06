
"""
# Exercise:
Humans in Europe are expected to live ~81 years.  But they spend a lot that time sleeping--silly humans!
Make a list of how much sleep time each teammate needs to feel rested (per night), then multiply it by the European life expectancy
to get a list of Estimated Sleep Expectancies (in years).

What's the average ESE of your group?
"""

# Raw Data:
sleep_per_night = [7, 8.5,8]  # e.g. [6.5, 9.2, 8, ...]

# Script (fill in here):
ese_years=[]
for sleep in sleep_per_night:
    ese_year=81*sleep/24
    ese_years.append(ese_year)


    
# Output:
print(ese_years)
