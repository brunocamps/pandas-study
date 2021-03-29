import pandas as pd
import numpy as np

obj = pd.Series([4, 7, -5, 3])

print(obj) # prints the object

print(obj.values) # prints the values as arrays
print(obj.index)  # prints the indexes interval

# Create a series which indexes match labels
obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])

print(obj2)
print(obj2.index)

#Selecting a single object
print(obj2['a'])
print(obj2[2])


obj3 = np.exp(obj2)
print(obj3)

print("-------------")

# If there's data inside a Python dictionary, 
# a Pandas Series can be created from it
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = pd.Series(sdata)
print(obj3)