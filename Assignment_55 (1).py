2.Write a Pandas program to create and display a DataFrame from a specified dictionary data which has the index labels. 
Sample Python dictionary data and list labels: 
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19], 
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], 
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']} ?


import pandas as pd
import numpy as np

# Sample data
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}

# Index labels
index_labels = ['student1', 'student2', 'student3', 'student4', 'student5', 'student6', 'student7', 'student8', 'student9', 'student10']

# Create DataFrame with index labels
df = pd.DataFrame(exam_data, index=index_labels)

# Display DataFrame
print(df)

#ANS:
                name  score  attempts qualify
student1   Anastasia   12.5         1     yes
student2        Dima    9.0         3      no
student3   Katherine   16.5         2     yes
student4       James    NaN         3      no
student5       Emily    9.0         2      no
student6     Michael   20.0         3     yes
student7     Matthew   14.5         1     yes
student8       Laura    NaN         1      no
student9       Kevin    8.0         2      no
student10      Jonas   19.0         1     yes
