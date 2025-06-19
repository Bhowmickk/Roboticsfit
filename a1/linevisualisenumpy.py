import matplotlib.pyplot as plot
import numpy as np

x = np.linspace(-10, 10, 1000)

print("Enter the coefficent of the first line:\n")
a1 = int(input("a1:\t"))
b1 = int(input("b1:\t"))
c1 = int(input("c1:\t"))

print("Enter the coefficent of the second line:\n")
a2 = int(input("a2:\t"))
b2 = int(input("b2:\t"))
c2 = int(input("c2:\t"))

y1 = (c1 - a1 * x) / b1
y2 = (c2 - a2 * x) / b2

plot.plot(x, y1)
plot.plot(x, y2)

plot.axhline(0, color='black', linewidth=0.5)  # x-axis
plot.axvline(0, color='black', linewidth=0.5)  # y-axis

plot.xlabel("x-axis")
plot.ylabel("y-axis")
plot.title("Graph of Two Linear Equations")
plot.grid(True)
plot.show()
