# 2.Write a Pandas program to split the following dataframe by school code and get mean, min, and max 
# value of age for each school. Also generate a horizontal bar chart based on the result and 
# explain the conclusion.


import pandas as pd
import matplotlib.pyplot as plt

# Create the DataFrame
student_data = pd.DataFrame({
    'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'age': [12, 12, 13, 13, 14, 12],
    'height': [173, 192, 186, 167, 151, 159],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']
})

# Group by 'school_code' and calculate mean, min, and max of age
age_stats = student_data.groupby('school_code')['age'].agg(['mean', 'min', 'max'])

# Print the result
print("Mean, Min, and Max age for each school:")
print(age_stats)

# Plot horizontal bar charts
age_stats.plot(kind='barh', figsize=(10, 6))
plt.xlabel('Age')
plt.title('Mean, Min, and Max Age for Each School')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.legend(title='Statistics')
plt.show()
