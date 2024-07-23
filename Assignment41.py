#1.Suppose you have a dataset containing daily temperature readings for a city, and you want 
#to identify days with extreme temperature conditions. Find days where the temperature either
#exceeded 35 degrees Celsius (hot day) or dropped below 5 degrees Celsius (cold day). 

import numpy as np

# Input temperature data
temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2, 4.0, 15.5, 6.3, -4.0, -12.0])

# Create masks for hot and cold days
hot_days = temperatures > 35
cold_days = temperatures < 5

# Get indices of hot and cold days
hot_days_indices = np.where(hot_days)[0]
cold_days_indices = np.where(cold_days)[0]

# Create lists of tuples with day and temperature
hot_temperatures_with_days = [(day + 1, temperatures[day]) for day in hot_days_indices]
cold_temperatures_with_days = [(day + 1, temperatures[day]) for day in cold_days_indices]

# Print results
print("Hot Days:")
print("Day    Temperature (°C)")
for day, temp in hot_temperatures_with_days:
    print(f"{day:<6} {temp}")

print("\nCold Days:")
print("Day    Temperature (°C)")
for day, temp in cold_temperatures_with_days:
    print(f"{day:<6} {temp}")


#ANS 
Hot Days:
Day    Temperature (°C)
3      36.8
6      38.7
10     37.2

Cold Days:
Day    Temperature (°C)
11     4.0
14     -4.0
15     -12.0
