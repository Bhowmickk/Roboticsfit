import scipy.linalg as lu

order = input("Enter the order of the matrix (e.g., 3x3):\t")
r, c = map(int, order.lower().split('x'))

# Matrix input
matrix = []
for i in range(r):
    row = []
    for j in range(c):
        temp = int(input(f"Enter the element in {i+1}th row, {j+1}th column: "))
        row.append(temp)
    matrix.append(row)

# LU Decomposition
P, L, U = lu.lu(matrix)

# Printing results
print("After LU decomposition......\n")
print("Permutated matrix (P):")
for row in P:
    print(row)

print("\nLower triangular matrix (L):")
for row in L:
    print(row)

print("\nUpper triangular matrix (U):")
for row in U:
    print(row)
