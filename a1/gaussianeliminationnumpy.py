import numpy as np
from scipy.linalg import lu_solve, lu_factor

print("Enter the coefficent of the first equation:\n")
a1 = int(input("a1:\t"))
b1 = int(input("b1:\t"))
c1 = int(input("c1:\t"))

print("Enter the coefficent of the second equation:\n")
a2 = int(input("a2:\t"))
b2 = int(input("b2:\t"))
c2 = int(input("c2:\t"))

A = np.array([[a1, b1], [a2, b2]])
B = np.array([[c1], [c2]])

LU, piv = lu_factor(A)
x_gauss = lu_solve((LU, piv), B)

print("\nSolution using Gaussian Elimination:")
print(f"x = {x_gauss[0][0]}, y = {x_gauss[1][0]}")

if np.linalg.det(A) != 0:
    A_inv = np.linalg.inv(A)
    x_inverse = np.dot(A_inv, B)
    print("\nSolution using Inverse Matrix Method:")
    print(f"x = {x_inverse[0][0]}, y = {x_inverse[1][0]}")
else:
    print("\nInverse Matrix Method not possible: matrix is singular (det = 0)")
