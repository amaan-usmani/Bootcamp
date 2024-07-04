# 1. Identifying Null Values

# You can identify null values in a DataFrame using the isnull() and notnull() methods.


import pandas as pd

# Example DataFrame
data = {'A': [1, 2, None], 'B': [None, 2, 3]}
df = pd.DataFrame(data)

# Check for null values
print(df.isnull())
print(df.notnull())

# 2. Dropping Null Values

# You can drop rows or columns with null values using the dropna() method.


# Drop rows with any null values
df_dropped_rows = df.dropna()

# Drop columns with any null values
df_dropped_cols = df.dropna(axis=1)

# 3. Filling Null Values

# You can fill null values using the fillna() method.


# Fill null values with a specified value
df_filled = df.fillna(0)

# Fill null values using a method (e.g., forward fill or backward fill)
df_ffill = df.fillna(method='ffill')  # Forward fill
df_bfill = df.fillna(method='bfill')  # Backward fill

# 4. Filling Null Values with Computed Values

# You can fill null values with computed values such as the mean, median, or mode of the column.


# Fill null values with the mean of the column
df['A'] = df['A'].fillna(df['A'].mean())

# Fill null values with the median of the column
df['B'] = df['B'].fillna(df['B'].median())

# 5. Replacing Null Values with Interpolation

# You can interpolate missing values using/ the interpolate() method.


# Interpolate missing values
df_interpolated = df.interpolate()

# 6. Handling Null Values during DataFrame Operations

# When performing operations on DataFrames, you can control how null values are handled.


# Sum columns, skipping NaN values
column_sum = df.sum()

# Mean of columns, skipping NaN values
column_mean = df.mean()
# Example Code
# Here is an example combining several of these methods:


import pandas as pd

# Example DataFrame
data = {'A': [1, 2, None, 4], 'B': [None, 2, 3, None], 'C': [5, None, None, 8]}
df = pd.DataFrame(data)

# Identify null values
print("Null values in DataFrame:")
print(df.isnull())

# Drop rows with any null values
df_dropped_rows = df.dropna()
print("\nDataFrame after dropping rows with null values:")
print(df_dropped_rows)

# Fill null values with a specified value
df_filled = df.fillna(0)
print("\nDataFrame after filling null values with 0:")
print(df_filled)

# Fill null values with the mean of each column
df['A'] = df['A'].fillna(df['A'].mean())
df['B'] = df['B'].fillna(df['B'].mean())
df['C'] = df['C'].fillna(df['C'].mean())
print("\nDataFrame after filling null values with the mean of each column:")
print(df)

# Interpolate missing values
df_interpolated = df.interpolate()
print("\nDataFrame after interpolating missing values:")
print(df_interpolated)
