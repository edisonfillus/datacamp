'''
Created on 4 de abr de 2018

@author: Edison Klafke Fillus
'''
from functools import reduce

# Create a list of strings: stark
stark = ['robb', 'sansa', 'arya', 'eddard', 'jon']

# Use reduce() to apply a lambda function over stark: result
result = reduce(lambda item1, item2 : item1 + item2, stark)

# Print the result
print(result)
