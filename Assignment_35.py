
#Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen.

file_name = r"F:\Anudip_Fooundation\dataAnalysis.txt"
f = open(file_name)
data = f.read()
f.close()

