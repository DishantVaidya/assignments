import numpy as np
#create a 1D array with 5 elements
a = np.array([1, 2, 3, 4, 5])
print(a)

#attributes of the array

print("size of the array:", a.size) #tells the number of elements in the array
print("shape of the array:", a.shape) #tells the dimensions of the array
print("dimension of the array:", a.ndim) #tells the number of dimensions of the array
print("data type of the array:", a.dtype) #tells the data type of the array, e.g. int, float, etc.

#indexing and slicing the array
print("Elements from index 1 to 4:", a[1:4]) #slicing the array from index 1 to 4
print("Elements on index 0 :", a[0]) #printing the element at index 0

