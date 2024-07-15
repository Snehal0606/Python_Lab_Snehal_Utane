#Write a Python program to get the key, value and item in a dictionary.

# Define a dictionary
sample_dict = {
    'name': 'Snehal',
    'age': 26,
    'occupation': 'Data Analyst',
    'location': 'India'
}

# Iterate through the dictionary to get key, value, and item
for key, value in sample_dict.items():
    print(f"Key: {key}, Value: {value}, Item: ({key}, {value})")
    

#ANS:

Key: name, Value: Snehal, Item: (name, Snehal)
Key: age, Value: 26, Item: (age, 26)
Key: occupation, Value: Data Analyst, Item: (occupation, Data Analyst)
Key: location, Value: India, Item: (location, India)
