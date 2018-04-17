'''
Created on 4 de abr de 2018

@author: Edison Klafke Fillus
'''

# Create a list of strings: flash
flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']

# Print each list item in flash using a for loop
for person in flash:
    print(person)
    
# Create an iterator for flash: superspeed
superspeed = iter(flash)

# Print each item from the iterator
print(next(superspeed))
print(next(superspeed))
print(next(superspeed))
print(next(superspeed))

# Create an iterator for range(3): small_value
small_value = iter(range(3))

# Print the values in small_value
print(next(small_value))
print(next(small_value))
print(next(small_value))

# Loop over range(3) and print the values
for i in range(3):
    print(i)

# Create an iterator for range(10 ** 100): googol
googol = iter(range(10 ** 100))

# Print the first 5 values from googol
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))

# Range doesn't create the list, just the iterator
print(googol)

for i in googol:
    if i % 10000 == 0:
        print(i)
    if i == 100000:
        break
  
# If you try to transform in List, you get and Overflow    
# googol_list = list(googol)

# Range accept parameter for start, stop and step
for i in range(5, 50, 5):
    print(i)
    
