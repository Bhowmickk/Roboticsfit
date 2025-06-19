order = int(input("Enter the order (2 or 3): "))

A = []
print("Enter the matrix row by row:")
for i in range(order):
    row = []
    for j in range(order):
        val = float(input(f"Element [{i+1},{j+1}]: "))
        row.append(val)
    A.append(row)

b = []
print("Enter the vector values:")
for i in range(order):
    val = float(input(f"b{i+1}: "))
    b.append(val)

print("\nMatrix A:")
for row in A:
    print(row)

print("\nVector b:")
print(b)
