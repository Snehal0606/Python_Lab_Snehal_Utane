
# Write a function in Python to count and display the total number of words in a text file “ABC.txt”


file_path = r"F:\Anudip_Fooundation\dataAnalysis.txt"

total_words = 0

with open(file_path, 'r') as file:
    for line in file:
        words = line.split()
        total_words += len(words)

print(f"Total number of words: {total_words}")

ANS:
    Total number of words: 2
