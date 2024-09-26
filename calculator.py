import sympy as sp

# Define the matrix
A = sp.Matrix([[1, -1, 1, 1, 6], [2, 0, -1, -1, 5], [2, -2, 0, 1, 4], [0, 1, 1, -1, 3]])

# Get the row echelon form and pivot columns
rref_matrix, pivot_columns = A.rref()

# Print the Row Echelon Form
print("Row Echelon Form:")
print(rref_matrix)
print(rref_matrix)

