# List 
# Creating a list
fruits = ['apple', 'banana', 'cherry']

# Accessing elements
print(fruits[0])  # Output: apple

# Modifying elements
fruits[1] = 'blueberry'
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']

# Adding elements
fruits.append('date')
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'date']

# Removing elements
fruits.remove('cherry')
print(fruits)  # Output: ['apple', 'blueberry', 'date']

# List comprehension
squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]




#Tuples
# Creating a tuple
coordinates = (10, 20, 30)

# Accessing elements
print(coordinates[1])  # Output: 20

# Tuples are immutable
# coordinates[1] = 40  # This will raise a TypeError

# Tuples can be used as keys in dictionaries
location = {(10, 20): 'point A', (30, 40): 'point B'}
print(location[(10, 20)])  # Output: point A



#Sets
# Creating a set
unique_numbers = {1, 2, 3, 4, 5}

# Adding elements
unique_numbers.add(6)
print(unique_numbers)  # Output: {1, 2, 3, 4, 5, 6}

# Removing elements
unique_numbers.remove(3)
print(unique_numbers)  # Output: {1, 2, 4, 5, 6}

# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print(set_a.union(set_b))       # Output: {1, 2, 3, 4, 5}
print(set_a.intersection(set_b)) # Output: {3}
print(set_a.difference(set_b))   # Output: {1, 2}

# Creating a dictionary
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}




#Dictionaries
# Accessing elements
print(student['name'])  # Output: John

# Modifying elements
student['age'] = 26
print(student)  # Output: {'name': 'John', 'age': 26, 'courses': ['Math', 'CompSci']}

# Adding elements
student['phone'] = '555-5555'
print(student)  # Output: {'name': 'John', 'age': 26, 'courses': ['Math', 'CompSci'], 'phone': '555-5555'}

# Removing elements
del student['age']
print(student)  # Output: {'name': 'John', 'courses': ['Math', 'CompSci'], 'phone': '555-5555'}

# Dictionary comprehension
squared_numbers = {x: x**2 for x in range(5)}
print(squared_numbers)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
