

"""
# Exercise:
Humans in Europe are expected to live ~81 years.  But they spend a lot that time sleeping--silly humans!
Make a list of how much sleep time each teammate needs to feel rested (per night), then multiply it by the European life expectancy
to get a list of Estimated Sleep Expectancies (in years).

What's the average ESE of your group?
"""

# Raw Data:
sleep_per_night = [7.0, 8.1]  # e.g. [6.5, 9.2, 8, ...]
lifetime = 81.0
days_per_year = 365.0
hours_per_day = 24.0
hours_per_year = days_per_year*hours_per_day

# Script (fill in here):
ese_years = [lifetime*days_per_year*k/hours_per_year for k in sleep_per_night]

# Output:
print(ese_years)
