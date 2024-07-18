#Write a Python program to sum all the items in a list.

def sum_of_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

# Example usage
numbers = [1, 2, 3, 4, 5]
print("The sum of the list is:", sum_of_list(numbers))


#ANS:
The sum of the list is: 15