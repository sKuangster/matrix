import numpy as np
A = np.array([
    [3.6, 6.6, 4],
    [9, 12.1, 4],
    [5.4, 11, 4]
])

b = np.array([70, 137.5, 95])

A_inv = np.linalg.inv(A)

x = np.dot(A_inv, b)

print("Number of solar plants (x1):", x[0])
print("Number of wind plants (x2):", x[1])
print("Number of waste plants (x3):", x[2])