import numpy as np

a = np.array([[1, 2], [3, 4]]) # Create a 2D array 
print(a)

b = np.array([[5, 6], [7, 8]]) # Create another 2D array
print(b)

Z= a + b  # Add the two arrays
print("Sum of the two arrays:\n", Z)

X = a* b  # Element-wise multiplication of the two arrays
print("Element-wise multiplication of the two arrays:\n", X)

