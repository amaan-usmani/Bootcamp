import numpy as np

# Creating a NumPy array from a Python list
my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)
print("Original array:")
print(my_array)

# Accessing elements in the array
print("\nAccessing elements:")
print("First element:", my_array[0])
print("Last element:", my_array[-1])

# Array operations
print("\nArray operations:")
print("Sum of elements:", np.sum(my_array))
print("Mean of elements:", np.mean(my_array))
print("Standard deviation:", np.std(my_array))

# Reshaping the array
reshaped_array = my_array.reshape(5, 1)
print("\nReshaped array:")
print(reshaped_array)
