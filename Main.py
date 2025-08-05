import numpy as np

# 1. Create an array consisting of linearly spaced elements between 0 to 9
original_array = np.linspace(0, 9, 10, dtype=int)
print("Original array:", original_array)

# 2. Replace all odd numbers in this array with -1 without modifying the original array
modified_array = original_array.copy()
modified_array[modified_array % 2 != 0] = -1
print("Modified array with odd numbers replaced:", modified_array)

# 3. Create a new array that contains the original array converted into a 2-dimensional array with 2 rows
array_2d = original_array.reshape(2, -1)
print("2D array:\n", array_2d)

# 4. Iterate through the original array and find out the sum of all elements
total_sum = np.sum(original_array)
print("Sum of all elements in the original array:", total_sum)