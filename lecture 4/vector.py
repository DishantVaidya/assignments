import numpy as np

#NumPy Program for adding two vectors

u = np.array([1,0]) #creating a vector u
v = np.array([0,1]) #creating a vector v
print("Vector u:", u)
print("Vector v:", v)

#adding two vectors
z=u+v 
print("Sum of vectors u and v:", z,"\n")

#multiplication with a scalar

y=np.array([1,2]) #creating a vector y
print("Vector y:", y)

#multiplying vector y with a scalar
z= 2*y
print("Vector y multiplied by 2:", z,"\n")

#hadamard product (element-wise multiplication)

u = np.array([1,2])
v = np.array([3,2])
print("Vector u:", u)
print("Vector v:", v)

#hadamard product of u and v
z = u * v
print("Hadamard product of u and v:", z, "\n")

#dot product of two vectors

u = np.array([1,2])
v = np.array([3,1])
print("Vector u:", u)
print("Vector v:", v)

#dot product of u and v
z = np.dot(u,v)
print("Dot product of u and v:", z, "\n")

