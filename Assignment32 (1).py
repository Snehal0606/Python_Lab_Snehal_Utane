#Write a Python program to get the largest and smallest number from a list without builtin functions.


The largest number in the list is: 8
The smallest number in the list is: -2


** Process exited - Return Code: 0 **
def find_largest_smallest(numbers):
    if not numbers:
        return None, None  # Return None for both if the list is empty

    largest = numbers[0]
    smallest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number
        if number < smallest:
            smallest = number

    return largest, smallest

# Example usage
numbers = [3, 5, 1, 8, -2, 7, 4]
largest, smallest = find_largest_smallest(numbers)
print("The largest number in the list is:", largest)
print("The smallest number in the list is:", smallest)

#ANS:
The largest number in the list is: 8
The smallest number in the list is: -2

