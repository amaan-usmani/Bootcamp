### 1. Importing NumPy

```python
import numpy as np
```

### 2. Creating NumPy Arrays

#### 2.1. Creating Arrays from Python Lists

```python
# 1D array
arr1d = np.array([1, 2, 3, 4, 5])

# 2D array (matrix)
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
```

#### 2.2. Initializing Arrays

```python
# Array of zeros
zeros_arr = np.zeros((3, 3))  # 3x3 array of zeros

# Array of ones
ones_arr = np.ones((2, 4))    # 2x4 array of ones

# Array of a constant value
const_arr = np.full((2, 3), 5)  # 2x3 array filled with 5

# Identity matrix
identity_matrix = np.eye(3)   # 3x3 identity matrix
```

### 3. Basic Array Operations

#### 3.1. Array Attributes

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Shape of the array
print(arr.shape)  # (2, 3)

# Number of dimensions
print(arr.ndim)   # 2

# Number of elements
print(arr.size)   # 6

# Data type of elements
print(arr.dtype)  # int64
```

#### 3.2. Array Indexing and Slicing

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Accessing elements
print(arr[0, 1])  # 2

# Slicing
print(arr[:, 1:])  # [[2, 3],
                   #  [5, 6]]
```

#### 3.3. Array Operations

```python
# Element-wise addition, subtraction, multiplication, division
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

addition = arr1 + arr2
subtraction = arr1 - arr2
multiplication = arr1 * arr2
division = arr1 / arr2

# Dot product
dot_product = np.dot(arr1, arr2)
```

### 4. Broadcasting

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Broadcasting a scalar value
result = arr + 10  # Adds 10 to each element
```

### 5. Universal Functions (ufuncs)

```python
arr = np.array([1, 2, 3, 4])

# Element-wise square root
sqrt_arr = np.sqrt(arr)

# Element-wise exponential
exp_arr = np.exp(arr)
```

### 6. Array Manipulation

```python
# Reshaping arrays
arr = np.array([[1, 2], [3, 4], [5, 6]])
reshaped_arr = arr.reshape((2, 3))

# Flattening arrays
flattened_arr = arr.flatten()
```

### 7. Statistical Functions

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Mean
mean = np.mean(arr)

# Standard deviation
std_dev = np.std(arr)

# Sum
total_sum = np.sum(arr)
```

### 8. Saving and Loading Arrays

```python
# Saving to a file
np.save('my_array.npy', arr)

# Loading from a file
loaded_arr = np.load('my_array.npy')
```
