'''
Created on 6 de abr de 2018

@author: Edison Klafke Fillus

OBS: Comprehension is eager, generate all values. For lazy generation, use generators
'''

# Get the first letter
doctor = ['house', 'cuddy', 'chase', 'thirteen', 'wilson']
print([doc[0] for doc in doctor])


# Create list comprehension: squares
squares = [i**2 for i in range(10)]
print(squares)


# Create a 5 x 5 matrix using a list of lists: matrix
matrix = [[col for col in range(5)] for row in range(5)]

'''
matrix = [[0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4]]
'''

# Print the matrix
for row in matrix:
    print(row)
    
    
    
'''
Using conditionals in comprehensions

[ output expression for iterator variable in iterable if predicate expression ].

'''
# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
new_fellowship = [member for member in fellowship if len(member) >= 7]

# Print the new list
print(new_fellowship)

# Create list comprehension: new_fellowship
new_fellowship = [member if len(member)>=7 else '' for member in fellowship]

# Print the new list
print(new_fellowship)


# Create dict comprehension: new_fellowship
new_fellowship = {member:len(member) for member in fellowship}

# Print the new list
print(new_fellowship)


