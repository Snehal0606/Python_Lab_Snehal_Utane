#Write a Python program and calculate the mean of the below dictionary.

def calculate_mean(input_dict):
    total = 0
    count = 0

    for key in input_dict:
        total += input_dict[key]
        count += 1

    mean = total / count
    return mean

# Example usage
test_dict = {"A": 6, "B": 9, "C": 5, "D": 7, "E": 4}
mean = calculate_mean(test_dict)
print("The mean of the values in the dictionary is:", mean)

#ANS:
The mean of the values in the dictionary is: 6.2