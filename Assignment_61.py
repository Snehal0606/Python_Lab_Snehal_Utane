
# 2. Write a Pandas program to create a Pivot table and find the item wise unit sold.

# Assuming the data is in a DataFrame named df
df = pd.read_csv('/content/salesdata.csv')

# Creating a pivot table for item wise unit sold
pivot_units = df.pivot_table(values='Units', 
                             index='Item', 
                             aggfunc='sum')

print("Item-Wise Units Sold:")
print(pivot_units)

#ANS:
Item-Wise Units Sold:
              Units
Item               
Cell Phone      278
Desk             10
Home Theater    722
Television      716
Video Games     395
