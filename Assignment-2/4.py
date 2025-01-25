import numpy as np

#Create array and convert to 3*3 matrix
a = np.array([1, 2, 3, 0, 1, 4, 5, 6, 0]).reshape(3, 3)

#Calculate inverse of set a
a_inverse = np.linalg.inv(a)

#Calculate product of a and inverse of a
product_1 = a@a_inverse
product_2 = a_inverse@a

#Create identity matrix
identity = np.identity(3)

#Check if product of set a with its inverse is equal to identity matrix
print(np.allclose(product_1, identity))
print(np.allclose(product_2, identity))
